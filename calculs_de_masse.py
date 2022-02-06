
from tkinter import *
from calculs import calculs2excel, Instruments

class incertitudes_de_masses:

    def __init__(self):

        self.appareil_calcul = ''
        self.type_calcul = ''
        self.range_calcul = ''
        self.liste = []
        self.window = Tk()
        self.window.title('Incertitude')
        self.window.geometry('720x480')

        self.info = Frame()
        self.appareil = Frame(self.info)
        self.appareil_text = Label(self.info,font=('arial', 20),text="Entrez l'appareil (4,5 ou 6,5)")
        self.appareil_text.pack(expand=True)
        self.appareil1_button = Button(self.appareil, text='6,5' ,command= lambda : self.type_appareil('6,5'))
        self.appareil1_button.pack(side=LEFT)
        self.appareil2_button = Button(self.appareil, text='4,5',command= lambda : self.type_appareil('4,5'))
        self.appareil2_button.pack(side=RIGHT)
        self.appareil.pack(expand=True)
        self.Type = Frame(self.info)
        self.Type_text = Label(self.info,font=('arial', 20), text="Entrez le type de mesure ")
        self.Type_text.pack(expand=True)
        self.Type1_button = Button(self.Type, text='Tension',command= lambda : self.type_type('Tension'))
        self.Type1_button.grid(row=0,column=0)
        self.Type2_button = Button(self.Type, text='Résistance',command= lambda : self.type_type('Résistance'))
        self.Type2_button.grid(row=0,column=1)
        self.Type3_button = Button(self.Type, text='Courant',command= lambda : self.type_type('Courant'))
        self.Type3_button.grid(row=0,column=2)
        self.Type.pack(expand=True)
        self.Range = Frame(self.info)
        self.Range_text = Label(self.info,font=('arial', 20), text="Entrez le range de votre mesure")
        self.Range_text.pack(expand=True)
        self.Range_entry = Entry(self.Range, bd=0)
        self.Range_entry.grid(row=0,column=0)
        self.Range.pack(expand=True)
        self.Valeur = Frame(self.info)
        self.Valeur_text = Label(self.info,font=('arial', 20), text="Entrez votre mesure")
        self.Valeur_text.pack(expand=True)
        self.Valeur_entry = Entry(self.Valeur, bd=0)
        self.Valeur_entry.grid(row=0,column=0)
        self.Valeur.pack(expand=True)
        self.Boutton = Frame(self.info)
        self.Type4_button = Button(self.Boutton, text='Calculez',command= lambda : self.prénom())
        self.Type4_button.grid(row=0,column=0)
        self.Type5_button = Button(self.Boutton, text='Reset',command= lambda : self.reset())
        self.Type5_button.grid(row=0,column=1)
        self.Type6_button = Button(self.Boutton, text='Ajouter',command= lambda : self.ajout(self.Valeur_entry.get(), self.Range_entry.get()))
        self.Type6_button.grid(row=0,column=2)
        self.Boutton.pack(expand=True)
        self.info.pack(expand=True)
        self.window.mainloop()

    def type_appareil(self,num):
        self.appareil_calcul = num
        if num == '6,5':
            self.appareil1_button.config(foreground="red")
            self.appareil2_button.config(foreground="black")
        elif num == '4,5':
            self.appareil2_button.config(foreground="red")
            self.appareil1_button.config(foreground="black")

    def type_type(self,type):
        self.type_calcul = type
        self.Type1_button.config(foreground="black")
        self.Type2_button.config(foreground="black")
        self.Type3_button.config(foreground="black")
        if type == 'Tension':
            self.Type1_button.config(foreground="red")
        elif type == 'Courant':
            self.Type3_button.config(foreground="red")
        elif type == 'Résistance':
            self.Type2_button.config(foreground="red")

    def reset(self):
        self.appareil_calcul = ''
        self.type_calcul = ''

    def ajout(self,valeur,range):
        self.liste.append([self.appareil_calcul, self.type_calcul, range, valeur])

    def prénom(self):

        def name(nom):
            Nom.destroy()
            self.appeler_calculs(nom)

        Nom = Tk()
        Nom.geometry('720x480')
        Nom_label = Label(Nom,font=('arial', 20), text="Veuillez entrez le nom de votre fichier")
        Nom_label.pack(expand=True)
        Nom_entry = Entry(Nom, bd=0)
        Nom_entry.pack(expand=True)
        Nom_button = Button(Nom, text='Choisir',command= lambda : name(Nom_entry.get()))
        Nom_button.pack(expand=True)
        Nom.mainloop()

    def appeler_calculs(self, nom):
        try:
            calculs2excel(self.liste, nom)
            rep = Tk()
            rep_text = Label(rep,font=('arial', 20), text='Réussi')
            rep_text.pack(expand=True)
            rep.mainloop()
        except Exception:
            rep = Tk()
            rep_text = Label(rep,font=('arial', 20), text='Erreur')
            rep_text.pack(expand=True)
            rep.mainloop()

class Name:

    def __init__(self):
        self.Name = ''
        self.Nom = Tk()
        self.Nom.geometry('720x480')
        self.Nom_label = Label(self.Nom,font=('arial', 20), text="Veuillez entrez le nom de votre fichier")
        self.Nom_label.pack(expand=True)
        self.Nom_entry = Entry(self.Nom, bd=0)
        self.Nom_entry.pack(expand=True)
        self.Nom_button = Button(self.Nom, text='Choisir',command= lambda : self.name(self.Nom_entry.get()))
        self.Nom_button.pack(expand=True)
        self.Nom.mainloop()

    def name(self,name):
        self.Name = name
        self.kill()

    def kill(self):
        self.Nom.destroy()
        
a = incertitudes_de_masses()