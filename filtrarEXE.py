#sacar todos los .exe del system32
import os
lista=os.listdir("c:\windows\system32")

for y in lista:
	if y[-3:]=="exe":
		print y