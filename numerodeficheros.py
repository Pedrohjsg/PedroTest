#Pedir para introducir una letra y listar los archivos com esa letra

import os
ficheros=os.listdir("c:\windows\system32")
letra=raw_input("Introduz una letra: ")
cuantos=0
for x in ficheros:
	if x.count(letra)>0:
		#print x
		cuantos=cuantos+1

print " "
print "Hay "+str(cuantos)+" ficheros con "+str(letra)
	