import tkinter as tk
from translate import translate_hu_to_es, translate_es_to_hu
from ui_conjugate import ui_conjugate_presente
from draw import draw_smiley, draw_sad_smiley, draw_thinking_smiley

def output():
    verb = verb_entry.get().strip().lower()

    if verb.endswith("ni"):
        conjugation_label.config(text="")
        verb_es = translate_hu_to_es(verb)

        if verb_es == "haber":
            result_label.config(text="Az ige spanyolul: haber. \nAz haber létezést kifejező imperszonális ige, jelen időben csak egy alakban használatos: e/3 → hay.", fg="black")
            draw_smiley(smiley_canvas)
            return
        elif verb_es:
            result_label.config(text=f"Az ige spanyolul: {verb_es}", fg="black")
            conjugation = ui_conjugate_presente(verb_es)
            conjugation_label.config(text=f"Ragozás eredménye:\n{conjugation}", fg="darkblue")
            draw_smiley(smiley_canvas)
        else:
            result_label.config(text="Nincs fordítás az adatbázisban!", fg="red")
            conjugation_label.config(text="")
            draw_sad_smiley(smiley_canvas)

    elif verb == "haber":
        result_label.config(text="Az ige magyarul: létezni. \nAz haber létezést kifejező imperszonális ige, jelen időben csak egy alakban használatos: e/3 → hay.", fg="black")
        draw_smiley(smiley_canvas)
        return

    elif verb.endswith(("ar", "er", "ir", "ír", "arse", "erse", "irse", "írse")):
        verb_es = verb
        verb_hu = translate_es_to_hu(verb_es)
        conjugation = ui_conjugate_presente(verb_es)

        if verb_hu:
            result_label.config(text=f"Az ige magyarul: {verb_hu}", fg="black")
            conjugation_label.config(text=f"Ragozás eredménye:\n{conjugation}", fg="darkblue")
            draw_smiley(smiley_canvas)
        else:
            result_label.config(text="Az ige nem található a szótárban, lehetséges ragozás:", fg="orange")
            conjugation_label.config(text=conjugation, fg="darkblue")
            draw_thinking_smiley(smiley_canvas)
    else:
        result_label.config(text="Nem ige vagy helytelen alak!", fg="red")
        conjugation_label.config(text="")
        draw_sad_smiley(smiley_canvas)
        return
def insert_nh():
    verb_entry.insert(tk.INSERT, "ñ")
    verb_entry.focus_set()

window = tk.Tk()
window.title("Spanyol Igeragozó")
window.geometry("600x300")

tk.Label(window, text="Kérem adja meg a ragozni kívánt igét főnévi igenév alakban(enni, olvasni):").pack(pady=5)
tk.Label(window, text="Por favor, introduzca el verbo en infinitivo (comer, leer):").pack(pady=2)

verb_entry = tk.Entry(window, width=30)
verb_entry.focus()
verb_entry.pack(pady=5)
nh_button = tk.Button(window, text="ñ", command=insert_nh, width=2)
nh_button.place(in_=verb_entry, relx=1.0, rely=0.0, x=5, y=0, anchor="nw")
verb_entry.bind("<Return>", lambda event: output())

tk.Button(window, text="Ragozás", command=output).pack(pady=10)

result_label = tk.Label(window, text="", fg="blue")
result_label.pack(pady=5)

conjugation_label = tk.Label(window, text="", fg="yellow")
conjugation_label.pack()

smiley_canvas = tk.Canvas(window, width=130, height=130, highlightthickness=0, bg=window.cget("bg"))
smiley_canvas.place(x=10, y=170)
draw_smiley(smiley_canvas)

exit_button = tk.Button(window, text="Kilépés", command=window.quit)
exit_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

window.mainloop()


