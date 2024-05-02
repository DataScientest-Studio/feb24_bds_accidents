import pandas as pd


train_csv_path = "../data/train_data15variables_stratified.csv"
test_csv_path = "../data/test_data15variables_stratified.csv"

train_data = pd.read_csv(train_csv_path)
test_data = pd.read_csv(test_csv_path)

# Séparer les caractéristiques (X) et les étiquettes (y) pour les ensembles d'entraînement et de test
X_train = train_data.drop(columns=['grav'])  
y_train = train_data['grav']
X_test = test_data.drop(columns=['grav'])
y_test = test_data['grav']
