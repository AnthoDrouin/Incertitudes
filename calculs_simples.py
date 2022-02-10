
from tkinter import *
from turtle import right
from calculs import calculs, Instruments
from sigfig import round
class incertitudes:

    def __init__(self):

        self.appareil_calcul = ''
        self.type_calcul = ''
        self.range_calcul = ''

        self.window = Tk()
        self.window.title('Incertitude')
        self.window.geometry('720x480')
        self.appareil = Frame()
        self.appareil_text = Label(self.window,font=('arial', 20),text="Entrez l'appareil (4,5 ou 6,5)")
        self.appareil_text.pack(expand=True)
        self.appareil1_button = Button(self.appareil, text='6,5' ,command= lambda : self.type_appareil('6,5'))
        self.appareil1_button.grid(row=0, column=0)
        self.appareil2_button = Button(self.appareil, text='4,5',command= lambda : self.type_appareil('4,5'))
        self.appareil2_button.grid(row=0, column=1)
        self.appareil3_button = Button(self.appareil, text='Source',command= lambda : self.type_appareil('Source'))
        self.appareil3_button.grid(row=0, column=2)
        self.appareil.pack(expand=True)
        self.Type = Frame()
        self.Type_text = Label(self.window,font=('arial', 20), text="Entrez le type de mesure ")
        self.Type_text.pack(expand=True)
        self.Type1_button = Button(self.Type, text='Tension',command= lambda : self.type_type('Tension'))
        self.Type1_button.grid(row=0,column=0)
        self.Type2_button = Button(self.Type, text='Résistance',command= lambda : self.type_type('Résistance'))
        self.Type2_button.grid(row=0,column=1)
        self.Type3_button = Button(self.Type, text='Courant',command= lambda : self.type_type('Courant'))
        self.Type3_button.grid(row=0,column=2)
        self.Type.pack(expand=True)
        self.Range = Frame()
        self.Range_text = Label(self.window,font=('arial', 20), text="Entrez le range de votre mesure")
        self.Range_text.pack(expand=True)
        self.Range_entry = Entry(self.Range, bd=0)
        self.Range_entry.grid(row=0,column=0)
        self.Range.pack(expand=True)
        self.Valeur = Frame()
        self.Valeur_text = Label(self.window,font=('arial', 20), text="Entrez votre mesure")
        self.Valeur_text.pack(expand=True)
        self.Valeur_entry = Entry(self.Valeur, bd=0)
        self.Valeur_entry.grid(row=0,column=0)
        self.Valeur.pack(expand=True)
        self.Boutton = Frame()
        self.Type4_button = Button(self.Boutton, text='Calculez',command= lambda : self.appeler_calculs(self.Valeur_entry.get(), self.Range_entry.get()))
        self.Type4_button.grid(row=0,column=0)
        self.Type5_button = Button(self.Boutton, text='Reset',command=self.reset)
        self.Type5_button.grid(row=0,column=1)
        self.Boutton.pack(expand=True)
    

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
        self.Type1_button.config(foreground="black")
        self.Type2_button.config(foreground="black")
        self.Type3_button.config(foreground="black")
        self.appareil2_button.config(foreground="black")
        self.appareil1_button.config(foreground="black")
        self.appareil3_button.config(foreground="black")
        

    def appeler_calculs(self,valeur,range):
        range = str(range)
        valeur = str(valeur)
        try:
            incertitude = calculs(self.appareil_calcul, self.type_calcul, range, valeur)
            incertitude = round(incertitude, sigfigs = 2)
            rep = Tk()
            rep_text = Label(rep,font=('arial', 20), text=str(incertitude))
            rep_text.pack(expand=True)
            rep.mainloop()
        except Exception:
            rep = Tk()
            rep_text = Label(rep,font=('arial', 20), text='Erreur')
            rep_text.pack(expand=True)
            rep.mainloop()
