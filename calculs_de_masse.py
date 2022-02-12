
from distutils import command
from tkinter import BOTH, ttk, Frame, Button, Label, Entry, Tk, StringVar, mainloop, LEFT, RIGHT
from I_A import calcul_intelligent, excel2excel
from matplotlib.pyplot import close, text
from calculs import calculs2excel, Instruments, calculs2tk
import tkinterDnD 


class incertitudes_de_masses:

    def __init__(self):

        self.appareil_calcul = ''
        self.type_calcul = ''
        self.range_calcul = ''
        self.liste = []
        self.window = Tk()
        self.window.title('Incertitude')
        self.window.geometry('720x480')
        self.excel = ''
        self.exporter = 'méthode_1'

        self.info = Frame()
        self.appareil = Frame(self.info)
        self.appareil_text = Label(self.info,font=('arial', 20),text="Entrez l'appareil (4,5 ou 6,5)")
        self.appareil_text.pack(expand=True)
        self.appareil1_button = Button(self.appareil, text='6,5' ,command= lambda : self.type_appareil('6,5'))
        self.appareil1_button.grid(row=0, column=0)
        self.appareil2_button = Button(self.appareil, text='4,5',command= lambda : self.type_appareil('4,5'))
        self.appareil2_button.grid(row=0, column=1)
        self.appareil3_button = Button(self.appareil, text='Source',command= lambda : self.type_appareil('Source'))
        self.appareil3_button.grid(row=0, column=2)
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
        self.Boutton= Frame(self.info)
        self.Boutton1 = Frame(self.Boutton)
        self.Boutton2 = Frame(self.Boutton)
        self.Type4_button = Button(self.Boutton2, text='Exporter',command= lambda : self.prénom())
        self.Type4_button.pack(side=LEFT, fill="both")
        self.Type5_button = Button(self.Boutton1, text='   Reset   ',command= lambda : self.reset())
        self.Type5_button.pack(side=RIGHT, fill="both")
        self.Type6_button = Button(self.Boutton1, text='Calculer',command= lambda : self.ajout(self.Valeur_entry.get(), self.Range_entry.get()))
        self.Type6_button.pack(side=LEFT, fill="both")
        self.Type7_button = Button(self.Boutton2, text='Importer',command= lambda : self.importer())
        self.Type7_button.pack(side=RIGHT, fill="both")
        self.Boutton1.pack(expand=True,fill="both")
        self.Boutton2.pack(expand=True,fill="both")
        self.Boutton.pack(expand=True)
        self.info.pack(side=LEFT, expand=True)

        self.information = Frame()
        self.info_text = Frame(self.information)
        self.info_label = Label(self.info_text,font=('arial', 20), text="Voici les mesures saisies")
        self.info_label.pack()
        self.info_text.pack()
        self.info_liste = Frame(self.information)
        self.info_liste.pack()
        self.information.pack(side=RIGHT, expand=True)
        

        self.window.mainloop()

    def type_appareil(self,num):
        self.appareil_calcul = num
        if num == '6,5':
            self.appareil2_button.config(foreground="black")
            self.appareil1_button.config(foreground="red")
            self.appareil3_button.config(foreground="black")
        elif num == '4,5':
            self.appareil2_button.config(foreground="red")
            self.appareil1_button.config(foreground="black")
            self.appareil3_button.config(foreground="black")
        elif num == 'Source':
            self.appareil2_button.config(foreground="black")
            self.appareil1_button.config(foreground="black")
            self.appareil3_button.config(foreground="red")

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
        self.liste = []
        self.Type1_button.config(foreground="black")
        self.Type2_button.config(foreground="black")
        self.Type3_button.config(foreground="black")
        self.appareil2_button.config(foreground="black")
        self.appareil1_button.config(foreground="black")
        self.appareil3_button.config(foreground="black")
        self.info_liste.destroy()

    def ajout(self,valeur,range):
        a = [self.appareil_calcul, self.type_calcul, range, valeur]
        b = str(a)
        self.liste.append(a)
        c = calculs2tk([a])
        self.valeur_liste = Label(self.info_liste,font=('arial', 20), text=c)
        self.valeur_liste.pack()

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
        if self.exporter == "méthode_1":
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
        elif self.exporter == "méthode_2":
            try:
                print([self.excel, nom, self.Range_entry.get(),self.appareil_calcul])
                appareil = self.appareil_calcul.replace(',','.')
                excel2excel(self.excel, nom, self.Range_entry.get(),appareil)
                rep = Tk()
                rep_text = Label(rep,font=('arial', 20), text='Réussi')
                rep_text.pack(expand=True)
                rep.mainloop()
            except Exception:
                rep = Tk()
                rep_text = Label(rep,font=('arial', 20), text='Erreur')
                rep_text.pack(expand=True)
                rep.mainloop()

    def importer(self):
        root = tkinterDnD.Tk()  
        root.title("tkinterDnD example")
        excel = ''
        self.exporter = 'méthode_2'

        def drop(event):
            global excel
            label_2.config(text=event.data)
            excel = event.data

        def close():
            global excel
            self.excel = excel
            root.destroy()

        label_2 = ttk.Label(root, ondrop=drop, text= 'Glisser le fichier ici!', padding=50, relief="solid")
        label_2.pack(fill="both", expand=True, padx=10, pady=10)
        boutton = Button(root, text='choisir', command= lambda : close())
        boutton.pack(fill="both",expand=True)

        root.mainloop()
