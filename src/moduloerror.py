#!/usr/bin/python
#!encoding:UTF-8
import modulo

def error (intervalo, n_test, umbral):
  
  fallos = 0
  for i in range(n_test):
    apr = modulo.aproximacion (intervalo)
    diferencia = abs(modulo.aproximacion - apr)
    if (diferencia > umbral):
      fallos += 1
  
  porcentaje = (float(fallos)/float(n_test))*100
  return porcentaje

if __name__=="__main__":
  
  import sys
  
  if (len(sys.argv) == 4):
    intervalo = int (sys.argv[1])
    n_test = int (sys.argv[2])
    umbral = int (sys.argv[3])
  else:  
    print 'Es necesario adjuntar en la línea de comando un entero que determine el número de intervalos deseados, el número de veces y  el umbral:'
    print 'nombre.py intervalo n_test umbral'
    intervalo = 10
    n_test = 10
    umbral = 0.000001
  while intervalo <= 0:
    print 'No se puede calcular PI aproximado con el intervalo introducido'
    intervalo = int (raw_input('Introduzca un nuevo intervalo: '))


  