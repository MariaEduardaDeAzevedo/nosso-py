from os import system, name
import time
from random import randrange

def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def ascend_print(palavra, contador):
  print(f'{palavra[:contador]}_')
  time.sleep(0.1)
  clear()
  print(f'{palavra[:contador]}')
  time.sleep(0.1)
  clear()
  print(f'{palavra[:contador]}_')
  time.sleep(0.3)
  clear()

  return contador + 1

def descend_print(palavra, contador):
  print(f'{palavra[:contador]}_')
  time.sleep(0.1)
  clear()
      
  return contador - 1

OLAS = [
  'Hello World!!!',
  'Olá Mundo!!!',
  'Bonjour le monde',
  'Hola mundo',
  'Привет, мир',
  'Hallo LOAC',
  'Dia duit an Domhan',
  'שלום עולם',
  '你好，世界'
]

METODOS_PRINT = {
  "ascend" : ascend_print,
  "descend" : descend_print,
}

def define_palavra_nova():
  palavra_index = randrange(len(OLAS))
  return OLAS[palavra_index]

def cria_animacao():
  contador = 0
  metodo_print = "ascend"

  palavra = define_palavra_nova()
  tamanho = len(palavra)

  while(True):
    contador = METODOS_PRINT[metodo_print](palavra, contador)

    if (contador - 1 == tamanho):
      metodo_print = "descend"

    if (contador == 0):
      palavra = define_palavra_nova()
      tamanho = len(palavra)
      metodo_print = "ascend"
    

if __name__ == "__main__":
  cria_animacao()
