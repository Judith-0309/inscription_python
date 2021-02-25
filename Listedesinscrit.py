from tkinter import  *
from PIL import Image, ImageTk

def listeInscrit(fenetre,liste):
    newFen = Toplevel(fenetre)
    newFen.geometry("400x400")
    newFen.title("Liste des inscrits")

    listeCan = Canvas(newFen,bg="#0a89c0")
    fontLabel = 'arial 11 bold'

    resultat = Label(listeCan, text="Liste des inscrits: ", font = fontLabel, fg='#0a89c0', bg='white')
    prenom = Label(listeCan, text="prenom",width=15, font = fontLabel, fg='white', bg="#0a89c0")
    nom = Label(listeCan, text="nom",width=6, font = fontLabel, fg='white', bg="#0a89c0")
    email = Label(listeCan, text=" email",width=6,font = fontLabel, fg='white', bg="#0a89c0")
    adresse = Label(listeCan, text="adresse",width=6,font = fontLabel, fg='white', bg="#0a89c0")
    photo = Label(listeCan, text="photo",width=12, font = fontLabel, fg='white', bg="#0a89c0")  
    status = Label(listeCan, text="Aucun inscrit pour le moment", font = 'arial 9 bold', fg='white', bg="#0a89c0")


    listeCan.grid(row=0,column=0)
    resultat.grid(row=0,column=0, columnspan=3)
    photo.grid(row=1,column=0,padx=5,pady=5)
    prenom.grid(row=1,column=1,padx=5,pady=5)
    nom.grid(row=1,column=2,padx=5,pady=5)
    email.grid(row=1,column=3,padx=5,pady=5)
    adresse.grid(row=1,column=4,padx=5,pady=5) 
    status.grid(row=2,column=0,columnspan=3)   


    if liste:
        li=2
        for p in  liste:
            photoLab =  Label(listeCan, height=50)
            img = Image.open(p.photo)
            img = img.resize((80,80),Image.ANTIALIAS)
            photoLab.img = ImageTk.PhotoImage(img)
            photoLab.configure(image=photoLab.img) 

            pre = Label(listeCan, text=p.prenom, font = fontLabel, fg='white', bg="#0a89c0")
            nom = Label(listeCan, text=p.nom, font = fontLabel, fg='white', bg="#0a89c0")
            ema = Label(listeCan, text=p.email, font = fontLabel, fg='white', bg="#0a89c0")
            adr = Label(listeCan, text=p.adresse, font = fontLabel, fg='white', bg="#0a89c0")

            photoLab.grid(row =li, column = 0,pady=2)
            pre.grid(row = li, column = 1)
            nom.grid(row= li, column = 2)
            ema.grid(row= li, column = 3)
            adr.grid(row= li, column = 4)
            listeCan.create_line(9,55,355,55,width=1,fill='white')

            li+=1 

            status.configure(text="{}  inscrits pour le moment".format(len(liste)))
            status.grid(row=li,column=0,columnspan =3,pady =2)

    newFen.mainloop()        





