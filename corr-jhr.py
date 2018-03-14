#coding: utf-8

### Bonjour, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses ###

### Tu as eu de la malchance.
### Comme je te l'écrivais, j'ai essayé d’ouvrir les pages de joueurs. Ça ne marche pas.
### Je n’ai pas vu ça souvent, mais ce qui se passe, c’est que
### les tableaux de ces pages du site de la LHJMQ sont générées par ton browser par un script JavaScript
### qui va chercher de l’info APRÈS la connexion initiale au site.
### Bref, ça exigerait un truc qui s’appelle Selenium et qu’on n’a malheureusement pas le temps de voir en classe.

### Je vois que tu as essayé d’aller chercher les infos pour chaque joueur se trouvant dans les pages de repêchage que tu as téléchargées.
### Dans le code ci-dessous, je t'indique comment y parvenir

import csv
import requests
from bs4 import BeautifulSoup

### Première chose: définissons le nom du fichier CSV qui va contenir les infos qu'on ramasse

fichier = "repechage.csv"

# entetes = {
# 	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
# 	"Cookie":"_ga=GA1.3.1932293326.1512249502; _icl_current_language=fr; _gid=GA1.3.10619140.1519686716"
# }

for n in range(2011,2018):
	url = "{}.html".format(n)
	#print (url)

	# contenu = requests.get(url, headers=entetes)
	page = BeautifulSoup(open(url),"html.parser")
	#print(page.h1)
	#print(page.tbody)

	for ligne in page.find_all("tr",class_="table__tr"):
		 # print(ligne.text)
		 # print (ligne.a)

### Jusqu'ici tout va bien!
### La variable «ligne» correspond à un joueur
### On peut donc dès maintenant se créer une liste qui va contenir toutes les infos pour ce joueur
		joueur = []
### On commence par y inclure l'année
		joueur.append(n)

### Pour recueillir les infos sur ce joueur, voici ma suggestion:

		for infos in ligne.find_all("td"):
			print(infos["data-reactid"])
			# print(infos.text)

			if "Round" in infos["data-reactid"]:
				ronde = infos.text.strip()
				print(ronde)
				joueur.append(ronde)
			elif "DraftOverall" in infos["data-reactid"]:
				rang = infos.text.strip()
				print(rang)
				joueur.append(rang)
			elif "Team" in infos["data-reactid"]:
				equipe = infos.text.strip()
				print(equipe)
				joueur.append(equipe)
			elif "PlayerName" in infos["data-reactid"]:
				nom = infos.text.strip()
				try:
					url = infos.a["href"]
				except:
					url = "?"
				print(nom)
				print(url)
				joueur.append(nom)
				joueur.append(url)
			elif "position" in infos["data-reactid"]:
				position = infos.text.strip()
				print(position)
				joueur.append(position)
			elif "Height" in infos["data-reactid"]:
				taille = infos.text.strip()
				print(taille)
				joueur.append(taille)
			elif "Weight" in infos["data-reactid"]:
				poids = infos.text.strip()
				print(poids)
				joueur.append(poids)
			elif "birthdate" in infos["data-reactid"]:
				dateNaissance = infos.text.strip()
				print(dateNaissance)
				joueur.append(dateNaissance)
			elif "lastteam" in infos["data-reactid"]:
				dernEquipe = infos.text.strip()
				print(dernEquipe)
				joueur.append(dernEquipe)
			elif "prov" in infos["data-reactid"]:
				province = infos.text.strip()
				print(province)
				joueur.append(province)
			elif "division" in infos["data-reactid"]:
				division = infos.text.strip()
				print(division)
				joueur.append(division)
			else:
				joueur.append("?")

		print(joueur)

### Puis, on écrit les infos dans notre fichier CSV
		carey = open(fichier,"a")
		price = csv.writer(carey)
		price.writerow(joueur)

		 
		 #Ronde = page.find("td", attrs={"table__td table__td-- text-col":"data-reactid":re.compile('*$Round\.1\.0')})		 
		 
		 # Nom = ligne.find("a", {"data-reactid":".0.0.3.1.2.0.1.0.$PlayerName.0"}).text
		 # print (Nom)
		 #Ce code est le seul qui fonctionne, mais je dois réussir à changer le dernier chiffre avant $PlayerName pour chaque joueur. J'en suis incapable.

		 # Ronde = ligne.find("a").text
		 # print (Ronde)
		 #Rien ne fonctionne...

		 #J'ai travaillé énormément sur le code, mais je n'ai pas été capable de moissonner les données... toutes les informations dans le tableau de repêchage ont le même code (avec le même nom de classe et la même balise). Donc, impossible de les différencier, python prend toujours le premier, soit le la ronde...)





		 #Nom = ligne.find("td")
		 #print (Nom)

		 #equipe = page.find("td", class_="table__td table__td-- text-col").Round
		 
		 #print(equipe)



		 #lien=ligne.a(["href"]

		 #if "href" is not None:
		 	#print(ligne.a(["href"]))
		 

		 #else: 
			#print(None)





		 #joueur=[]
		 #for joueur in page.find_all("td",class_="table__td table__td-- text-col"):
		 	#lien=.a["href"]

		 	#print(lien)
			
#Bonjour Jean-Hugues,

# J'ai travaillé pendant toute la semaine de relâche sur ce projet, mais en vain...Le site de la LHJMQ est très compliqué à moissonner. Comme je l'explique dans mon code,toutes les informations dans le tableau de repêchage ont le même code (avec le même nom de classe et la même balise). Donc, impossible de les différencier, python prend toujours le premier, soit le la ronde... De plus, pour le nom du joueur, j'ai fait la chose que tu m'a dis de faire, mais j'ai toujours un message d'erreur qui revient...(AttributeError: 'NoneType' object has no attribute 'text'). Après plusieurs recherches, je n'ai pas trouvé la façon d'isoler les données. J'ai trouvé une façon, mais je dois pouvoir changer le dernier chiffre du data-reactid pour chaque joueur, une autre chose que je n'ai pas été capable. 

