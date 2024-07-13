function checkInput() {
	var error = document.getElementById("error");

	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;

	if (username == "" || password == "") {
		error.hidden = false;
		return;
	}

	console.log(username + ":" + password);

	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/handle_post", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify({
    	"username": username,
		"password": password
	}));

	xhr.onreadystatechange = function () {
		if (this.readyState != 4) return;
	
		if (this.status == 200) {
			var data = JSON.parse(this.responseText);
			console.log(data.completed);
			error.hidden = false;
			error.innerText = data.completed;

			if (data.go) {
				setCookie("username", username);
				setCookie("password", data.hashed);
				window.location.href = window.location.origin;
			}
	
			// we get the returned data
		}
	
		// end of state change: it can be after some time (async)
	};
}

function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	let expires = "expires="+d.toUTCString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}