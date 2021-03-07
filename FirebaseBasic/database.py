# from itertools import chain 
database={
"RKI-2536"          :(2200, "scanner"),
str(7622201423216)  :(235,  "bournvita"),
str(261459)         :(100,  "nut"),
str(69606800395)    :(937,  "electronic comp"),
str(5060214370240)  :(4500,  "RPI"),
str(69659265885)    :(945,   "Robu.in"),
"Z36798373"         :(1500,  "Hand Sanitizer")
}
res = [ele for value in database for ele in value] 
print((ele))