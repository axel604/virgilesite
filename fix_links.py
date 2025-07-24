import os
import re

def patch_img_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Patch tous les chemins Windows absolus pour images
    content_patched = re.sub(
        r'src="C:\\\\Users\\\\sisit\\\\Desktop\\\\Virgilesite\\\\images\\\\([^"]+)"',
        r'src="images/\1"',
        content
    )
    # Patch aussi les variantes sans échappement double
    content_patched = re.sub(
        r'src="C:\\Users\\sisit\\Desktop\\Virgilesite\\images\\([^"]+)"',
        r'src="images/\1"',
        content_patched
    )

    # Patch aussi pour les balises <img src='...'>
    content_patched = re.sub(
        r"src='C:\\Users\\sisit\\Desktop\\Virgilesite\\images\\([^']+)'",
        r"src='images/\1'",
        content_patched
    )

    if content != content_patched:
        print(f"Patched: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content_patched)

def patch_all_html(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".html"):
                patch_img_links(os.path.join(dirpath, file))

if __name__ == "__main__":
    patch_all_html(".")
    print("Tous les liens d’images ont été patchés !")
