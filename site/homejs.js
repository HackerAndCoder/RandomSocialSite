var cookies = document.cookie;

var content = ""

if (!cookies) {
	console.log("redirect to log in / sign up")
	window.location.assign("/signin.html")
}

getMoreContent();

function postRequest(json_data) {
	const xhr = new XMLHttpRequest();
        xhr.open("POST", window.location.href);
        xhr.setRequestHeader("Content-Type", "application/json");
        const body = json_data;
        xhr.onload = () => 
        {
            if (xhr.readyState == 4 && xhr.status == 201 || xhr.status == 200) 
            {
				if (JSON.parse(json_data).request == "post") {
					return;
				}
				console.log(xhr.responseText);
				content = xhr.responseText;
				
				return_packet = JSON.parse(content);
				posts = return_packet["content"];

				addContentToPage(posts)

				//console.log(posts);
				
            } else 
            {
                console.log(`Error: ${xhr.status}`);
            }
        };
        xhr.send(body);
}

function getMoreContent() {
	postRequest(JSON.stringify(
		{
			"username": getCookie("username"),
			"request":"content"
		}
	))
}

function postMessage(message) {
	postRequest(
		JSON.stringify(
			{
				"username": getCookie("username"),
				"request": "post",
				"message": message
			}
		)
	)
}

function getCookie(cname) {
	let name = cname + "=";
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(';');
	for(let i = 0; i <ca.length; i++) {
	  let c = ca[i];
	  while (c.charAt(0) == ' ') {
		c = c.substring(1);
	  }
	  if (c.indexOf(name) == 0) {
		return c.substring(name.length, c.length);
	  }
	}
	return "";
}

function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	let expires = "expires="+d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
  

function addContentToPage(content) {
	template = "<div id=\"spacer\"></br></div><div class=\"post\" {color_if_liked}><div class=\"innerContent\"><h3 class=\"profname\"><img src=\"prof/{username}.png\" class=\"profpic\">{username}</h3> <h4 class=\"messagecontents\">{message}</h4><div width=\"100%\" style=\"max-height: 20px;\" class=\"actions\"><button class=\"action\" onclick=\"like(this, {id})\">{user_liked}</button><div class=\"like_num\">{like_num} likes</div></div></div></div>"
	for (var i = 0; i < content.length; i++) {
		let c = JSON.parse(content[i]);

		console.log("adding content: " + content[i]);
		
		let to_write = template;
		if (c["liked"]) {
			to_write = to_write.replace('{color_if_liked}', 'style="border-color: green;"');
			to_write = to_write.replace('{user_liked}', "Unlike");
		} else {
			to_write = to_write.replace('{color_if_liked}', '');
			to_write = to_write.replace("{user_liked}", "Like");
		}

		to_write = to_write.replace('{message}', c["message"]);
		to_write = to_write.replace('{username}', c["username"]);
		to_write = to_write.replace('{username}', c["username"]);
		to_write = to_write.replace('{id}', c["id"]);
		to_write = to_write.replace('{like_num}', c["like_num"]);

		console.log(to_write);

		document.getElementById("content").innerHTML += to_write;
	}
}

window.onscroll = function()
{
    var scrollHeight, totalHeight;
    scrollHeight = document.body.scrollHeight;
    totalHeight = window.scrollY + window.innerHeight;

    if(totalHeight >= scrollHeight)
    {
        console.log("at the bottom");
		getMoreContent();
    }
}


function signout() {
	setCookie("username", "", -1);
	setCookie("password", "", -1);
	window.location.reload();
}

document.getElementById("username").innerHTML = getCookie("username")

function mp() {
	let message = prompt("What do you want to post?", "");
	postMessage(message);
}

function like(button, id) {
	if (button.innerHTML == "Unlike") {
		unlike(button, id);

		let t = button.parentNode.getElementsByClassName('like_num')[0].innerHTML.split(" ");
	
		t[0] = Number(t[0]) - 1;

		button.parentNode.getElementsByClassName('like_num')[0].innerHTML = t.join(" ")

		return;
	}

	
	let t = button.parentNode.getElementsByClassName('like_num')[0].innerHTML.split(" ");
	
	t[0] = Number(t[0]) + 1;

	button.parentNode.getElementsByClassName('like_num')[0].innerHTML = t.join(" ")

	button.parentNode.parentNode.parentNode.style.borderColor = "green";
	button.innerHTML = "Unlike";
	postRequest(JSON.stringify(
		{
			"username": getCookie("username"),
			"request": "like",
			"id": id
		}
	))
}

function unlike(button, id) {
	button.parentNode.parentNode.parentNode.style.borderColor = "rgb(202, 202, 202)";
	button.innerHTML = "Like";
	postRequest(JSON.stringify(
		{
			"username": getCookie("username"),
			"request": "unlike",
			"id": id
		}
	))
}

function accountsettings() {
	window.location.href = window.location.origin + "/account.html";
}