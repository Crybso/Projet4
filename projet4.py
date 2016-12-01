

def encode_noms(noms):
    dico = {}
    for nom in noms:
        dico[nom] = {}
    return dico
    
def add_depense(depenses):
    msg = 'Ajouter une dépense avec le format "nom  catégorie montant": '

    Input = input(msg).split(" ")
    flag = False
    if len(Input) == 3 and Input[0] in depenses:
        try:
            float(Input[2])
        except:
            return depenses
        #Vérifie que le nombre de décimale(s) soit <=2
        if "." in Input[2]:
            if len(Input[2].split(".")[1]) <= 2:
                Input[2] = float(Input[2])
                flag = True
        else:
            flag = True
        Input[2] = float(Input[2])
    #Si l'input est vérifié:
    if flag:
        nom, cat, montant = Input
        if cat in depenses[nom]:
            depenses[nom].append(montant)
        else:
            depenses[nom] = [montant]
    return depenses
    