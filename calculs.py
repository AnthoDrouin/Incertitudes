
Instruments = {'6,5' : {'Tension':{'100m': ['100','0.0050', '0.0035'], "1": ["1, 0.0040, 0.0007"], 
"10": ["10", "0.0035", "0.0005"], "100": ["100", "0.0045", "0.0006"], "1000": ["1000", "0.0045", "0.0010"]},
'Résistance':{"100": ["100", "0.010", "0.004"], "1k": ["1", "0.010", "0.001"], "10k": ["10", "0.010", "0.001"],
"100k": ["100", "0.010", "0.001"], "1M": ["1", "0.010", "0.001"], "10M": ["10", "0.040", "0.001"],
"100M": ["100", "0.800", "0.010"]}, 'Courant':{"10m": ["10", "0.050", "0.020"], "100m": ["100", "0.050", "0.005"],
"1": ["1", "0.100", "0.010"], "3": ["3", "0.120", "0.020"]}}, "4,5": {"Tension": {"500m": ["0.01", "0.02", "400"]}}}

def calculs(appareil, type, range, valeur):
    instrument = Instruments[appareil]
    type_mesure = instrument[type]
    range_mesure = type_mesure[range]
    incertitude = float(valeur) * (float(range_mesure[1])/100) + float(range_mesure[0]) * (float(range_mesure[2])/100)
    return incertitude

