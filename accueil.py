# -*- coding: utf-8 -*-
from tkinter import  *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from Listedesinscrit import listeInscrit


class Personnage():
    def __init__(self,prenom,nom,adresse,email,photo):
        self.prenom = prenom
        self.nom = nom
        self.adresse = adresse
        self.email = email
        self.photo = photo
    
    def __str__(self):
        return self.prenom + " " + self.nom


        def __eq__(self,other):
            return(self.prenom ==other.prenom and self.nom == other.nom)


def parcourir():
    global imageName
    imn = askopenfilename(initialdir="/",title="selectionner une image ",
    filetypes = (("png files","*.png"),("jpeg files","*.jpg")) )
    if imn:
        imageName=imn
        if imageName:
            texte = imageName.split("/")
            photoEntree.configure(text=".../"+texte[-1])


def appartient(liste,val):
    for i in range(len(liste)):
        if liste[i]==val:
            return TRUE
        return FALSE

def valider():
    global listePersonne,imageName
    photo = imageName
    if prenomEntree.get() and nomEntree.get() and emailEntree.get() and adresseEntree.get() and photo:
        pn = Personnage(prenomEntree.get(),nomEntree.get(),emailEntree.get(),adresseEntree.get(),photo)
        if appartient(listePersonne,pn):
            showerror(title="Formulaire invalide",message="Cet utilisateur existe déja!")
        else:
            listePersonne.append(pn)
            showinfo(title="Enregistrement réussi",message="{} a bien été ajouté".format(prenomEntree.get()))
    else: 
            showerror(title="Formulaire invalide",message="Tous les champs doivent etre renseigner")

def reinitialiser():
    global imageName,listePersonne
    prenomEntree.delete(0,END)
    nomEntree.delete(0,END)
    adresseEntree.delete(0,END)
    emailEntree.delete(0,END)
    imageName=''
    photoEntree.configure(text="aucune image selectionnée")
    # listePersonne.clear()


imageName,listePersonne='',[]

    
fontLabel = 'arial 13 bold'
fontEntree = 'arial 11 bold'

fen = Tk()
fen.geometry("300x320+300+150")
fen.title("Page de login")

contenu = Canvas(fen,bg="#0a89c0")

prenom = Label(contenu, text="prenom: ", font = fontLabel, fg='white', bg="#0a89c0")
nom = Label(contenu, text="nom: ", font = fontLabel, fg='white', bg="#0a89c0")
email = Label(contenu, text=" email: ", font = fontLabel, fg='white', bg="#0a89c0")
adresse = Label(contenu, text="adresse: ", font = fontLabel, fg='white', bg="#0a89c0")
photo = Label(contenu, text="photo: ", font = fontLabel, fg='white', bg="#0a89c0")
VALIDATION = Label(contenu, text="Entrez vos informations ici ", font = fontLabel, fg='#0a89c0', bg='white')


prenomEntree = Entry(contenu,font=fontEntree)
nomEntree = Entry(contenu,font=fontEntree)
emailEntree = Entry(contenu,font=fontEntree)
adresseEntree = Entry(contenu,font=fontEntree)
photoEntree = Label(contenu,text=" pas image selectionnée",font='arial 8 bold', 
fg='#0a89c0',bg='white')

buttonParcourir = Button(contenu,text="Pr", command=parcourir,fg='#0a89c0',bg='white' )

VALIDATION.grid(row=0,column=0,columnspan=2)
prenom.grid(row=1,column=0,sticky=E,padx=5,pady=5)
nom.grid(row=2,column=0,sticky=E,padx=5,pady=5)
email.grid(row=3,column=0,sticky=E,padx=5,pady=5)
adresse.grid(row=4,column=0,sticky=E,padx=5,pady=5)
photo.grid(row=5,column=0,sticky=E,padx=5,pady=5)


prenomEntree.grid(row=1,column=1,padx=5,pady=5)
nomEntree.grid(row=2,column=1,padx=5,pady=5)
emailEntree.grid(row=3,column=1,padx=5,pady=5)
adresseEntree.grid(row=4,column=1,padx=5,pady=5)
photoEntree.grid(row=5,column=1,padx=5,pady=5,sticky=W)
buttonParcourir.grid(row=5,column=1,padx=5,pady=5,sticky=E)

b1 = Button(fen,text="Valider",command=valider,width=10,fg='white',bg="#0a89c0")
b2 = Button(fen,text="Reinitialiser",command=reinitialiser,width=10, fg='white',bg="#0a89c0")
b3 = Button(fen,text="Voir la liste",command=lambda: listeInscrit(fen,listePersonne),fg='white',bg="#0a89c0")

b1.grid(row=6,column=0,pady=5)
b2.grid(row=7,column=0,pady=5)
b3.grid(row=8,column=0,pady=5)

contenu.grid(row=0,column=0,padx=5,pady=5)

fen.mainloop()









