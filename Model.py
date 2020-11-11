# ================================
# Regressão logística multivariada
# ================================

# Importar módulos de análise.
import numpy as np
import pandas as pd

# Usar pandas para ler os arquivos do excel. Remover Colunas EV e PL por correlação alta.
empresas = pd.read_excel("Dados.xlsx")
empresas.drop(["Patrimônio líquido","Enterprise Value"], axis=1, inplace=True)
#print(empresas.tail())

# Separar dados em X (features, input) e Y (label, output ou previsão)
X = empresas[["Margem líquida", "Cresc EBITDA", "Receita líquida", "Funcionários", "Market Share", "Dív. Líq. EBITDA", "Liquidez"]]
y = empresas[["MEA"]]

# Separar dados em treino e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)

#Criar e treinar modelo
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

#Testar modelo
from sklearn.metrics import classification_report
print(classification_report(y_test, logmodel.predict(X_test)))

# true pos/amostra de positivos
# true pos/amostra total
