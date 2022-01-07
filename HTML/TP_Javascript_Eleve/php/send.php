<?php
 // Récupération des données du formulaire
 $nom = $_POST["nom"];
 $sel = $_POST["sel"];
 $in = $_POST["in"];
 $ra = $_POST["ra"];
 $fo = $_POST["fo"];
 $en = $_POST["en"];
 $pr = $_POST["pr"];
 $pr = $_POST[""];
 $fu = $_POST["fu"];
 $rs = $_POST["rs"];
 $cr = $_POST["cr"];
 $msg = $_POST["msg"];
 $em = $_POST["em"];

 // Texte à envoyer
 $texte = "Nom : $nom\n";
 $texte = $texte . "Genre : $gender\n";
 $texte = $texte . "Personnage : $sel\n";
 $texte = $texte . "Capacité intelligence : $in\n";
 $texte = $texte . "Personnage : $sel\n";
 $texte = $texte . "Personnage : $sel\n";
 $texte = $texte . "Personnage : $sel\n";
 $texte = $texte . "Personnage : $sel\n";
 $texte = $texte . "Message personnel : $msg\n";
 $texte = $texte . "Email de contact : $em\n";
 $texte = stripslashes($texte);

 // Destinataire et objet du message
 $dest = "inscriptions@fortnite.com";
 $obj = "Formulaire d\'inscription";

 //Entête masqué (encodage des caractères)
 $headers = "Content-type: text-plain; charset=utf-8";

 // Envoi du message, puis confirmation sur la page
 $envoi_bon = mail($dest, $obj, $texte, $headers);
 if ($envoi_bon) { echo "Envoi OK"; }
 else { echo "Erreur"; }
?>