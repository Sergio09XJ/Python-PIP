#Este es un programa que simula el juego de papel peidra y tiejras. 
import random 


print("\n ------------------------ PIEDRA | PAPEL | TIJERA -------------------------- ")
nombre = input("\n-¿Cual es tu Nombre? ")

def datos(nombre):
  
   ataque_u = input("\n-Dame tu movimiento " + nombre+": ")
   ataque_u = ataque_u.capitalize()

   while ataque_u != "Piedra" and ataque_u != "Papel" and ataque_u != "Tijera":
      print("\n-Tu ataque esta mal escrito o no es parte del juego")
      ataque_u = input("-Damelo de nuevo: ")
      ataque_u = ataque_u.capitalize()

   return ataque_u   



def maquina():

   eleccion_m = random.randint(1,3)
   if  eleccion_m == 1:
      ataque_m = "Piedra"
   elif eleccion_m == 2:
      ataque_m = "Papel"
   else: 
      ataque_m = "Tijera"  

   return ataque_m

def pelea():
   cont_u = 0
   cont_m = 0
    
   for i in range(0,3):


       print("\n")
       print("\n "+str(i+1)+"º Asalto -----------------")
       golpe_u = datos(nombre)
       golpe_m = maquina()

       print("-La Maquina eligió: "+ golpe_m)

       if golpe_u == golpe_m:
         print("(-----"+golpe_u + "|" + golpe_m+"-----)")
         print("\n"+nombre + " tuviste un empate con la Maquina.")
         cont_u += 1
         cont_m += 1
       elif golpe_u == "Piedra" and golpe_m == "Tijera" or golpe_u == "Tijera" and golpe_m == "Papel" or golpe_u == "Papel" and golpe_m == "Piedra": 
         print("(-----"+golpe_u + "|" + golpe_m+"-----)")
         print("\n" +nombre + " le ganaste a la Maquina.")
         cont_u += 1
       else:
         print("(-----"+golpe_u + "|" + golpe_m+"-----)")
         print("\n" +"La Maquina te gano " + nombre)   
         cont_m += 1
       print("------------------------------------")
      
   return cont_u, cont_m
   

golpes_u,golpes_m  = pelea()

def ganador(golpes_u,golpes_m): 
  if golpes_u == golpes_m: 
     print("\n")
     print("\n ---------- ¡Tuvsite un Empate con la Maquina! ---------- ")
     print("              "+  nombre + " > " + str(golpes_u) + " | " + str(golpes_m) + " < " + "Maquina" )
  elif golpes_u > golpes_m: 
     print("\n")
     print("\n     ---------- ¡Le ganaste a la Maquina! ----------      ")
     print("                  "+  nombre + " > " + str(golpes_u) + " | " + str(golpes_m) + " < " + "Maquina" )
  else: 
     print("\n")
     print("\n   ---------- ¡Perdiste contra la Maquina! ----------     ")
     print("                "+  nombre + " > " + str(golpes_u) + " | " + str(golpes_m) + " < " + "Maquina" )   

ganador(golpes_u,golpes_m)
print("\n")




   
    



