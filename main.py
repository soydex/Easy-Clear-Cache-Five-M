import os
import shutil

home_dir = os.path.expanduser("~")
fivem_dir = os.path.join(
    home_dir, "AppData", "Local", "FiveM", "FiveM.app", "data"
)

folder_to_keep = "game-storage"

if os.path.exists(fivem_dir):
    try:
        folders = os.listdir(fivem_dir)
        for folder in folders:
            if folder != folder_to_keep:
                folder_path = os.path.join(fivem_dir, folder)
                shutil.rmtree(folder_path)
                print(f"Dossier supprimé : {folder_path}")

        print(f"Tous les dossiers sauf '{folder_to_keep}' ont été supprimés avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
else:
    print(f"Le répertoire spécifié n'existe pas : {fivem_dir}")
