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
            depenses[nom].append(montant)
        else:
            depenses[nom] = [montant]
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
