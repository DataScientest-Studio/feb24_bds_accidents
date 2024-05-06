import pandas as pd

def chargement_train_test_data():
    # Séparation ensemble train/test
    train_csv_path = "../data/train_data15variables_stratified.csv"
    test_csv_path = "../data/test_data15variables_stratified.csv"

    train_data = pd.read_csv(train_csv_path)
    test_data = pd.read_csv(test_csv_path)

    # Séparer les caractéristiques (X) et les étiquettes (y) pour les ensembles d'entraînement et de test
    X_train = train_data.drop(columns=['grav'])  
    y_train = train_data['grav']
    X_test = test_data.drop(columns=['grav'])
    y_test = test_data['grav']

    return X_train, y_train , X_test, y_test

def chargement_df() :
    # Assemblage du df_modelling dont la taille dépassait les 100mo autorisés github
    df1 = pd.read_csv("../data/df_modelling_1.csv")
    df2 = pd.read_csv("../data/df_modelling_2.csv")

    # Concaténation des deux dataframes
    df = pd.concat([df1, df2], ignore_index=True)

    return df