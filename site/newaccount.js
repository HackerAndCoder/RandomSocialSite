function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	let expires = "expires="+ d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
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

function fillTopicContainer() {
  var topics = [];
  var xhr = new XMLHttpRequest();
	xhr.open("POST", "/", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(
	 JSON.stringify
	  (
		 {
      "request": "topics"
		 }
		)
	);
	
  xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 201 || xhr.status == 200) {
      topics = JSON.parse(xhr.responseText).topics;
    }
  }

  for (var i = 0; i < topics.length; i++) {
    var t = document.createElement("div");
    t.class = "topic";
    t.innerText = topics[i];
    document.getElementById("topicscontainer").appendChild(t);
  }
}

function goBackToSignin() {
  window.location.href = "/signin.html";
}
  
let welcometext = document.getElementById("welcometext");
welcometext.innerHTML = welcometext.innerHTML.replace('{username}', getCookie("username"));

fillTopicContainer();