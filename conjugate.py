from openpyxl import load_workbook


def conjugate_presente(verb_es):
    verb = SpanishVerb(verb_es)

    if verb.is_irregular:
        return f"{verb_es}: coming soon (irregular)"

    if verb.group == "ar":
        return conjugate_presente_ar(verb)
    elif verb.group == "er":
        return conjugate_presente_er(verb)
    elif verb.group == "ir":
        return conjugate_presente_ir(verb)

def conjugate_presente_ar(verb):
    stem = verb.stemPresente
    endings = ["o", "as", "a", "amos", "áis", "an"]
    persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

    forms = [f"{person} {stem}{ending}" for person, ending in zip(persons, endings)]
    return "\n".join(forms)

def conjugate_presente_er(verb):
    stem = verb.stemPresente
    endings = ["o", "es", "e", "emos", "éis", "en"]
    persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

    forms = [f"{person} {stem}{ending}" for person, ending in zip(persons, endings)]
    return "\n".join(forms)

def conjugate_presente_ir(verb):
    stem = verb.stemPresente
    endings = ["o", "es", "e", "imos", "ís", "en"]
    persons = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

    forms = [f"{person} {stem}{ending}" for person, ending in zip(persons, endings)]
    return "\n".join(forms)

class SpanishVerb:
    def __init__(self, infinitive):
        self.infinitive = infinitive.strip().lower()
        self.is_reflexive = self.infinitive.endswith("se")
        self.group = self._get_group()
        self.is_irregular = self._is_irregular()

        if self.is_irregular:
            self.stemPresente = self._get_irregularStem()  # később bővíthető
        else:
            self.stemPresente = self._get_regularStem()

    def _get_irregularStem(self):
        return "coming soon"

    def _get_regularStem(self):
        if self.is_reflexive:
            return self.infinitive[:-4]
        return self.infinitive[:-2]

    def _get_group(self):
        if self.infinitive.endswith(("ar", "arse")):
            return "ar"
        elif self.infinitive.endswith(("er", "erse")):
            return "er"
        else:
            return "ir"

    def _is_irregular(self):
        verb_es = self.infinitive.strip().lower()
        wb = load_workbook("verbos.xlsx")
        ws = wb["verbos"]

        for row in ws.iter_rows(min_row=3):  # feltételezve, hogy az első 2 sor fejléc
            cell_value = str(row[1].value).strip().lower()  # B oszlop = spanyol ige
            if cell_value == verb_es:
                cell_d = row[3]  # D oszlop = stemPresente
                font_color = cell_d.font.color

                # Ha van szín és RGB típusú, akkor ellenőrizzük
                if font_color and font_color.type == "rgb":
                    return font_color.rgb.upper() == "FFFF0000"  # piros színkód
                return False
        return False