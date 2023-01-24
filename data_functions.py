import pandas as pd

def return_dataframe(nom_competence):

    df = pd.read_csv(f'./Data/{nom_competence}.csv', encoding="UTF-8-sig", delimiter=";")

    return df

def format_ressources(prereq_str):

    liste_prereq = prereq_str.split(sep="+")

    return liste_prereq

def return_item_data(df, nom_item):

    item_index = df.index[df["Nom"]==nom_item].tolist()[0]

    temps_item = df["Temps (minutes)"][item_index]
    cout_item = df["Fabrication : Crédits"][item_index]
    prereq_item = df["Pré-Requis"][item_index]
    ressources_item = df["Fabrication : Ressources"][item_index]

    return (temps_item, cout_item, prereq_item, format_ressources(ressources_item))