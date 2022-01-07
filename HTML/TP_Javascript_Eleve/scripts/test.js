function test(){
	var a = document.getElementById("pw");
	var b = document.getElementById("pw2");
	if(a.value==b.value) {
		alert("Mot de passe correct");
	} else {
		alert("Mot de passe incorrect");
		//this.setCustomValidity();
		document.getElementById("pwd2").className = "invalid";
	}
}

function affname(){
	var d = document.getElementById("nom");
	alert("Votre personnage s'appelle : " +d.value);
}

/*function namecorrect() {
	var c = document.getElementById("nom");
	if(a.value=='') {
		document.getElementById("nom").className = "invalid";
	}
}*/