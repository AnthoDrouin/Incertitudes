from tkinter import *
import calculs_de_masse
import calculs_simples
import calculs
import calculs_intelligent

class intro:
    def __init__(self):
        self.intro = Tk()
        self.intro.title('Incertitude')
        self.intro.geometry('720x480')
        self.incertitude = Frame()
        self.appareil_text = Label(self.intro,font=('arial', 20),text="Choisissez le type calculs")
        self.appareil_text.pack(expand=True)
        self.incertitude_text = Label(self.intro,font=('arial', 20),text="Section incertitudes")
        self.incertitude_text.pack(expand=True)
        #self.bouton_1 = Button(self.incertitude, text='Calculs simple')
        #self.bouton_1.grid(row=0, column=0)
        self.bouton_2 = Button(self.incertitude, text='Calculs de masse' ,command= self.appel_mass)
        self.bouton_2.grid(row=0, column=1)
        self.bouton_3 = Button(self.incertitude, text='Calculs intelligent', command = self.appel_intelligent)
        self.bouton_3.grid(row=0, column=0)
        self.incertitude.pack(expand=True)
        self.incertitude_text = Label(self.intro,font=('arial', 20),text="Section graphiques")
        self.incertitude_text.pack(expand=True)
        self.intro.mainloop()

    def appel_mass(self):
        self.intro.destroy()
        calculs_de_masse.incertitudes_de_masses()
    
    def appel_simple(self):
        self.intro.destroy()
        calculs_simples.incertitudes()

    def appel_intelligent(self):
        self.intro.destroy()
        calculs_intelligent.Incertitude_intelligente()

a = intro()

#ca fonctionne !
