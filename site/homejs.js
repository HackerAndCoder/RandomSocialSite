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
				console.log(xhr.responseText);
				content = xhr.responseText;
				addContentToPage(JSON.parse(content));
				
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
			"password": getCookie("password"),
			"request":"content"
		}
	))
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
	for (var i = 0; i < content.content_length; i++) {
		document.getElementById("content").innerHTML += content.content[i];
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
		getMoreContent()
    }
}


function signout() {
	setCookie("username", "", -1);
	setCookie("password", "", -1);
	window.location.reload();
}