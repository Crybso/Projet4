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
    Retourne une liste contenant [nom, catégorie, montant]
    et None si l'input de l'utilisateur n'est pas correct.
    """
    Input = input().split(" ")
    flag = False
    if len(Input) == 3 and Input[0] in depenses:
        #Vérifie que le montant soit convertible en float
        try:
            float(Input[2])
        except:
            pass
        #Montant convertible en float
        else:
            #Décimales?
            if "." in Input[2]:
                #Vérifie que le nombre de décimales soit <= 2
                if len(Input[2].split(".")[1]) <= 2:
                    flag = True
            #Pas de décimales
            else: flag = True
            #Converti le montant en float
            Input[2] = float(Input[2])
        finally:
            if flag:
                return Input
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