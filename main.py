import json
from ollama import chat


model = "deepseek-r1:14b"

ORDER = """
Réponds sans texte inutile, on ne cherche ici que la réponse a la question, ne fait aucun détour, répond juste la pure vérité
"""

folder = {
    "Documents": ["Documents/File.md", "Documents/File.txt" "Documents/File.docx"],
    "Downloads": ["Downloads/File.zip", "Downloads/File.tar.gz" "Downloads/File.txt"],
}

folderString = json.dumps(folder)

stream = chat(
    model=model,
    messages=[
        {"role": "system", "content": ORDER},
        {
            "role": "user",
            "content": "D'après cette structure de donnée"
            + folderString
            + "quels sont les fichiers dans les dossier Documents et Downloads?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
