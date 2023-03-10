import pandas as pd

def return_dataframe(nom_competence):

    df = pd.read_csv(f'./Data/{nom_competence}.csv', encoding="UTF-8-sig", delimiter=";")

    return df

def format_ressources(prereq_str):

    liste_prereq = prereq_str.split(sep="+")

    return liste_prereq

def apply_gestion(temps, cout, gestion):

    temps = int(temps)
    cout = int(cout)
    
    gestion_dict = {1:(0,0), 2:(10, 25), 3:(20, 50), 4:(30,100)}

    if gestion[0] is False:
        return temps, cout

    elif gestion[1]:
        temps -= gestion_dict[gestion[1]][0]
        cout -= gestion_dict[gestion[1]][1]

    if temps < 5:
        temps = 5
    if cout < 10:
        cout = 10

    return temps, cout

def return_item_data(df, nom_item, gestion):

    item_index = df.index[df["Nom"]==nom_item].tolist()[0]

    temps_item = df["Temps (minutes)"][item_index]
    cout_item = df["Fabrication : Crédits"][item_index]
    if cout_item == "-" or "" or None:
        cout_item = df["Prix du marché"][item_index]

    prereq_item = df["Pré-Requis"][item_index]
    ressources_item = df["Fabrication : Ressources"][item_index]

    temps_item, cout_item = apply_gestion(temps_item, cout_item, gestion)

    return (temps_item, cout_item, prereq_item, format_ressources(ressources_item))

def return_ressources(df, nom_item, liste_ressources_input):

    # print(f"itération de return_ressources démarrée. Item: {nom_item}")

    liste_ressources_this_iter = [] # Variable temporaire pour cette itération

    try:
        item_index = df.index[df["Nom"]==nom_item].tolist()[0]
        ressources_item = df["Fabrication : Ressources"][item_index]
    except IndexError:
        raise IndexError(f"Erreur rencontrée avec la ressource {nom_item}. La cause probable est que la ressource fille nécessaire appartient à une autre compétence que l'item mère. Cette fonction sera éventuellement prise en charge!")

    ressources_liste = format_ressources(ressources_item) # Liste des ressources pour l'objet examiné

    if ressources_liste[0] == "-" or None or "": # Il n'y a pas de ressources requises
        return liste_ressources_input # Retourner la liste d'entrée non modifiée. Cela termine la récursivité le cas échéant.

    for i in range(len(ressources_liste)):
        ressources_liste[i] = ressources_liste[i].strip()

    for i in range(len(ressources_liste)): # S'il y a des ressources dans la liste
        if ressources_liste[i][-1] == ")" and ressources_liste[i][-3] == "(": # Un multiple de cette ressource est nécessaire
            for j in range(int(ressources_liste[i][-2])):
                liste_ressources_this_iter.append(ressources_liste[i][:-3].strip()) # Ajouter cette ressource un nombre approprié de fois
        else:
            liste_ressources_this_iter.append(ressources_liste[i].strip()) # Sinon, l'ajouter une seule fois

    liste_ressources_input += liste_ressources_this_iter # Ajouter les ressources à la liste d'input
    for ressource in liste_ressources_this_iter: # pour chaque ressource dans la liste générée cette itération
        # print("La fonction sera appelée recursivement. À ce stade la liste est:")
        # print(liste_ressources_this_iter)
        return_ressources(df, ressource, liste_ressources_input) # Utiliser récursivement la fonction pour ajouter les ressources filles

    return liste_ressources_input # Une fois la récursivité terminée, retourner la liste complète.

