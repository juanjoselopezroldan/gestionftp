# -*- coding: utf-8 -*-
import sys
import os
import crypt

#Para empezar crearemos el usuario/departamento con su clave
usuario=str(raw_input("Introduce el nombre de departamento que sera a su vez el de usuario: "))
clave=str(raw_input("Introduce clave del usuario: "))

#Cifraremos la clave que hemos generado
alfabeto="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
encpass=crypt.crypt(clave,alfabeto)

#Creamos el usuario con su respectiva clave
os.system("useradd "+usuario+" -p "+encpass)

#Crearemos el directorio del virtualhost para asi poder almacenar el contenido en ese directorio
os.system("mkdir /srv/"+usuario)
os.system("chown -R "+usuario+". /srv/"+usuario)

#Creamos el contenido que vamos a añadir en el virtualhost
virtualhost=["Alias /"+usuario+" /srv/ftp/"+usuario+"\n",
			"<Directory /srv/"+usuario+"/> \n"
			"	Options +Indexes +SymLinksIfOwnerMatch \n"
			"	AllowOverride None\n"
			"	Require all granted\n"
			"</Directory>\n"
			"</VirtualHost>\n"]

#Eliminamos la ultima linea del virtualhost para añadir el nuevo contenido
os.system("sed -i '$d' /etc/apache2/sites-available/ftp.conf")

#Abrimos el fichero y con la opcion "a" indicamos que vamos a escribir al final de archivo y añadimos el contenido al fichero del virtualhost
datos=open('/etc/apache2/sites-available/ftp.conf',"a")
datos.writelines(virtualhost)
datos.close()

#Añadimos en el fichero de configuracion del servicio ftp la linea que indicar la ruta del DocumentRoot para que asi el usuario pueda iniciar sesion en su sitio FTP
ruta=["DefaultRoot			/srv/ftp/"+usuario+" "+usuario+"\n"]
ftp=open('/etc/proftpd/proftpd.conf',"a")
ftp.writelines(ruta)
ftp.close()

#Creacion del directorio para que pueda guardar la informacion el usuario de ese espacio ftp y ademas de ello se le asigna los permisos necesarios para que ese usuario pueda escribir en el directorio
os.system("mkdir /srv/ftp/"+usuario)
os.system("chown "+usuario+":"+usuario+" -R /srv/ftp/"+usuario)

#Reiniciamos los servicios para aplicar los cambios
os.system("service apache2 restart")
os.system("service proftpd restart")

print "La creacion del departamento se ha realizado correctamente"