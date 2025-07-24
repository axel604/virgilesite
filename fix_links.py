import os
import re

# Extensions à traiter
EXTS = (".html", ".xml", ".txt")

def rewrite_links_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Remplace /virgilesite/xxx par xxx (chemin relatif)
    content = re.sub(r'href="/virgilesite/([^"]+)"', r'href="\1"', content)
    content = re.sub(r'src="/virgilesite/([^"]+)"', r'src="\1"', content)
    # Remplace /xxx.html par xxx.html (sauf si http, https, //)
    content = re.sub(r'href="/([^"/][^"]*)"', r'href="\1"', content)
    content = re.sub(r'src="/([^"/][^"]*)"', r'src="\1"', content)
    # Facultatif : gère les liens dans le sitemap et robots.txt
    content = re.sub(r'https://axel604.github.io/virgilesite/', r'https://axel604.github.io/virgilesite/', content) # garder pour le sitemap actuel
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(EXTS):
                filepath = os.path.join(subdir, file)
                rewrite_links_in_file(filepath)
                print(f"✔ Liens corrigés dans : {filepath}")

if __name__ == "__main__":
    # Mets ici le chemin de ton dossier projet, "." pour le dossier courant
    dossier = "."
    main(dossier)
