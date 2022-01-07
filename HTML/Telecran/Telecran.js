
var canvasKeyboard, telecran, width, height; // For drawing the canvas
var downcheck, upcheck, rightcheck, leftcheck; // For checking what direction is clicked

// Curent position

var x=345;//position initiale du curseur
var y=250;
var xB1=25;// position du bouton gauche
var yB1=475;
var xB2=665;// position du bouton droit
var yB2=475;
var angleB1=-1.57;// position initiale du point du bouton gauche
var angleB2=-1.57;
var widthEcranOr=590// taille de l'écran
var heightEcranOr=400;
var deltaH=(Math.PI*2)/heightEcranOr;// correspondance entre le pas de déplacement vertical le pas de rotation du bouton (une rotation de 2PI du bouton gauche correspond à la hauteur de l'écran
var deltaW=(Math.PI*2)/widthEcranOr;
var deltaDown=5;//pas de déplacement vertical avec les flèches left et right
var deltaRight=5;
// Initialisation
function init() {

    canvasTelecran = document.getElementById('telecran');       
    telecran = canvasTelecran.getContext('2d');
	
	
	
	document.onkeydown = deplacePointe;
	document.onkeyup = canvasStop;
}

function draw(x1,y1) {
	telecran.beginPath();
	telecran.strokeStyle = 'rgba(255,0,255,1)';
    telecran.moveTo(x,y);
	telecran.lineTo(x1,y1);
	telecran.stroke(); 
}
function drawTelecran(){
	// le contour du Télécran

	// l'écran or

	// la pointe du Télécran
 
	//les molettes

	// les ascenceurs

	// le texte
	
}

function drawDisk(x,y){// le corps de la molette
	
	}

function drawPoint(x,y,angle){// le point bleu de la molette
	
}

function drawButton(x,y,angle){// la molette
	
}

function ascenseurH(){
	// l'ascenceur
	
	// le curseur
	
}

function ascenseurV(){
	// l'ascenceur
	
	// le curseur
	
}

function reset(){
	drawTelecran();
}

function deplacePointe(e) {
  	if(e.keyCode == '39') {//touche Right
		//
  	}
	else reset();
}



// When the user stops pressing a key, check which key it is and set it to false
function canvasStop(e) {
	
	if(e.keyCode == '38') {
		upcheck = false;
	}
	if(e.keyCode == '40') {
		downcheck = false;
	}
	if(e.keyCode == '37') {
		leftcheck = false;
	}
	if(e.keyCode == '39') {
		rightcheck = false;
	}

}