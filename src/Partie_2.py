# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:27:31 2020

@author: Julie

Interrogation de la base de données :
    - programme avec menu
    - connexion automatique à la base de données
    - déconnexion à la fermeture du programme
    
"""

import sqlite3, sys

# Connexion à la base de données & Création d'un curseur
connexion = sqlite3.connect("base.db")
cursor = connexion.cursor()

###############################################################################
#                               MENU                                          #
###############################################################################   
def afficheMenu():
    print()
    print("                            MENU PRINCIPAL")    
    print()
    global rep
    print("        1 - Afficher la liste des régions")
    print()
    print("        2 - Afficher la liste des départements")
    print()
    print("        3 - Afficher les données d'une région au choix")
    print()
    print("        4 - Afficher les données d'un département et un thème :") 
    print("            social ou environnemental")
    print()
    print("        5 - Afficher la liste des départements dont type d'énergie")
    print("            (éolien, photovoltaïque, autre) a augmenté entre ")
    print("            les 2 années de référence, dans l'ordre décroissant")
    print()           
    print("        6 - Liste des départements dont la région a eu une production") 
    print("            de granulats > à 25K tonnes en 2014")
    print()
    print("        7 - Liste des 5 départements avec le plus grand taux")
    print("            d'énergie éolien comme source de puissance électrique")
    print("            en 2015")
    print()
    print("        8 - Région dont le département à le plus faible taux de") 
    print("            valorisation matière organique en 2013")
    print()
    print("        9 - Part de l'argriculture bio dans la surface agricole") 
    print("            totale du département contenant le plus garnd porcentage") 
    print("            de population éloignée de plus de 7 minutes des services")
    print("            de santé de proximité")
    print()
    print("       10 - Taux de pauvreté, en 2014, des régions dont la part des")
    print("            jeunes non insérés est > à 30%")
    print()
    print("       11 - Poids de l'économie sociale dans les emplois salariés")
    print("            de la région dont la source de la puissance électrique")
    print("            en énergies renouvelables provenait à, au moins, 10%")
    print("            de l'énergie photovoltaïque et dont la part de ")
    print("            l'agriculture bio, dans la surface totale, était, ")
    print("            d'au moins 5%, en 2015")
    print()
    print("       0 -  Quitter le programme")
    rep = int(input())
###############################################################################
#                           LES REQUÊTES SQL                                  #
###############################################################################
def connexionBD():
    print("        /----------------------------------------------------------\\")
    print("        |                     Bienvenue !                          |")
    print("        |                                                          |")
    print("        |         Connexion à la base de données réussite !        |")
    print("        |                                                          |")
    print("        |              Que voulez-vous faire ?                     |")
    print("        \\----------------------------------------------------------/")

def questionOne():
    requete = "SELECT nccenr FROM REGION;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 1 : ", resultat)

    
def questionTwo():
    requete = "SELECT nccenr FROM DEPARTEMENT"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 2 : ", resultat)


def questionThree():
    choix = input("Vous voulez afficher quelle région (ex : Corse) ? ")
    requete = "SELECT R.nccenr, S.Taux_de_pauvreté_2014, S.Part_des_jeunes_non_insérés_2014, S.Part_des_jeunes_non_insérés_2009, S.Poids_de_l_économie_sociale_dans_les_emplois_salariés_du_territoire_2015 FROM REGION R join SOCIALREG S on R.nccenr = S.REGIONS WHERE nccenr LIKE \"%" + choix + "%\";"
    cursor.execute(requete)
    resultat = cursor.fetchone()
    print()
    print("Dans l'ordre, Nom de la région, Taux de pauvreté en 2014, Part des jeunes non insérés (2014 et 2009), Poids de l'économie sociale dans les emplois salariés du territoire en 2015 : ", resultat)
        

def questionFour():
    choix_Dep = input("Veuillez choisir un département (ex : Ain) : ")
    choix_Theme = input("Veuillez choisir un thème (Social ou Environnement) : ")
    print()
    if (choix_Theme == "Social"):
        requete = "SELECT Espérance_de_vie_des_hommes_à_la_naissance_2015, Espérance_de_vie_des_hommes_à_la_naissance_2010, Espérance_de_vie_des_femmes_à_la_naissance_2015, Espérance_de_vie_des_femmes_à_la_naissance_2010, Part_de_la_population_éloignée_de_plus_de_7_mn_des_services_de_santé_de_proximité_2016, Part_de_la_population_estimée_en_zone_inondable_2013, Part_de_la_population_estimée_en_zone_inondable_2008 FROM SOCIALDEP WHERE DEPARTEMENTS LIKE \"%" + choix_Dep + "%\";"
        cursor.execute(requete)
        resultat = cursor.fetchone()
        print("Dans l'ordre, Espérence de vie des hommes à la naissance (2015 et 2010), Espérance de vie des femmes à la naissance (2015 et 2010), Part de la population éloignée de plus de 7 minutes des services de santé de proximité (2016), Part de la population estimée en zone inondable (2013 et 2008) :", resultat)
    if (choix_Theme == "Environnement"):
        requete = "SELECT Taux_de_valorisation_matière_et_organique_2013, Taux_de_valorisation_matière_et_organique_2009, Part_de_surfaces_artificialisées_2012, Part_de_surfaces_artificialisées_2006, Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016, Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2010, Production_de_granulats_2014, Production_de_granulats_2009, Eolien_2015, Eolien_2010, Photovoltaïque_2015, Photovoltaïque_2010, Autre_2015, Autre_2010 FROM ENVIRONNEMENTDEP WHERE DEPARTEMENTS LIKE \"%" + choix_Dep + "%\";"
        cursor.execute(requete)
        resultat = cursor.fetchone()
        print("Dans l'ordre, Taux de valorisation des matières organiques (2013 et 2009), Part de la surface artificialisées (2012 et 2006), Part de l'agriculture bio dans la surface agricole totale (2016 et 2010), Production de granulats (2014 et 2009), Eolien (2015 et 2010), Photovoltaïque (2015 et 2010), Autre (2015 et 2010) : ", resultat)

def questionFive():
    choix_Energie = input("Veuillez choisir un type d'énergie (éolien, photovoltaïque ou autre) : ")
    print()
    if (choix_Energie == "éolien"):
         requete = "SELECT DEPARTEMENTS FROM ENVIRONNEMENTDEP WHERE \"Eolien_2015\" - \"Eolien_2010\" > 0 ORDER BY \"Eolien_2015\" - \"Eolien_2010\" DESC;"
         cursor.execute(requete)
         resultat = cursor.fetchall()
         print("Réponse à la question 5 (éolien) : ", resultat)
    if (choix_Energie == "photovoltaïque"):
        requete = "SELECT DEPARTEMENTS FROM ENVIRONNEMENTDEP WHERE \"Photovoltaïque_2015\" - \"Photovoltaïque_2010\" > 0 ORDER BY \"Photovoltaïque_2015\" - \"Photovoltaïque_2010\" DESC;"
        cursor.execute(requete)
        resultat = cursor.fetchall()
        print("Réponse à la question 5 (photovoltaïque) : ", resultat)
    if (choix_Energie == "autre"):
        requete = "SELECT DEPARTEMENTS FROM ENVIRONNEMENTDEP WHERE \"Autre_2015\" - \"Autre_2010\" > 0 ORDER BY \"Autre_2015\" - \"Autre_2010\" DESC;"
        cursor.execute(requete)
        resultat = cursor.fetchall()
        print("Réponse à la question 5 (autre) : ", resultat)


def questionSix():
    requete = "SELECT D.libelle FROM (SELECT sr.REGIONS, sr.total FROM( SELECT REGIONS, SUM(Production_de_granulats_2014) total FROM DEPARTEMENT D INNER JOIN ENVIRONNEMENTDEP E on D.nccenr = E.DEPARTEMENTS GROUP BY REGIONS) as sr WHERE sr.total > 25000000 AND sr.total !=0) as sv INNER JOIN  DEPARTEMENT D on D.REGIONS = sv.REGIONS JOIN REGION R on D.REGIONS = R.REGIONS ORDER BY sv.REGIONS;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 6 : ", resultat)

def questionSeven():
    requete = "SELECT DEPARTEMENTS FROM ENVIRONNEMENTDEP ORDER BY Eolien_2015 DESC LIMIT 5;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 7 : ", resultat)

def questionEight():
    requete = "SELECT R.libelle FROM REGION R join DEPARTEMENT D on R.REGIONS = D.REGIONS join ENVIRONNEMENTDEP E on D.libelle = E.DEPARTEMENTS WHERE Taux_de_valorisation_matière_et_organique_2013 !=0 ORDER BY Taux_de_valorisation_matière_et_organique_2013 ASC LIMIT 1;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 8 : ", resultat)    

def questionNine():
    requete = "SELECT E.Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016 FROM ENVIRONNEMENTDEP E join SOCIALDEP S on E.DEPARTEMENTS = S.DEPARTEMENTS ORDER BY Part_de_la_population_éloignée_de_plus_de_7_mn_des_services_de_santé_de_proximité_2016 DESC LIMIT 1;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 9 : ", resultat)
    
def questionTen():
    requete = "SELECT Taux_de_pauvreté_2014 FROM SOCIALREG WHERE Part_des_jeunes_non_insérés_2014 > 30 AND Taux_de_pauvreté_2014 !=0;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 10 : ", resultat)
    
def questionEleven(): 
    requete = "SELECT Poids_de_l_économie_sociale_dans_les_emplois_salariés_du_territoire_2015 FROM SOCIALREG S join REGION R on S.REGIONS = R.nccenr join DEPARTEMENT D on R.REGIONS = D.REGIONS join ENVIRONNEMENTDEP E on D.nccenr = E.DEPARTEMENTS WHERE Photovoltaïque_2015 >= 10 AND Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016 >= 5;"
    cursor.execute(requete)
    resultat = cursor.fetchall()
    print("Réponse à la question 11 : ", resultat)
    
def deconnexionBD():
    connexion.close()
    print("        /----------------------------------------------------------\\")
    print("        |      Vous avez été déconnecté de la base de données !    |")
    print("        |                                                          |")
    print("        |                      A bientôt !                         |")
    print("        \\----------------------------------------------------------/")

###############################################################################
#                          PROGRAMME PRINCIPAL                                #
###############################################################################       
while(True):
    connexionBD()
    afficheMenu()
    rep = int(rep)
        
    if (rep == 1):
        questionOne()
        afficheMenu()
         
    if (rep == 2):
        questionTwo()
        afficheMenu()
         
    if (rep == 3):
        questionThree()
        afficheMenu()
         
    if (rep == 4):
        questionFour()
        afficheMenu()
         
    if (rep == 5):
        questionFive()
        afficheMenu()
         
    if (rep == 6):
        questionSix()
        afficheMenu()
         
    if (rep == 7):
        questionSeven()
        afficheMenu()
         
    if (rep == 8):
        questionEight()
        afficheMenu()
         
    if (rep == 9):
        questionNine()
        afficheMenu()
         
    if (rep == 10):
        questionTen()
        afficheMenu()
         
    if (rep == 11):
        questionEleven()
        afficheMenu()
        
    if (rep == 0):
        deconnexionBD()
        sys.exit(0)

###############################################################################
########################### FIN DU PROGRAMME ##################################
###############################################################################    