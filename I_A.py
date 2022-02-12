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
    for i in stri[::-1]:
        try:
            int(i)
            break
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

    if stri[0] == '-':
        stri = stri[1:]

    sufixes = stri[-nb:]
    sufixes_numero = sufixe[sufixes]
    valeure = float(stri[:-nb])
    a = model.predict([[sufixes_numero,valeure,float(appareil)]])

    if a[0] == 'err_d':
        valeure = valeure/1000
        n_suffixe = sufixes_numero + 1
        b = model.predict([[n_suffixe,valeure,float(appareil)]])
    elif a[0] == 'err_m':
        valeure = valeure*1000
        n_suffixe = sufixes_numero - 1
        print([[n_suffixe,valeure,float(appareil)]])
        b = model.predict([[n_suffixe,valeure,float(appareil)]])
        print(b)
    else:
        b = a

    c = b[0]
    appareil = str(appareil)
    app_cal = appareil.replace('.',',')
    d = calculs2tk([[app_cal, type, c, valeure]])
    return (d[0], c)



def excel2excel(path, name, unite, appareil):
    données = pd.read_excel(path)
    valeurs = données['value']
    unité = [unite for _ in range(len(valeurs))]
    combi = tuple(zip(valeurs, unité))
    stris = []
    for tup in combi:
        stris.append(str(tup[0]) + str(tup[1]))
    res = []
    for stri in stris:
        stri = str(float(stri[:-len(unite)])) + stri[-len(unite):]
        incertitude = calcul_intelligent(stri, appareil)
        num = stri[:-len(unite)]
        res.append([num, f"{incertitude}", unite, "", appareil])
    
    df = pd.DataFrame(res, columns=["valeurs", "incertitude", "unité", "", "appareil"])
    df.to_excel(f"{name}_output.xlsx")


#print(excel2excel('/Users/laurentemond/Desktop/Classeur2.xlsx', 'se', 'a', '6.5'))