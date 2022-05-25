from mailbox import NoSuchMailboxError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

arch_club = open("data/datos_clubs.txt", "r")
clubes = arch_club.readlines()

for r in clubes:
        name = r.split(";")[0]
        depor = r.split(";")[1]
        fundation = r.split(";")[2].replace("\n","")
        clubs = Club(nombre = name, deporte = depor,fundacion = fundation)
        session.add(clubs)

session.commit()

