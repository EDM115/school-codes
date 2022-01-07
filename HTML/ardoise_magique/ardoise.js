/************************************/
/* Fonctions pour l'ardoise magique */
/************************************/

var canvas;// panneau de dessin html

var penDown = false;// booléen indiquant si le pinceau est levé ou abaissé
var x, y;// coordonnées de la souris
var form;// forme du pinceau

function init() {// initialisation de l'ardoise
	// on récupère le nom du canvas HTML
	canvas = document.getElementById('ardoise');
	context = canvas.getContext('2d');// panneau de dessin sur lequel s'appliquent les fonctions
    // valeurs par défaut du pinceau couleur, taille, forme
    context.strokeStyle = '#000';
    context.lineWidth = '1';
    context.form=1;// carré vide
	// Evénements de la souris     addEventListener(mot clé, action, false);
	canvas.addEventListener('mousemove', move, false);
	canvas.addEventListener('mousedown', clicked, false);
	canvas.addEventListener('mouseup', released, false);
}

function clicked() {
	// on abaisse le pinceau pour dessiner
	context.beginPath();
	context.moveTo(x, y);
	penDown = true;
	draw();
}

// Pour déterminer les coordonnées de la souris
function getOffset(e) {
    var cx = 0;
    var cy = 0;
    
    while(e && !isNaN(e.offsetLeft) && !isNaN(e.offsetTop)) {
        cx += e.offsetLeft - e.scrollLeft;
        cy += e.offsetTop - e.scrollTop;
        e = e.offsetParent;
    }
    return { top: cy, left: cx };
}

function move(e) {
	//  position de la souris
	if(e.offsetX || e.offsetY) {
		x = e.pageX - getOffset(document.getElementById('ardoise')).left - window.pageXOffset;
		y = e.pageY - getOffset(document.getElementById('ardoise')).top - window.pageYOffset;
	}
	else if(e.layerX || e.layerY) {
		x = (e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft)
		- getOffset(document.getElementById('ardoise')).left - window.pageXOffset;
		y = (e.clientY + document.body.scrollTop + document.documentElement.scrollTop)
		- getOffset(document.getElementById('ardoise')).top;
	}	
		
	// on dessine seulement si le pinceau est abaissé
	if (penDown) {
		draw();
	}
}
// On dessine avec la forme du pinceau
function draw(){
	if (context.form==1){// on dessine un carré
		carre();
	} 
	else
	{//on dessine un carré plein
		//context.fillRect(x,y,context.lineWidth,context.lineWidth);
		//context.fill();
		carre_plein();
	} 
	// on peut remplacer les if imbriqués par un switch si la variable est un entier ou un caractère
/*
	witch(context.form){
	case 1: e=context.lineWidth;
			context.lineWidth=1;
			context.beginPath();
			context.rect(x,y,e,e);
			context.stroke();
			context.lineWidth=e;
			break;
	default: 
		    context.fillRect(x,y,context.lineWidth,context.lineWidth);
			context.fill();
	}
*/	
}
function carre(){
		e = context.lineWidth;// e conserve la taille du pinceau 
		context.lineWidth=1;
		context.beginPath();
		context.rect(x,y,e,e);
		context.stroke();
		context.lineWidth=e; // le pinceau récupère sa taille
}

function carre_plein(){
		context.fillRect(x,y,context.lineWidth,context.lineWidth);
		context.fill();
}

function cercle(){
		e = context.lineWidth;
		context.beginPath();
		context.arc(centerX, centerY, 0, 2*Math.PI);
		context.fill();
		context.lineWidth=e;
		context.stroke();
}

function disk(){
		
}

function released() {
	// souris relâchée: on lève le pinceau
	if (penDown) {
		penDown = false;	
	}
}
// on change la forme du pinceau
function changeForm(s) {
	context.form= s;
}

// on change la taille du pinceau
function changeSize(s) {
	context.lineWidth = s;
}

// on change la couleur du pinceau et du remplissage
function changeColor(c) {
	context.strokeStyle = c;
	context.fillStyle = c;
}

