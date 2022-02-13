from calculs import calculs, calculs2tk
import pandas as pd
from sklearn import tree

sufixe = {'mv': 1 , 'v' : 2, 'o' : 3, 'ko' : 4, 'Mo' : 5, 'ua' : 6,  'ma' : 7, 'a' : 8, }

incertitudes_data = pd.read_excel('incertitudes.xlsx')
info_incertitude = incertitudes_data.drop(columns=['range'])
range_incertitude = incertitudes_data['range']
model = tree.DecisionTreeClassifier()
model.fit(info_incertitude.values,range_incertitude.values)

ajustement_data = pd.read_excel('ajustement.xlsx')
ajustement_incertitude = ajustement_data.drop(columns=['range'])
ajustement_range_incertitude = ajustement_data['range']
model2 = tree.DecisionTreeClassifier()
model2.fit(ajustement_incertitude.values,ajustement_range_incertitude.values)

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
    a = model2.predict([[float(appareil),sufixes_numero,valeure]])
    

    if a[0] == 'err_d':
        valeure = valeure/1000
        n_suffixe = sufixes_numero + 1
        b = model.predict([[float(appareil),n_suffixe,valeure]])
    elif a[0] == 'err_m':
        valeure = valeure*1000
        n_suffixe = sufixes_numero - 1
        
        b = model.predict([[float(appareil),n_suffixe,valeure]])
        
    else:
        b = model.predict([[float(appareil),sufixes_numero,valeure]])

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
        affichage = str(calcul_intelligent(stri, appareil))
        indice1 = affichage.index("±")
        indice2 = affichage.index(" ")
        print(indice1, indice2)
        incertitude = affichage[indice1 + 1: indice2]
        num = affichage[2: indice1]
        unite_range = affichage[indice2 + 1:]
        unite_range = unite_range[:-2]
        res.append([num, incertitude, unite_range, "", appareil])

    a = 0
    for i, j in enumerate(path):
        if j == "/":
            a = i

    final_path = path[:(a + 1)]
    print(final_path)

    df = pd.DataFrame(res, columns=["valeurs", "incertitude", "unité/range", "", "appareil"])
    df.to_excel(final_path + f"{name}_output.xlsx")


#print(excel2excel('/Users/laurentemond/Desktop/Classeur2.xlsx', 'se', 'a', '6.5'))