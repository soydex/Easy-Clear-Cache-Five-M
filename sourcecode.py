import os
import shutil

home_dir = os.path.expanduser("~")

fivem_dir_name = "AppData"
fivem_dir_name2 = "Local"
fivem_dir_name3 = "FiveM"
fivem_dir_name4 = "FiveM.app"
fivem_dir_name5 = "data"

fivem_dir = os.path.join(home_dir, fivem_dir_name,fivem_dir_name2,fivem_dir_name3,fivem_dir_name4,fivem_dir_name5,)

folder_to_keep = "game-storage"

folders = os.listdir(fivem_dir)

for folder in folders:
    if folder != folder_to_keep:
        shutil.rmtree(os.path.join(fivem_dir, folder))

print("Tous les dossiers sauf " + folder_to_keep + " ont été supprimés avec succès")
