# Importando los módulos necesarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import f1_score

# Abriendo el archivo csv
humandata = pd.read_csv('C:\\Temp\\juego_azar.csv', sep=';')
# Obteniendo la cantidad de la data
humandatalength = len(humandata)
# Lista con la data generada por el script
randomdata = []

# Generando combinaciones aleatorias
for i in range(len(humandata)):
    randomdata.append(sorted(np.random.choice(50, 5, replace=False) + 1))
randomdata = np.array(randomdata)
randomdata = pd.DataFrame(randomdata,
                          index = [i + humandatalength for i in range(humandatalength)],
                          columns = ['N1', 'N2', 'N3', 'N4', 'N5'])

# Mostrando la cantidad de combinaciones humanas y aleatorias
print ('Cantidad de combinaciones humanas: %s' % (len(humandata))) # Humanas
print('Cantidad de combinaciones aleatorias: %s' % (len(randomdata))) # Aleatorias

# Mostrando las combinaciones más comunes en los humanos
humangroup = humandata.groupby(['N1', 'N2', 'N3', 'N4', 'N5'])
groupsize = humangroup.size()
groupsize.sort_values(ascending=False)
print(groupsize)

# El primer número más común usado por los humanos
print('El primer número más común usado por los humanos: ')
randomgroup = randomdata.groupby(['N1'])
randomgroupsize = randomgroup.size()
randomgroupsize.sort_values(ascending=False)
print(randomgroupsize)

# Número más usado en cada columna
columns = ['N1', 'N2', 'N3', 'N4', 'N5']
freq = []
for col in columns:
    freq.append(humandata[col].value_counts().argmax())

# Mostrando el número más usado en cada columna
x_pos = [i for i, _ in enumerate(columns)]
plt.title('Número más utilizado en una columna')  
plt.xlabel('Columna')  
plt.ylabel('Número') 
plt.bar(x_pos,freq,color="blue")
plt.xticks(x_pos,columns)
plt.show()

# Obteniendo la data para entrenar y probar
from sklearn.model_selection import train_test_split
humandata = humandata.drop(columns=['DRAW_ID']) # Obviando la columna de DRAW_ID
X = pd.concat([humandata,randomdata]) # Valor de entrada
humandata['H/G'] = 0
randomdata['H/G'] = 1
Y = pd.concat([humandata,randomdata])  # Valor a predecir

# Realizando el split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Creando modelo de predicción
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

pred_data = knn.predict(x_test)

# Formateando la data predecida como DataFrame
pred_data = pd.DataFrame(pred_data, 
                        index = [i for i in range(len(pred_data))], 
                        columns = ['N1', 'N2', 'N3', 'N4', 'N5','H/G'])

print('Resultado de la predicción', pred_data, sep='\n')
print('') # Salto de línea adicional

# Obteniendo el F1 Score utilizando la utilidad multietiqueta y formatear los datos
# de forma que F1 Score pueda arrojarnos el resultado
mlb = MultiLabelBinarizer().fit(y_test)
score = f1_score(mlb.transform(y_test),mlb.transform(pred_data),average='weighted')

print('El f1_score es: %s' %(score))