# -*- coding: utf-8 -*-
import sys
import os
import crypt

#Para empezar crearemos el usuario/departamento con su clave
usuario=str(raw_input("Introduce el nombre de departamento que sera a su vez el de usuario: "))
clave=str(raw_input("Introduce clave del usuario: "))

#Cifraremos la clave que hemos generado
alfabeto="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#clave=clave.join([choice(alfabeto) for i in range(8)])
encpass=crypt.crypt(clave,alfabeto)

#Creamos el usuario con su respectiva clave
os.system("useradd "+usuario+" -p "+encpass)
print "La creacion se ha realizado correctamente"

#Crearemos el directorio del virtualhost para asi poder almacenar el contenido en ese directorio
os.system("mkdir /srv/"+usuario)
os.system("chown -R "+usuario+". /srv/"+usuario)
#Añadimos el contenido al fichero del virtualhost
fichero