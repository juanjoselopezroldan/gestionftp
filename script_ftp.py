# -*- coding: utf-8 -*-
import sys
import os

usuario=str(raw_input("Introduce el nombre de departamento que sera a su vez el de usuario: "))
clave=str(raw_input("Introduce clave del usuario: "))

os.system("useradd "+usuario+" -p "+clave+"")
print "La creacion se ha realizado correctamente"