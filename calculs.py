import pandas as pd
from sigfig import round

Instruments = {'6,5' : {'Tension':{'100m': ['100','0.0050', '0.0035'], "1": ["1", "0.0040", "0.0007"], 
"10": ["10", "0.0035", "0.0005"], "100": ["100", "0.0045", "0.0006"], "1000": ["1000", "0.0045", "0.0010"]},
'Résistance':{"100": ["100", "0.010", "0.004"], "1k": ["1", "0.010", "0.001"], "10k": ["10", "0.010", "0.001"],
"100k": ["100", "0.010", "0.001"], "1M": ["1", "0.010", "0.001"], "10M": ["10", "0.040", "0.001"],
"100M": ["100", "0.800", "0.010"]}, 'Courant':{"10m": ["10", "0.050", "0.020"], "100m": ["100", "0.050", "0.005"],
"1": ["1", "0.100", "0.010"], "3": ["3", "0.120", "0.020"]}}, "4,5": {"Tension": {"500m": ["0.01", "0.02", "400"],
"5": ["0.0001", "0.02", "400"], "50": ["0.001", "0.02", "400"], "500": ["0.01", "0.02", "400"],
"1000": ["0.1", "0.02", "400"]}, "Résistance": {"500": ["0.01", "0.1", "500"], "5k": ["0.0001", "0.1", "300"],
"50k": ["0.001", "0.1", "300"], "500k": ["0.01", "0.1", "300"], "5M": ["0.0001", "0.1", "300"], "50M": ["0.001", "0.3", "300"]},
"Courant": {"500u": ["0.01", "0.05", "500"], "5m": ["0.0001", "0.05", "400"], "50m": ["0.001", "0.05", "400"],
"500m": ["0.01", "0.05", "400"], "5": ["0.0001", "0.25", "500"], "10": ["0.001", "0.25", "500"]},
"Source": {"Tension": {"6": ["1", "0.1", "0.5"], "25": ["1", "0.05", "2"]}, "Courant": {"6": ["1", "0.2", "1"],
"25": ["1", "0.15", "0.4"]}}}}

def calculs(appareil, type, range, valeur):
    instrument = Instruments[appareil]
    type_mesure = instrument[type]
    range_mesure = type_mesure[range]
    incertitude = float(valeur) * (float(range_mesure[1])/100) + float(range_mesure[0]) * (float(range_mesure[2])/100)
    return incertitude


def calculs2excel(liste, name):
    #liste = [[appareil1, type1, range1, valeur1], [appareil2, type2, range2, valeur2]...]
    #Retourne excel nommé Output. Si le excel est déjà écrit, alors il fait tout simplement l'actualiser.
    res = []
    unit = {"Résistance": "\u03A9", "Tension": "V", "Courant": "A"}
    for calcul in liste:
        appareil = calcul[0]
        type = calcul[1]
        rangee = calcul[2]
        valeur = calcul[3]
        unite = unit.get(type)
        if rangee[-1] in ["u", "k", "M", "m"]:
            facteur_unit = rangee[-1]
            unite = f"{facteur_unit}{unite}"
        incertitude = round(calculs(appareil, type, rangee, valeur), sigfigs=2)
        res.append([valeur, f"±{incertitude}", unite, "", rangee, appareil])
    df = pd.DataFrame(res, columns=["valeur", "incertitude", "unité", "", "range", "appareil"])
    df.to_excel(f"{name}.xlsx")  # Peut ajouter titre personalisé
    return


def calculs2tk(liste):
    res = []
    unit = {"Résistance": "\u03A9", "Tension": "V", "Courant": "A"}
    for calcul in liste:
        appareil = calcul[0]
        type = calcul[1]
        rangee = calcul[2]
        valeur = calcul[3]
        unite = unit.get(type)
        if rangee[-1] in ["u", "k", "M", "m"]:
            facteur_unit = rangee[-1]
            unite = f"{facteur_unit}{unite}"
        incertitude = round(calculs(appareil, type, rangee, valeur),sigfigs=2)
        affiche = f"{valeur}±{incertitude} {unite}"
        res.append(affiche)
    return res

liste = [["6,5", "Tension", "100m", "88"]]
