from firebase import firebase

Suyash = firebase.FirebaseApplication('https://myproject1-218e6-default-rtdb.firebaseio.com/', None)

database={
"RKI-2536"          :(2200, "scanner"),
str(7622201423216)  :(235,  "bournvita"),
str(261459)         :(100,  "nut"),
str(69606800395)    :(937,  "electronic_comp"),
str(5060214370240)  :(4500,  "RPI"),
str(69659265885)    :(945,   "Robu.in"),
"Z36798373"         :(1500,  "Hand Sanitizer")
}

temprature = int(input("Enter:  "))
data_to_upoload = {
        'Temp' : temprature
}

Suyash.post("Suyash/", data_to_upoload)
