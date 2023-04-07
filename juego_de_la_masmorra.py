import random

print("Juego Epicardo \n"
      "-------------- \n"
      "\n"
      "En un reino lejado hay una misteriosa masmorra que se dice que está llena de tesoros \n"
      "y peligros mortales. Muchos aventurreros ha intentado entrar, pero pocos lograron \n"
      "salir con vida y menos aún con riquezas\n"
      "tu y tu compaero de aventura acaban de inciar una nueva aventura dentro de la masmorra \n"
      "para encontrar los tesoros que abundan en su interior \n"
      "\n"
      "Justo al entrar se encuentarn un dos caminos, uno a la dercha y otro a la izquierda \n"
      "\n"
      "¿a cual escogeran?")

opcion = input("OPCION(A) - Lado Derecho / OPCION (B) - Lado Izquierdo: ")

if opcion == "B":
      print("Se dan media vuelta y salen corriendo escapando hacia la entrada de la masmorra. \n"
            "Fin del Juego")
if opcion == "A":
      print("Inician su camnino por el lado derecho\n"
            "y a los pocos pasos se encuentran a los guardias esqueleticos\n"
            "¿Que hacen?")
      opcion = input("OPCION(A) - Se regresan a la entrada / OPCION (B) - Luchan contra los guardias: ")

      if opcion == "A":
            print("Salen corriendo hacia la entrada gritando, caen en las trampas activadas\n"
                  "por los guardias y mueren\n"
                  "Fin del Juego")
      elif opcion == "B":
            print("Sacan sus espadas y escudos y comienza la batalla\n"
                  "Golpes, esquivos y una gran primera victoria contra los desafios de esta aventura. "
                  "Siguen adelante y se percata que los guardias al morir arrojan diamantes"
                  "¿Los agarra?")
            opcion = input("OPCION(A) - Si / OPCION (B) - NO: ")

            if opcion == "A":
                  print("Agarran los diamantes y siguen su rumbo, hay dos caminos para seguir"
                        "uno para arriba y otro para la derecha, cual escogen")

                  opcion = input("OPCION(A) - Hacia arriba / OPCION (B) - A la derecha: ")

                  if opcion == "A":
                        print("Comienzan a subir la escalera de huesos"
                              "al llegar se encuentra con un duende con una cubeta llena de oro")

                        numero_ganador = random.randint(1,5)
                        numero_elegido = int(input("El duende les hace una pregunta"
                                                   "¿del 1 al 5 en que número estoy pensando?"))

                        if numero_elegido == numero_ganador:
                              print("Así es, lo han logrado, tienen derecho de llevarse mi cubeta de oro"
                                    "y seguir adelante, mucha suerte!")

                        print("JA JA JA, ahora morirán porque el número en el que estaba pensado es: {}".format(numero_ganador))
                        print("Fin del Juego")

                  if opcion == "B":
                        print("Caminan hacia la derecha y al final del oscuro pasillo se encuentran con"
                              "el tesoro soñado y encuentran la salida para salir con vida de la masmorra.\n"
                              "Fin de Juego")

