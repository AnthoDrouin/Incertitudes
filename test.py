from calculs import calculs, calculs2tk
import pandas as pd
from sklearn import tree

sufixe = {'mv': 1 , 'v' : 2, 'o' : 3, 'ko' : 4, 'Mo' : 5, 'ua' : 6,  'ma' : 7, 'a' : 8, }

incertitudes_data = pd.read_excel('incertitudes.xlsx')
info_incertitude = incertitudes_data.drop(columns=['range'])
range_incertitude = incertitudes_data['range']
model = tree.DecisionTreeClassifier()
model.fit(info_incertitude.values,range_incertitude.values)

def calcul_intelligent(stri,appareil):
    nb = 0
    type = ''
    for i in stri:
        try:
            int(i)
        except Exception:
            if i == '.':
                pass
            else:
                nb += 1

    if stri[-1:] == 'a':
        type = 'Courant'
    elif stri[-1:] == 'o':
        type = 'Résistance'
    elif stri[-1:] == 'v':
        type = 'Tension'

    sufixes = stri[-nb:]
    sufixes_numero = sufixe[sufixes]
    valeure = float(stri[:-nb])
    a = model.predict([[sufixes_numero,valeure,float(appareil)]])
    if a == 'err_d':
        valeure = valeure/1000
        n_suffixe = sufixes_numero + 1
        a = model.predict([[n_suffixe,valeure,float(appareil)]])
    elif a == 'err_m':
        valeure = valeure*1000
        n_suffixe = sufixes_numero - 1
        a = model.predict([[n_suffixe,valeure,float(appareil)]])
    c = a[0]
    appareil = str(appareil)
    app_cal = appareil.replace('.',',')
    b = calculs2tk([[app_cal, type, c, valeure]])
    return (b[0], c)


print(calcul_intelligent('0.01a','6.5'))