#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def encode_noms(noms):
    """
    Retourne un dictionnaire de dictionnaires vides
    avec une clef pour chaque nom de la liste noms.
    """
    dico = {}
    for nom in noms:
        dico[nom] = {}
    return dico

def add_depense(depenses):
    """
    Retourne le dictionnaire depenses mis à jour.
    """
    print('Ajouter une dépense avec le format "nom  catégorie montant": ')
    Input = get_Input(depenses)
    #si l'entrée de l'utilisateur est valide
    if Input:
        nom, cat, montant = Input
        #si la catégorie existe, ajout du montant à la fin de la liste
        if cat in depenses[nom]:
            depenses[nom][cat].append(montant)
        #sinon, création de la clef avec liste associée contenant la dépense
        else:
            depenses[nom][cat] = [montant]
    #si l'entrée n'est pas valide
    else:
        print("Encodage impossible, veuillez réessayer.")
    return depenses

def get_Input(depenses):
    """
    Retourne le tuple (nom, cat, montant)
    et None si l'input de l'utilisateur n'est pas correct.
    """
    flag = False
    Input = input().split(" ")
    if len(Input) == 3:
        nom, cat, montant = Input
        #Vérifie que le nom soit une clef du dictionnaire
        if nom in depenses:
            #Vérifie que le montant soit convertible en float
            if montant.replace(".","",1).isdigit():
                #Si il y a des démicales
                if "." in montant:
                    #Vérifie que leur nombres soit <= 2
                    if len(montant.split(".")[1]) <= 2:
                        flag = True
                        montant = float(montant)
                    else:
                        print("Veuillez limiter le nombre de décimales à deux.")
                #Sans décimales, pas d'erreur possible
                else:
                    flag = True
                    montant = int(montant)
            else: print("Impossible de convertir le montant en nombre.")
        else: print("Le nom entré n'est pas présent dans les comptes.")
    if flag:
        return nom, cat, montant
    return None
    
def display_depenses(depenses):
    """
    Affiche le dictionnaire depenses
    """
    for name in depenses:
        #si le dictionnaire de la personne contient des dépenses
        if len(depenses[name]) > 0:
            #affiche le nom de la personne
            print("\n{} a dépensé :".format(name))
        for cat in depenses[name]:
            #affiche la catégorie suivie des montants associés
            print("-", cat, end=" : ")
            montant = depenses[name][cat]
            print(str(montant).strip("[]"))
    return
    
def compute_depenses_personne(depenses):
    """
    Retourne un dictionnaire ayant comme clefs les noms des personnes
    et comme valeur le montant total dépensé par les différentes personnes
    """
    totPers = {}
    for name in depenses:
        #initialise la somme pour la personne
        somme = 0
        for cat in depenses[name]:
            for montant in depenses[name][cat]:
                somme += montant
        #ajoute la clef et la la somme pour la personne
        totPers[name] = somme
    return totPers

def compute_depenses_cat(depenses):
    """
    Retourne un dictionnaire ayant comme clefs les catégories actuelles
    et comme valeur le montant total dépensé dans les différentes catégories
    """
    totCat = {}
    somme = 0
    for name in depenses:
        for cat in depenses[name]:
            if cat not in totCat:
                #création clef avec valeur 0 si la catégorie est nouvelle
                totCat[cat] = 0
            for montant in depenses[name][cat]:
                #incrém. valeur de cat par le montant dépense par la personne
                totCat[cat] += montant
    return totCat

def display_depenses_personne_cat(depensesTot):
    """
    Affiche le dictionnaire depensesTot qui est le résultat de
    compute_depenses_cat ou compute_depenses_personne
    """
    for key, value in depensesTot.items():
        print(key,":",value)
    return

def compute_comptes(depenses):
    """
    Effectue les comptes.
    Retourne un dictionnaire avec une clef pour chaque personne redevable
    Et comme valeur un dictionnaire avec le montant dû à chaque personne.
    """
    comptes = {}
    total = 0
    nb_personnes = len(depenses)
    #dictionnaire contenant les dépenses de chaque personne
    comptes_personne = compute_depenses_personne(depenses)
    for value in comptes_personne.values():
        total += value
    for name in depenses:
        #ce dictionnaire a comme valeur pour chaque personne son compte, càd
        #la soustraction de la part totale à payer moins le montant déjà payé
        compte = round(total/nb_personnes-comptes_personne[name],2)
        comptes_personne[name] = compte
    #on cherche une personne devant de l'argent (debiteur)
    for debiteur in depenses:
        debit = comptes_personne[debiteur]
        if debit > 0:
            #on créé une clef et un dictionnaire pour cette personne
            comptes[debiteur] = {}
            for crediteur in depenses:
                credit = comptes_personne[crediteur]
                if credit < 0:
                    #on ajoute une clef pour le crediteur
                    comptes[debiteur][crediteur] = 0
                    #si le montant redevable est supérieur au montant 
                    #dû au créditeur
                    if debit + credit > 0:
                        #le debiteur rembourse alors le montant dû au créditeur
                        comptes[debiteur][crediteur] += -credit
                        comptes_personne[debiteur] -= -credit
                        comptes_personne[crediteur] += -credit
                    else:
                        #sinon le debiteur rembourse le montant qu'il doit
                        comptes[debiteur][crediteur] += debit
                        comptes_personne[debiteur] -= debit
                        comptes_personne[crediteur] += debit
    return comptes

def display_comptes(comptes):
    """
    Affiche le dictionnaire comptes de la fonction compute_comptes
    """
    for name in comptes:
        print(name,"doit a :")
        for subname in comptes[name]:
            print("- {} : {}".format(subname,comptes[name][subname]))
    return

def compta(noms):
    """
    Initialise le dictionnaire principal depenses avec la liste noms
    et la boucle principale qui attend le choix de l'utilisateur.
    """
    #si la liste noms n'existe pas
    if not noms:
        print("Erreur d'encodage des noms")
        return
    #si elle existe, initiation du dictionnaire depenses
    else:
        depenses = encode_noms(noms)
    flag = False
    #boucle principale, effectue le choix de l'utilisateur.
    while not flag:
        display_menu()
        choix = get_choice()
        if choix == 1:
            depenses = add_depense(depenses)
        elif choix == 2:
            display_depenses(depenses)
        elif choix == 3:
            display_depenses_personne_cat(compute_depenses_personne(depenses))
        elif choix == 4:
            display_depenses_personne_cat(compute_depenses_cat(depenses))
        elif choix == 5:
            display_comptes(compute_comptes(depenses))
        elif choix == 6:
            flag = True
        else:
            print("Choix non reconnu, veuillez réessayer.")
    print("Au-revoir!")
    return

def get_choice():
    """
    Retourne le chiffre entre 1 et 6 choisi par l'utilisateur sinon -1
    """
    choice = input()
    if len(choice) == 1 and choice in "123456":
        return int(choice)
    return -1

def display_menu():
    """
    Affiche le menu principal.
    """
    print("\nQue voulez-vous faire ?")
    print("1: Ajouter une dépense\n2: Voir les dépenses")
    print("3: Voir les dépenses par personne")
    print("4: Voir les dépenses par catégorie")
    print("5: Faire les comptes\n6: Sortir de l'application\n")
    return

if __name__ == "__main__":
    #création de la liste noms
    noms = []
    for arg in sys.argv[1:]:
        noms.append(arg)
    #initialisation du programme avec cette liste
    compta(noms)
