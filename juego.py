import random

def ahorcado():
  print("""
  ¡Bienvenido al juego del Ahorcado!
  Las reglas son simples:
  -1. Tienes 6 intentos para adivinar la palabra.
  -2. Si adivinas una letra, se mostrará en la pantalla.
  -3. Si no adivinas una letra, se te restará un intento.
  -4. Si adivinas la palabra, ¡ganas!
  -5. Si te quedas sin intentos, pierdes.
  """)

  palabras = ["python", "javascript", "programacion", "computadora", "ciencia"]
  palabra_secreta = random.choice(palabras)
  letras_en_palabra = set(palabra_secreta)  # Letras en la palabra
  alfabeto = set(chr(x) for x in range(ord('a'), ord('z') + 1))  # Todas las letras del alfabeto
  letras_usadas = set()  # Letras que el usuario ha adivinado

  vidas = 6
  print("""
  ______________
  |            |                              
  |            o              
  |           /|\                   
  |           / \                           
  |                     
  --------------
     """)

  # Bucle principal del juego
  while len(letras_en_palabra) > 0 and vidas > 0:
    # Dibujo del ahorcado
    print("\n" * 2)

    if vidas == 5:
      print("""
     ______________
     |            |                                  
     |            o              
     |           /|\                   
     |           /                           
     |                     
     ---------------
    """)
    if vidas == 4:
      print("""
      ______________
      |            |                                  
      |            o              
      |           /|\                  
      |                                     
      |                     
      ---------------""")
    if vidas == 3:
      print("""
      ______________
      |            |                                  
      |            o              
      |           /|                  
      |                                      
      |                     
      ---------------
      """)
    if vidas == 2:
     print("""
     ______________
     |            |                                  
     |            o              
     |                             
     |                                      
     |                     
     ---------------
     """)
    if vidas == 1:
      print("""
      ______________
      |            |                                  
      |            o              
      |                             
      |                                      
      |                     
      ---------------
      """)


    # Letras usadas
    print("Te quedan", vidas, "vidas y has usado estas letras: ", " ".join(letras_usadas))

    # Palabra actual (e.g. "p - t - o -")
    letras_mostradas = [letra if letra in letras_usadas else '-' for letra in palabra_secreta]
    print('Palabra actual: ', ' '.join(letras_mostradas))

    letra_adivinada = input('Adivina una letra: ').lower()
    if letra_adivinada in alfabeto - letras_usadas:
      letras_usadas.add(letra_adivinada)
      if letra_adivinada in letras_en_palabra:
        letras_en_palabra.remove(letra_adivinada)
        print("")

      else:
        vidas -= 1  # Resta una vida si la letra está mal
        print('La letra no está en la palabra.')

    elif letra_adivinada in letras_usadas:
      print("Ya has usado esa letra. Intenta otra vez.") 

  # El bucle se ha detenido, el jugador ganó o perdió
  if vidas == 0:
    print("""¡Te has quedado sin vidas!
    ______________
     |            |                         
     |                          
     |                             
     |                                      
     |                     
     ---------------"""
    '¡Te has quedado sin vidas! La palabra era', palabra_secreta)
  else:
    print('¡Felicidades! Has adivinado la palabra', palabra_secreta)

