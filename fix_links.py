import os
import re

def patch_links_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Patch tous les chemins qui commencent par / et qui ne sont pas des URL externes
    # Pour les balises src et href
    content_patched = re.sub(r'((src|href)=["\'])/(?!/|[a-zA-Z]+:)', r'\1', content)

    # Optionnel : tu peux ajouter d'autres patterns si besoin

    if content != content_patched:
        print(f"Patched: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content_patched)

def patch_all_html(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".html"):
                patch_links_in_file(os.path.join(dirpath, file))

if __name__ == "__main__":
    patch_all_html(".")
    print("Tous les fichiers HTML ont été patchés !")