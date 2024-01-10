import os
#test
def classifier(valeur):
    if valeur <= -127:
        return 1
    elif -127 < valeur <= -107:
        return 2
    elif -107 < valeur <= -27:
        return 3
    elif -27 < valeur <= 30:
        return 4
    elif 30 < valeur <= 82:
        return 5
    elif 82 < valeur <= 140:
        return 6
    else:
        return 7

def traiter_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as f:
            lignes = f.readlines()
        resultats = [classifier(float(valeur)) for valeur in lignes]

        resultats_padded = resultats + [0] * (395 - len(resultats))
        print(f"Résultats pour le fichier {chemin_fichier}:")
        for resultat in resultats_padded:
            print(resultat)
        dossier_destination = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/TrueAngles_TrainMULTI"
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)
        nom_fichier = os.path.basename(chemin_fichier)
        chemin_destination = os.path.join(dossier_destination, nom_fichier)

        with open(chemin_destination, 'w') as f_dest:
            for resultat in resultats_padded:
                f_dest.write(str(resultat) + '\n')

        print(f"Le fichier traité a été sauvegardé dans {chemin_destination}")

    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    dossier_a_traiter = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/Alpha_valueTrain"
    fichiers_du_dossier = os.listdir(dossier_a_traiter)
    fichiers_texte = [fichier for fichier in fichiers_du_dossier if fichier.endswith(".txt")]
    for fichier in fichiers_texte:
        chemin_absolu = os.path.join(dossier_a_traiter, fichier)
        traiter_fichier(chemin_absolu)
