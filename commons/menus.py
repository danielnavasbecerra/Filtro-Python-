from commons.utils import validar_opcion

def menu_principal():
    print("------ Sistema Gestor de Peliculas BlockBuster ------")
    print("1. Administrador de Generos")
    print("2. Administrador de Actores")
    print("3. Administrador de formatos")
    print("4. Gestor de peliculas")
    print("5. Gestor de informes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op


def menu_gestor_generos():
    print("----------- Gestor de Generos -----------")
    print("1. Crear genero")
    print("2. Listar generos")
    print("3. Ir Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op
    

def menu_gestor_actores():
    print("----------- Gestor de Actores -----------")
    print("1. Crear Actor")
    print("2. Listar Actor")
    print("3. Ir Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op


def menu_gestor_formatos():
    print("----------- Gestor de Formatos -----------")
    print("1. Crear formatos")
    print("2. Listar formatos")
    print("3. Ir Menu principal")
    op=validar_opcion("Opcion: ",1,3)
    return op


def menu_gestor_peliculas():
    print("----------- Gestor de Peliculas -----------")
    print("1. Agregar pelicula")
    print("2. Editar pelicula")
    print("3. Eliminar pelicula")
    print("4. Eliminar Actor")
    print("5. Buscar pelicula")
    print("6. Listar todas peliculas")
    print("7. Menu principal")
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_modificar_peliculas():
    print("----------- Modificar Peliculas -----------")
    print("1. ID")
    print("2. Nombre")
    print("3. Duracion")
    print("4. Sinopsis")
    print("5. Genero")
    print("6. Actor")
    print("7. Formato")
    print("8. Regresar al gestor de Peliculas")
    op=validar_opcion("Opcion: ",1,8)
    return op



def menu_gestor_informes():
    print("----------- Gestor de Informes -----------")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Listar las peliculas donde el protagonista sea Silvester Stallone")
    print("3. Buscar pelicula y mostrar la sinopsis y los actores")
    print("4. Ir menu principal")
    op=validar_opcion("Opcion: ",1,4)
    return op