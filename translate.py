import pandas as pd
import re


# Excel beolvasása egyszer, globálisan
df = pd.read_excel("verbos.xlsx", sheet_name="verbos", skiprows=2, engine="openpyxl")

# Szótárak létrehozása
hu_to_es = {
    str(k).strip().lower(): str(v).strip()
    for k, v in zip(df.iloc[:, 0], df.iloc[:, 1])
}

es_to_hu = {
    str(v).strip().lower(): str(k).strip()
    for k, v in zip(df.iloc[:, 0], df.iloc[:, 1])
}

''' def translate_hu_to_es(verb_hu):
    return hu_to_es.get(verb_hu.strip().lower()) '''

def translate_hu_to_es(verb_hu):
    verb_hu = verb_hu.strip().lower()
    for hu, es in hu_to_es.items():
        # Zárójeles rész eltávolítása
        hu_clean = re.sub(r"\s*\(.*?\)", "", hu)

        # Többes jelentés szétbontása
        hu_parts = [part.strip().lower() for part in hu_clean.split("/")]

        # Pontos egyezés keresése
        if verb_hu in hu_parts:
            return es
    return None


def translate_es_to_hu(verb_es):
    return es_to_hu.get(verb_es.strip().lower())