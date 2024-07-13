from flask import Flask, Response, request, redirect, json
import os, json, database, post_handler, random
app = Flask(__name__)

database.restore_from_disk()

def get_post(id):
    p = post_handler.get_post(id)
    return get_plaintext_file("template.html").replace('{message}', p["message"]).replace("{username}", p["username"])

def get_plaintext_file(path):
    with open(os.path.join('site', path)) as f:
        return f.read()
    
def get_binary_file(path):
    with open(os.path.join('site', path), mode="rb") as f:
        return f.read()
    
def get_extention(path):
    try:
        p = path.split('.')
        return p[-1]
    except:
        return None

@app.route('/')
def home_return():
    return get_plaintext_file('home.html')

@app.route('/', methods = ["POST"])
def return_content():
    return json.dumps({"test":"good","content_length":100,"content":[get_post(random.randrange(0, post_handler.get_post_id_number())) for _ in range(100)]})

@app.route('/handle_post', methods = ['POST'])
def handle_signin():
    try:
        data = json.loads(request.get_data(as_text=True))
        username = data["username"]
        password = data["password"]
        
        print(f"login or sign up : {username}:{password}")
    except:
        return '{"completed":"Something went wrong, please try again","go":false,"hashed":"'+str(password)+'"}'
    
    if database.does_user_exist(username):
        if not database.is_right_password(username, str(password)):
            return '{"completed":"Password is incorrect","go":false,"hashed":"'+str(password)+'"}'

    if not database.does_user_exist(username):
        database.set_user_and_password(username, password)

    database.save_to_disk()
    return '{"completed":"Redirecting...", "go":true,"hashed":"'+str(password)+'"}'

@app.route('/<a>')
def hello_world(a):
    if get_extention(a) in ('png', 'jpg', 'jpeg', ''):
        print(f'bin path {a} extention {get_extention(a)}')
        return get_binary_file(a)
    try:
        return Response(get_plaintext_file(a), 
                        mimetype=f'text/{get_extention(a) if get_extention(a) != "js" else "javascript"}')
    except:
        return ""

@app.route('/prof/<a>')
def prof_return(a):
    return hello_world(os.path.join('prof', a))

if __name__ == '__main__':
    app.run(host='0.0.0.0')