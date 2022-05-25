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

arch_jugador = open("data/datos_jugadores.txt", "r")
jugador = arch_jugador.readlines()

for j in jugador:
        equipo = session.query(Club).filter_by(nombre = j.split(";")[0]).one()
        posicion = j.split(";")[1]
        dorsal = j.split(";")[2]
        nombre = j.split(";")[3].replace("\n","")

        jugadores = Jugador(nombre = nombre, dorsal = dorsal,posicion = posicion, club = equipo)
        session.add(jugadores)

session.commit()



