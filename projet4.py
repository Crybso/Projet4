#!/usr/bin/env python
# -*- coding: utf-8 -*-

depenses = {'Cedric': {'trajet' : [125], 'repas': [43,52]},
'Fabio': {'repas': [46,57],'trajet' : [21]}, 'Francois': {'hotel': [140]}}

def encode_noms(noms):
    """
    Retourne un dictionnaire de dictionnaires vides
    avec une clef par personne.
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
    Input = getInput(depenses)
    if Input:
        nom, cat, montant = Input
        if cat in depenses[nom]:
            depenses[nom][cat].append(montant)
        else:
            depenses[nom][cat] = [montant]
    return depenses
    
    
def getInput(depenses):
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
                #Sans décimale, pas d'erreur possible
                else:
                    flag = True
                    montant = int(montant)
    if flag:
        return nom, cat, montant
    return None
    
def display_depenses(depenses):
    """
    Affiche le dictionnaire depenses
    """
    for name in depenses:
        print("\n{} a dépensé :".format(name))
        for cat in depenses[name]:
            print("-", cat, end=" : ")
            montant = depenses[name][cat]
            print(str(montant).strip("[]"))
    return
    
def compute_depenses_personne(depenses):
    """
    Retourne un dictionnaire ayant comme clefs les noms des personnes
    et comme valeur le montant total dépensé par les différentes personnes
    """
    dico = {}
    for name in depenses:
        somme = 0
        for cat in depenses[name]:
            for montant in depenses[name][cat]:
                somme += montant
        dico[name] = somme
    return dico
    
def compute_depenses_cat(depenses):
    """
    Retourne un dictionnaire ayant clefs les catégories actuelles
    et comme valeur le montant total dépensé dans les différentes catégories
    """
    dico = {}
    somme = 0
    for name in depenses:
        for cat in depenses[name]:
            if cat not in dico:
                dico[cat] = 0
            for montant in depenses[name][cat]:
                dico[cat] += montant
    return dico
    
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
    Et comme valeur un dictionnaire avec le montant du à chaque personne.
    """
    comptes = {}
    total = 0
    nb_personnes = len(depenses)
    comptes_personne = compute_depenses_personne(depenses)
    for value in comptes_personne.values():
        total += value
    for name in depenses:
        #le dictionnaire comptes_personne contient contient pour chaque personne
        #le montant du ou l'avoir (respectivement positif et négatif)
        comptes_personne[name] = total/nb_personnes - comptes_personne[name]
    #on cherche une personne devant de l'argent (debiteur)
    for debiteur in depenses:
        debit = comptes_personne[debiteur]
        if debit > 0:
            #on créé une clef et un dictionnaire pour cette personne
            comptes[debiteur] = {}
            for crediteur in depenses:
                credit = comptes_personne[crediteur]
                if comptes_personne[crediteur] < 0:
                    #on ajoute une clef pour le crediteur
                    comptes[debiteur][crediteur] = 0
                    #si le montant redevable est supérieur au montant du au créditeur
                    if debit + credit > 0:#précision?
                        #le debiteur rembourse alors le montant redevaable
                        comptes[debiteur][crediteur] += round(credit, 2)
                        comptes_personne[debiteur] -= round(credit, 2)
                    else:
                        #sinon le debiteur rembourse le montant qu'il doit
                        comptes[debiteur][crediteur] += round(debit, 2)
                        comptes_personne[debiteur] -= round(debit, 2)
    return comptes
