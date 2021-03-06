import I_A
from tkinter import *

class Incertitude_intelligente:

    def __init__(self):
        self.appareil_calcul = ''
        self.courant = ''

        self.window = Tk()
        self.window.title('Incertitude')
        self.window.geometry('720x480')
        self.appareil = Frame()
        self.appareil_text = Label(self.window,font=('arial', 20),text="Entrez l'appareil (4,5 ou 6,5)")
        self.appareil_text.pack(expand=True)
        self.appareil1_button = Button(self.appareil, text='6,5' ,command= lambda : self.type_appareil('6.5'))
        self.appareil1_button.grid(row=0,column=0)
        self.appareil2_button = Button(self.appareil, text='4,5',command= lambda : self.type_appareil('4.5'))
        self.appareil2_button.grid(row=0,column=1)
        self.appareil3_button = Button(self.appareil, text='Source',command= lambda : self.type_appareil('Source'))
        self.appareil3_button.grid(row=0,column=2)
        self.appareil.pack(expand=True)

        self.curent_type = Frame()
        self.curent = Frame(self.curent_type)
        self.curent_text = Label(self.window,font=('arial', 20),text="Entrez le type de courant")
        self.curent_text.pack(expand=True)
        self.DC_button = Button(self.curent, text='DC' ,command= lambda : self.type_courant('DC'))
        self.DC_button.grid(row=0,column=0)
        self.AC_button = Button(self.curent, text='AC',command= lambda : self.type_courant('AC'))
        self.AC_button.grid(row=0,column=1)
        self.curent.pack(expand = True)
        self.curent_type.pack(expand=True)

        self.Valeur = Frame()
        self.Valeur_text = Label(self.window,font=('arial', 20), text="Entrez votre mesure")
        self.Valeur_text.pack(expand=True)
        self.Valeur_entry = Entry(self.Valeur, bd=0)
        self.Valeur_entry.grid(row=0,column=0)
        self.Valeur.pack(expand=True)
        self.réponse = Frame()
        self.réponse_text = Label(self.window,font=('arial', 20), text="Votre incertitude est : ")
        self.réponse_text.pack(expand=True)
        self.range_text = Label(self.window,font=('arial', 20), text="Le range déterminé est : ")
        self.range_text.pack(expand=True)
        self.Boutton = Frame()
        self.Type4_button = Button(self.Boutton, text='Calculez',command= lambda : self.appeler_calculs(self.Valeur_entry.get()))
        self.Type4_button.grid(row=0,column=0)
        self.Type5_button = Button(self.Boutton, text='Reset',command=self.reset)
        self.Type5_button.grid(row=0,column=1)
        self.Boutton.pack(expand=True)

        self.window.mainloop()

    def type_appareil(self,num):
        self.appareil_calcul = num
        if num == '6.5':
            self.appareil1_button.config(foreground="red")
            self.appareil2_button.config(foreground="black")
            self.appareil3_button.config(foreground="black")
        elif num == '4.5':
            self.appareil2_button.config(foreground="red")
            self.appareil1_button.config(foreground="black")
            self.appareil3_button.config(foreground="black")
        elif num == 'Source':
            self.appareil_calcul = '5.0'
            self.appareil2_button.config(foreground="black")
            self.appareil1_button.config(foreground="black")
            self.appareil3_button.config(foreground="red")

    def type_courant(self, value):
        if value == "AC":
            self.appareil_calcul = float(self.appareil_calcul)+1
            self.courant = "AC"
            self.frequence = Frame(self.curent_type)
            self.courant_text = Label(self.frequence,font=('arial', 20), text="Entrez votre fréquence")
            self.courant_text.grid(row=1, column=0)
            self.courant_entry = Entry(self.frequence, bd=0)
            self.courant_entry.grid(row=1, column=1)
            self.frequence.pack(expand=True)
            self.AC_button.config(foreground="red")
            self.DC_button.config(foreground="black")
        elif value == "DC":
            self.courant = "DC"
            self.DC_button.config(foreground="red")
            self.AC_button.config(foreground="black")

    def appeler_calculs(self, valeur):
        if self.courant == "DC":
            try:
                a = I_A.calcul_intelligent(str(valeur),self.appareil_calcul)
            except Exception:
                rep = Tk()
                rep_text = Label(rep,font=('arial', 20), text='Erreur')
                rep_text.pack(expand=True)
                rep.mainloop()
            self.réponse_text.config(text=f"Votre réponse est : {a[0]}")
            self.range_text.config(text=f"Le range déterminé est : {a[1]}")
        else:
            try:
                a = I_A.calcul_intelligent_AC(str(valeur),self.appareil_calcul, self.frequence)
            except Exception:
                rep = Tk()
                rep_text = Label(rep,font=('arial', 20), text='Erreur')
                rep_text.pack(expand=True)
                rep.mainloop()
                self.réponse_text.config(text=f"Votre réponse est : {a[0]}")
                self.range_text.config(text=f"Le range déterminé est : {a[1]}")

    def reset(self):
        self.appareil_calcul = ''
        self.appareil2_button.config(foreground="black")
        self.appareil1_button.config(foreground="black")
