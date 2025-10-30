import tkinter as tk
from translate import translate_hu_to_es, translate_es_to_hu
from conjugate import conjugate_presente, SpanishVerb


def output():
    verb = verb_entry.get().strip().lower()

    if verb.endswith("ni"):
        verb_es = translate_hu_to_es(verb)
        if verb_es:
            result_label.config(text=f"Az ige spanyolul: {verb_es}", fg="black")
        else:
            result_label.config(text="Nincs fordítás az adatbázisban!", fg="red")


    elif verb.endswith(("ar", "er", "ir", "ír", "arse", "erse", "irse", "írse")):
        verb_es = verb
        verb_hu = translate_es_to_hu(verb_es)
        result_label.config(text=f"Az ige magyarul: {verb_hu}", fg="black")

    else:
        result_label.config(text="Nem ige vagy helytelen alak!", fg="red")
        return
    conjugate_presente(verb_es)
    conjugation_label.config(text=f"Ragozás eredménye:\n {(conjugate_presente(verb_es))}", fg="darkblue")

    verb_to_conjugate = SpanishVerb(verb_es)
    print("Infinitive:", verb_to_conjugate.infinitive)
    print("Reflexive:", verb_to_conjugate.is_reflexive)
    print("Group:", verb_to_conjugate.group)
    print("irregular type:", verb_to_conjugate.irregular)
    print("Stem (presente):", verb_to_conjugate.stemPresente)
    print(conjugate_presente(verb_es))



# Ablak létrehozása
window = tk.Tk()
window.title("Spanyol Igeragozó")
window.geometry("600x300")

# Címke – utasítás
tk.Label(window, text="Kérem adja meg a ragozni kívánt igét főnévi igenév alakban(enni, olvasni):").pack(pady=5)
tk.Label(window, text="Por favor, introduzca el verbo en infinitivo (comer, leer):").pack(pady=2)

# Beviteli mező
verb_entry = tk.Entry(window, width=30)
verb_entry.pack(pady=5)

# Gomb – ragozás indítása
tk.Button(window, text="Ragozás", command=output).pack(pady=10)

# Eredmény megjelenítése
result_label = tk.Label(window, text="", fg="blue")
result_label.pack(pady=5)

conjugation_label = tk.Label(window, text="", fg="yellow")
conjugation_label.pack()


# GUI futtatása
window.mainloop()