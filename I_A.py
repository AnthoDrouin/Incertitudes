
import pandas as pd
from sklearn import tree

incertitudes_data = pd.read_excel('incertitudes.xlsx')
print(incertitudes_data)
info_incertitude = incertitudes_data.drop(columns=['range'])
range_incertitude = incertitudes_data['range']

model = tree.DecisionTreeClassifier()
model.fit(info_incertitude.values,range_incertitude.values)
prediction = model.predict([[1,1]])
print(prediction)
