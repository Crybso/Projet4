print("----------------------------------------------------------")
print("Les messages d'erreur des tests commencent par 'ERROR TEST:'")
print("----------------------------------------------------------")

try :
    import projet4
    
except :
    print("Erreur import projet 4")
    
try :

    file = open("projet4.py", 'r')
    content = file.read()
    
    if "__name__" not in content or "__main__" not in content:
        print("ERROR TEST: if __name__ == \"__main__\" ")
        
    res = projet4.encode_noms(["Pierre","Paul"])
    if len(res) !=2 or "Pierre" not in res.keys() or not isinstance(res["Pierre"],dict) or not len(res["Pierre"])==0 or "Paul" not in res.keys() or not isinstance(res["Paul"],dict) or not len(res["Paul"])==0:
        print("ERROR TEST: encode_noms")
            
    res = {"Pierre":{"hotel" : [10,12], "repas" : [23]},"Paul":{"trajet" : [30], "repas" : [12,15]}}
    
    totPers = projet4.compute_depenses_personne(res)
    if len(totPers) != 2 or "Pierre" not in totPers.keys() or totPers["Pierre"] != 45 or "Paul" not in totPers.keys() or totPers["Paul"] != 57 :
        print("ERROR TEST: compute_depenses_personne")
    
    totCat = projet4.compute_depenses_cat(res)
    if len(totCat) != 3 or "hotel" not in totCat.keys() or totCat["hotel"] != 22 or  "repas" not in totCat.keys() or totCat["repas"] != 50 or  "trajet" not in totCat.keys() or totCat["trajet"] != 30 :
        print("ERROR TEST: compute_depenses_cat")
        
    res = projet4.add_depense(res)
    if not 8.50 in res["Pierre"]["hotel"]:
        print("ERROR TEST: add_depense 1")
    
    res = projet4.add_depense(res)
    if len(res)>2:
        print("ERROR TEST: add_depense 2")
    
    res = projet4.add_depense(res)
    if len(res["Pierre"]["repas"])>1:
        print("ERROR TEST: add_depense 3")

    res = projet4.add_depense(res)
    if "inconnu" in res["Pierre"]:
        print("ERROR TEST: add_depense 4")
    
    res = projet4.add_depense(res)
    if "inconnu" not in res["Pierre"] or res["Pierre"]["inconnu"] != [2]:
        print("ERROR TEST: add_depense 5")
            
    res = projet4.compute_comptes(res)
    if "Pierre" not in res or "Paul" not in res["Pierre"] or res["Pierre"]["Paul"] > 0.77 or res["Pierre"]["Paul"] < 0.73 : 
        print("ERROR TEST: compute_comptes")

except:
    print("Exception lors des test")
