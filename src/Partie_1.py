# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:46:17 2020

@author: Julie

Projet SQL :
    - Crétaion de la base de données
    - Création des tables DEPARTEMENTS et REGIONS
    - Ajout des données issues des fichiers csv aux tables
    - Lecture des données d'un fichier xls
    + Ajout des tables SOCIALREG, SOCIALDEP et ENVIRONNEMENTDEP
    + Conversion xls -> csv 
    + Ajout des données dans les nouvelles tables
    
"""

import sqlite3, csv
import pandas as pd 
from sqlalchemy import create_engine


# Connection à la base de données
connexion = sqlite3.connect("base.db")

# Création d'un curseur pour faire les requêtes
cursor = connexion.cursor()


# Crations des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS DEPARTEMENT(
        DEPARTEMENTS TEXT PRIMARY KEY,
        REGIONS INTEGER,
        cheflieu TEXT,
        tncc INTEGER,
        ncc TEXT,
        nccenr TEXT,
        libelle TEXT
        ) 
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS REGION(
        REGIONS INTERGER PRIMARY KEY,
        cheflieu TEXT,
        tncc INTEGER,
        ncc TEXT,
        nccenr TEXT,
        libelle TEXT
        )
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS SOCIALREG(
       Indicateurs_Dimension_sociale_Régions TEXT PRIMARY KEY,
       REGIONS TEXT,
       Taux_de_pauvreté_2014 INTEGER,
       Part_des_jeunes_non_insérés_2014 INTEGER,
       Part_des_jeunes_non_insérés_2009 INTEGER,
       Poids_de_l_économie_sociale_dans_les_emplois_salariés_du_territoire_2015 INTEGER
       )
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS SOCIALDEP(
       Indicateurs_Dimension_sociale_Départements TEXT PRIMARY KEY,
       DEPARTEMENTS TEXT,
       Espérance_de_vie_des_hommes_à_la_naissance_2015 INTEGER,
       Espérance_de_vie_des_hommes_à_la_naissance_2010 INTEGER,
       Espérance_de_vie_des_femmes_à_la_naissance_2015 INTEGER,
       Espérance_de_vie_des_femmes_à_la_naissance_2010 INTEGER,
       Part_de_la_population_éloignée_de_plus_de_7_mn_des_services_de_santé_de_proximité_2016 INTEGER,
       Part_de_la_population_estimée_en_zone_inondable_2013 INTEGER,
       Part_de_la_population_estimée_en_zone_inondable_2008 INTEGER
       )               
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ENVIRONNEMENTDEP(
       Indicateurs_Dimension_environnementale_Départements TEXT PRIMARY KEY,
       DEPARTEMENTS TEXT,
       Taux_de_valorisation_matière_et_organique_2013 INTEGER,
       Taux_de_valorisation_matière_et_organique_2009 INTEGER,
       Part_de_surfaces_artificialisées_2012 INTEGER,
       Part_de_surfaces_artificialisées_2006 INTEGER,
       Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016 INTEGER,
       Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2010 INTEGER,
       Production_de_granulats_2014 INTEGER,
       Production_de_granulats_2009 INTEGER,
       Eolien_2015 INTEGER,
       Eolien_2010 INTEGER,
       Photovoltaïque_2015 INTEGER,
       Photovoltaïque_2010 INTEGER,
       Autre_2015 INTEGER,
       Autre_2010 INTEGER
       )               
""")

# Ajout des données dans les tables précédemment créées
with open('departement2020.csv','r') as fin:
    # csv.DictReader utilise la première ligne du fichier pour les en-têtes de colonne par défaut
    dr = csv.DictReader(fin) # la virgule est le délimiteur par défaut
    to_db_1 = [(i['DEPARTEMENTS'], i['REGIONS'], i['cheflieu'], i['tncc'], i['ncc'], i['nccenr'], i['libelle']) for i in dr]


cursor.executemany("INSERT INTO DEPARTEMENT (DEPARTEMENTS, REGIONS, cheflieu, tncc, ncc, nccenr, libelle) VALUES (?,?,?,?,?,?,?); ", to_db_1)

