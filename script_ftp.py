# -*- coding: utf-8 -*-
import sys
import os
import random
import crypt

usuario=str(raw_input("Introduce el nombre de departamento que sera a su vez el de usuario: "))
clave=str(raw_input("Introduce clave del usuario: "))

salt=getsalt()
encpass=crypt.crypt(clave,salt)

os.system("useradd "+usuario+" -p "+encpass)
print "La creacion se ha realizado correctamente"