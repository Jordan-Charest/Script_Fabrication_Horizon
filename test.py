import numpy as np
import pandas as pd

def return_dataframe(nom_competence):

    df = pd.read_csv(f'{nom_competence}.csv', encoding="UTF-8-sig", delimiter=",")

    return df

def format_prereq(prereq_str):

    liste_prereq = prereq_str.split(sep="+")

    return liste_prereq

def return_item_data(df, nom_item):

    item_index = df.index[df["Nom"]==nom_item].tolist()[0]

    temps_item = df["Temps"][item_index]
    cout_item = df["Cout"][item_index]
    prereq_item = df["Pré-Requis"][item_index]

    return (temps_item, cout_item, prereq_item)

competence = input("Entrez la compétence de fabrication:")
df = return_dataframe(competence)

item = input("Entrer le nom de l'item:")
(temps, cout, prereq) = return_item_data(df, item)

print(f"Le nom est {item}, le temps est {temps}, et le cout est {cout}.\n")
if prereq == "-":
    print(f"Il n'y a aucun Pré-Requis pour l'item.")
else:
    print(f"La liste de pré-requis est:\n {format_prereq(prereq)}")
    cout_tot = input("Souhaitez-vous connaître le coût total incluant les pré-requis? (O/N)")

    if cout_tot == "O" or "o":
        print("WIP")