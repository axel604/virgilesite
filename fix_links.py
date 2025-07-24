import os
import re

def patch_img_links(filepath, relpath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    patched = content

    # Compte le niveau de profondeur du fichier
    depth = relpath.count(os.sep)
    # On ne patch que si ce n'est pas à la racine (root)
    if depth > 0:
        # Pour chaque <img src="images/...">, on ajoute les ../ nécessaires
        patched = re.sub(
            r'src="images/', f'src="{"../" * depth}images/', patched
        )
        # Pour chaque <img src="favicon/...
        patched = re.sub(
            r'src="favicon/', f'src="{"../" * depth}favicon/', patched
        )
        # Tu peux ajouter d'autres patchs si tu as d'autres dossiers d'assets

    if patched != content:
        print(f"Patched: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(patched)

def patch_all_html(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".html"):
                relpath = os.path.relpath(os.path.join(dirpath, file), root)
                patch_img_links(os.path.join(dirpath, file), relpath)

if __name__ == "__main__":
    patch_all_html(".")
    print("Tous les chemins d’images ont été adaptés selon la profondeur du fichier !")
