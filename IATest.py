import json
from ollama import chat
from main import get_tree


model = "deepseek-r1:14b"

ORDER = """
Réponds sans texte inutile, on ne cherche ici que la réponse a la question, ne fait aucun détour, répond juste la pure vérité
"""

dir = "N:\\Download\\parcoursup"

folder = []

folder = get_tree(dir, folder)

folderString = json.dumps(folder)


stream = chat(
    model=model,
    messages=[
        {"role": "system", "content": ORDER},
        {
            "role": "user",
            "content": "D'après cette structure de donnée"
            + folderString
            + "combien y a t'il de pdf, donne moi juste le nombre",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
