#!/usr/bin/python
#!encoding:UTF-8
def aproximacion (nn):
  n =int(nn)
  sumatorio = 0.0
  for i in range (1, n+1):
    xi = (i-0.5)/float(n)
    fxi = 4/(1 + (xi**2))
    sumatorio += fxi
  c = sumatorio/float(n)
  return c

if __name__=="__main__":
  from math import pi 
  print 'El valor de PI con 35 decimales: %.35f\n' % pi 
  
  import sys
  
  if (len(sys.argv) == 3):
    intervalo = int (sys.argv[1])
    veces = int (sys.argv[2])
  else:  
    print 'Es necesario adjuntar en la línea de comando un entero que determine el número de intervalos deseados y otro para el número de veces:'
    print 'nombre.py intervalo veces'
    intervalo = 10
    veces = 10
  while intervalo <= 0:
    print 'No se puede calcular PI aproximado con el intervalo introducido'
    intervalo = int (raw_input('Introduzca un nuevo intervalo: '))
  l = []
  print 'i.                 PI35DT                                lista i                                PI35DT - lista i' 
  print '\n'
  for vez in range (1, veces+1):
    x = aproximacion (intervalo*vez)
    l = l + [x]
    dif = abs(pi - x)
    print '%d.  %.35f  %.35f  %.35f' % (vez, pi, x, dif)
  print '\n'
  print l