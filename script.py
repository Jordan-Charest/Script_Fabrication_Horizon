from data_functions import *

# Entrer le nom de la compétence

valid_competence = False
while valid_competence is False:
    try:
        competence = input("Entrez la compétence de fabrication:")
        df = return_dataframe(competence)
        valid_competence = True
    except:
        print("Le nom de la compétence est invalide. Réessayez.\n")

print(df)


valid_item = False
while valid_item is False:
    try:
        item = input("Entrer le nom de l'item (sensible à la casse et à la ponctuation):")
        (temps, cout, prereq, liste_ressources) = return_item_data(df, item)
        valid_item = True
    except:
        print("Le nom de l'item est invalide ou appartient à une autre compétence que celle spécifiée. Réessayez.\n")

print(f"\nLe nom est {item}, le temps est {temps} min, et le coût de fabrication est {cout} cr.\n")


if prereq == "-" or None:
    print(f"Il n'y a aucun pré-requis pour l'item.")
else:
    print(f"Le pré-requis est: {prereq}")

if liste_ressources[0] == "-" or None:
    print(f"Il n'y a aucune ressource nécessaire à la fabrication de l'item.")
else:
    print(f"La liste de ressources nécessaires à la fabrication de l'item est:\n{liste_ressources}")
    cout_tot = input("Souhaitez-vous connaître le coût total de fabrication incluant le coût de fabrication des ressources requises? (O/N)")



    if cout_tot == "O" or "o":
        liste_ressources_input = [item]
        liste_finale = return_ressources(df, item, liste_ressources_input)

        print("La liste totale de ressources requises est (incluant la ressource finale):")
        print(liste_finale)

        temps_counter = 0
        cout_counter = 0

        for item in liste_finale:
            (temps_add, cout_add, prereq_add, liste_ressources_add) = return_item_data(df, item)
            temps_counter += float(temps_add)
            cout_counter += float(cout_add)

        print(f"Le coût total pour produire l'item ainsi que toutes les ressources filles est {cout_counter}.")
        print(f"Le temps total pour produire l'item ainsi que toutes les ressources filles est {temps_counter}.")