with open('region2020.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db_2 = [(i['REGIONS'], i['cheflieu'], i['tncc'], i['ncc'], i['nccenr'], i['libelle']) for i in dr]

cursor.executemany("INSERT INTO REGION (REGIONS, cheflieu, tncc, ncc, nccenr, libelle) VALUES (?,?,?,?,?,?); ", to_db_2)


with open('SocialReg.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db_3 = [(i['Indicateurs_Dimension_sociale_Régions'], i['REGIONS'], i['Taux_de_pauvreté_2014'], i['Part_des_jeunes_non_insérés_2014'], i['Part_des_jeunes_non_insérés_2009'], i['Poids_de_l_économie_sociale_dans_les_emplois_salariés_du_territoire_2015']) for i in dr]

cursor.executemany("INSERT INTO SOCIALREG (Indicateurs_Dimension_sociale_Régions, REGIONS, Taux_de_pauvreté_2014, Part_des_jeunes_non_insérés_2014, Part_des_jeunes_non_insérés_2009, Poids_de_l_économie_sociale_dans_les_emplois_salariés_du_territoire_2015) VALUES (?,?,?,?,?,?); ", to_db_3)


with open('SocialDep.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db_4 = [(i['Indicateurs_Dimension_sociale_Départements'], i['DEPARTEMENTS'], i['Espérance_de_vie_des_hommes_à_la_naissance_2015'], i['Espérance_de_vie_des_hommes_à_la_naissance_2010'], i['Espérance_de_vie_des_femmes_à_la_naissance_2015'], i['Espérance_de_vie_des_femmes_à_la_naissance_2010'], i['Part_de_la_population_éloignée_de_plus_de_7_mn_des_services_de_santé_de_proximité_2016'], i['Part_de_la_population_estimée_en_zone_inondable_2013'], i['Part_de_la_population_estimée_en_zone_inondable_2008']) for i in dr]

cursor.executemany("INSERT INTO SOCIALDEP (Indicateurs_Dimension_sociale_Départements, DEPARTEMENTS, Espérance_de_vie_des_hommes_à_la_naissance_2015, Espérance_de_vie_des_hommes_à_la_naissance_2010, Espérance_de_vie_des_femmes_à_la_naissance_2015, Espérance_de_vie_des_femmes_à_la_naissance_2010, Part_de_la_population_éloignée_de_plus_de_7_mn_des_services_de_santé_de_proximité_2016, Part_de_la_population_estimée_en_zone_inondable_2013, Part_de_la_population_estimée_en_zone_inondable_2008) VALUES (?,?,?,?,?,?,?,?,?); ", to_db_4)


with open('EnvironnementDep.csv','r') as fin: 
    dr = csv.DictReader(fin)
    to_db_5 = [(i['Indicateurs_Dimension_environnementale_Départements'], i['DEPARTEMENTS'], i['Taux_de_valorisation_matière_et_organique_2013'], i['Taux_de_valorisation_matière_et_organique_2009'], i['Part_de_surfaces_artificialisées_2012'], i['Part_de_surfaces_artificialisées_2006'], i['Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016'], i['Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2010'], i['Production_de_granulats_2014'], i['Production_de_granulats_2009'], i['Eolien_2015'], i['Eolien_2010'], i['Photovoltaïque_2015'], i['Photovoltaïque_2010'], i['Autre_2015'], i['Autre_2010']) for i in dr]

cursor.executemany("INSERT INTO ENVIRONNEMENTDEP (Indicateurs_Dimension_environnementale_Départements, DEPARTEMENTS, Taux_de_valorisation_matière_et_organique_2013, Taux_de_valorisation_matière_et_organique_2009, Part_de_surfaces_artificialisées_2012, Part_de_surfaces_artificialisées_2006, Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2016, Part_de_l_agriculture_biologique_dans_la_surface_agricole_totale_2010, Production_de_granulats_2014, Production_de_granulats_2009, Eolien_2015, Eolien_2010, Photovoltaïque_2015, Photovoltaïque_2010, Autre_2015, Autre_2010) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); ", to_db_5)


# Lecture fichier xls
file_S = 'DD-indic-reg-dep_janv2018.xls'

engine = create_engine('sqlite://', echo = False)
df_S = pd.read_excel(file_S, sheet_name = 'Social')

print("Social", df_S)

file_E = 'DD-indic-reg-dep_janv2018.xls'

engine = create_engine('sqlite://', echo = False)
df_E = pd.read_excel(file_E, sheet_name = 'Environnement')

print("Environnement", df_E)

connexion.commit()


# Déconection de la base de données
connexion.close()