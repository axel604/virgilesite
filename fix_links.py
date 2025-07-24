import os
import re

def patch_nav_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Supprimer slash initial sur les liens href internes (menu, footer, etc)
    # mais NE PAS toucher aux liens commençant par // ou http
    content = re.sub(r'href="/(?!/|http)', 'href="', content)

    # 2. Remplacer blog.html par blog/
    content = re.sub(r'href="blog\.html"', 'href="blog/"', content)

    # 3. Remplacer href="#contact" par contact.html (menu)
    content = re.sub(r'href="#contact"', 'href="contact.html"', content)

    # 4. Remplacer les sous-pages .html par / pour dossiers (menu typique)
    for page in ["nourrissons", "sportifs", "seniors", "quotidien"]:
        # href="sportifs.html" → href="sportifs/"
        content = re.sub(
            rf'href="{page}\.html"', 
            f'href="{page}/"', 
            content
        )

    # 5. Bonus : remettre .html uniquement sur les pages de la racine
    # (C'est optionnel et à ajuster selon tes besoins)

    if original != content:
        print(f"Patched: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

def patch_all_html(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".html"):
                patch_nav_links(os.path.join(dirpath, file))

if __name__ == "__main__":
    patch_all_html(".")
    print("Tous les menus/footers ont été patchés !")
