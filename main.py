from commons.utils import limpiar_pantalla,salir
from commons.menus import menu_principal,menu_gestor_generos,menu_gestor_actores,menu_gestor_formatos,menu_gestor_peliculas,menu_gestor_informes
from businnes.generos import crear_generos,listar_generos
from businnes.actores import crear_actores,listar_actores
from businnes.formatos import crear_formatos,listar_formatos
from businnes.peliculas import agregar_peliculas,editar_pelicula,eliminar_pelicula,eliminar_actor,buscar_pelicula,listar_peliculas
from businnes.informes import listar_pelicula_genero_especifico,listar_pelicula_actor_especifico,buscar_pelicula_mostrando_sinopsis_actores

# funtions
def generos():
    limpiar_pantalla()
    op=menu_gestor_generos()
    if op==1:
       crear_generos()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       generos()
    elif op==2:
       listar_generos()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       generos()


def actores():
    limpiar_pantalla()    
    op=menu_gestor_actores()
    if op==1:
        crear_actores()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        actores()
    elif op==2:
        listar_actores()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        actores()

        
def formatos():
    limpiar_pantalla()    
    op=menu_gestor_formatos()
    if op==1:
        crear_formatos()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        formatos()
    elif op==2:
        listar_formatos()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        formatos()


def peliculas():
    limpiar_pantalla()    
    op=menu_gestor_peliculas()
    if op==1:
        agregar_peliculas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()
    elif op==2:
        editar_pelicula()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()
    elif op==3:
        eliminar_pelicula()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()
    elif op==4:
        eliminar_actor()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()
    elif op==5:
        buscar_pelicula()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()
    elif op==6:
        listar_peliculas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        peliculas()

        
def informes():
    limpiar_pantalla()    
    op=menu_gestor_informes()
    if op==1:
        listar_pelicula_genero_especifico()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        informes()
    elif op==2:
        listar_pelicula_actor_especifico()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        informes()
    elif op==3:
        buscar_pelicula_mostrando_sinopsis_actores()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        informes()

    
#start
while True: 
    limpiar_pantalla()
    op=menu_principal()
    if  op==1:
       generos()
    elif op==2:
       actores()
    elif op==3:
       formatos()
    elif op==4:
       peliculas()
    elif op==5:
       informes()
    elif op==6:
       print("\nSaliendo...")
       salir()
       break