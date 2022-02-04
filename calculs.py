
Instruments = {'6,5' : {'Tension':{'100m': ['100','0.0050', '0.0035'], "1": ["1, 0.0040, 0.0007"], 
"10": ["10", "0.0035", "0.0005"], "100": ["100", "0.0045", "0.0006"], "1000": ["1000", "0.0045", "0.0010"]},
'Résistance':{}, 'Courant':{}}}

def calculs(appareil, type, range, valeur):
    instrument = Instruments[appareil]
    type_mesure = instrument[type]
    range_mesure = type_mesure[range]
    incertitude = float(valeur) * (float(range_mesure[1])/100) + float(range_mesure[0]) * (float(range_mesure[2])/100)
    return incertitude 


