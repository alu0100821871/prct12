#!/usr/bin/python
#!encoding:UTF-8
import modulo
import time
import timeit

def error (intervalo, n_test, umbral):
  
  fallos = 0
  for i in range(n_test):
    apr = modulo.aproximacion (intervalo)
    diferencia = abs(modulo.PI - apr)
    if (diferencia > umbral):
      fallos += 1
  
  porcentaje = (float(fallos)/float(n_test))*100
  return porcentaje

if __name__=="__main__":
  
  n = int (raw_input('Introduzca un intervalo: '))
  umbral = [1, 0.1, 0.001, 0.0001, 0.00001]
  veces = len(umbral)
  lista = []
  tiempos = []
  for i in range (len(umbral)):
    t0 = time.time()
    umb = umbral[i]
    valores =  error (n, veces, umb)
    lista = lista + [valores]
    tf = time.time()
    tiempos = tiempos + [tf-t0]
  print lista
  print tiempos
  print 'Introduzca el nombre del fichero donde se almacenarán los resultados:'
  nombre = raw_input();
  f=open(nombre,'w')
  f.write('Los tiempos son:')
  for j in tiempos:
    f.write(str(tiempos[j]) + '\n')
  
  f.close()
  

  