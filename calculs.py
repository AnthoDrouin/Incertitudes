
Instruments = {'6,5' : {'Tension':{'100m':['100','0.0050', '0.0035']}, 'Résistance':{}, 'Courant':{}}}

def calculs(appareil, type, range, valeur):
    instrument = Instruments[appareil]
    type_mesure = instrument[type]
    range_mesure = type_mesure[range]
    incertitude = float(valeur) * (float(range_mesure[1])/100) + float(range_mesure[0]) * (float(range_mesure[2])/100)
    return incertitude 


# Ceci est un test
