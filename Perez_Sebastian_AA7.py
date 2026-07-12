# Sistema de gestión y análisis de un centro deportivo escolar


def pedir_entero(mensaje, minimo, maximo):
    """Solicita un número entero dentro de un rango permitido."""
    valido = False

    # Repite la pregunta hasta que el usuario ingrese un valor correcto.
    while valido == False:
        texto = input(mensaje)

        if texto.isdigit():
            numero = int(texto)

            if numero >= minimo and numero <= maximo:
                valido = True
            else:
                print("Error: ingrese un número entre", minimo, "y", maximo)
        else:
            print("Error: debe ingresar un número entero.")

    return numero


def pedir_texto(mensaje):
    """Solicita un texto que no puede estar vacío."""
    texto = ""

    # Se repite mientras el usuario no escriba información.
    while texto == "":
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: este dato no puede quedar vacío.")

    return texto


def buscar_fila_por_id(matriz, identificador):
    """Busca un identificador en la primera columna de una matriz."""
    posicion = -1

    # Recorre cada fila hasta encontrar el identificador solicitado.
    for indice in range(len(matriz)):
        if matriz[indice][0] == identificador:
            posicion = indice

    return posicion


def registrar_actividad(actividades, uso_semanal, asignacion, asistencia_semanal):
    """Registra una actividad y crea sus filas relacionadas."""
    identificador = pedir_entero("Identificador de la actividad: ", 1, 9999)

    if buscar_fila_por_id(actividades, identificador) != -1:
        print("Error: ya existe una actividad con ese identificador.")
    else:
        nombre = pedir_texto("Nombre de la actividad: ")
        categoria = ""

        while categoria != "Individual" and categoria != "Colectiva":
            categoria = pedir_texto("Categoría (Individual/Colectiva): ")
            categoria = categoria.capitalize()

            if categoria != "Individual" and categoria != "Colectiva":
                print("Error: escriba Individual o Colectiva.")

        actividades.append([identificador, nombre, categoria])

        # Se crean filas con cero para relacionar la actividad con las otras matrices.
        uso_semanal.append([identificador, 0, 0, 0, 0, 0])
        asignacion.append([identificador, 0])
        asistencia_semanal.append([identificador, 0, 0, 0, 0, 0])

        print("Actividad registrada correctamente.")


def insertar_actividad(actividades, uso_semanal, asignacion, asistencia_semanal):
    """Inserta una actividad en la posición indicada por el usuario."""
    identificador = pedir_entero("Identificador de la actividad: ", 1, 9999)

    if buscar_fila_por_id(actividades, identificador) != -1:
        print("Error: ya existe una actividad con ese identificador.")
    else:
        nombre = pedir_texto("Nombre de la actividad: ")
        categoria = ""

        while categoria != "Individual" and categoria != "Colectiva":
            categoria = pedir_texto("Categoría (Individual/Colectiva): ")
            categoria = categoria.capitalize()

            if categoria != "Individual" and categoria != "Colectiva":
                print("Error: escriba Individual o Colectiva.")

        posicion = pedir_entero(
            "Posición donde desea insertar la actividad: ", 0, len(actividades)
        )

        # insert() coloca las filas en la misma posición de todas las matrices.
        actividades.insert(posicion, [identificador, nombre, categoria])
        uso_semanal.insert(posicion, [identificador, 0, 0, 0, 0, 0])
        asignacion.insert(posicion, [identificador, 0])
        asistencia_semanal.insert(posicion, [identificador, 0, 0, 0, 0, 0])

        print("Actividad insertada correctamente.")


def registrar_entrenador(entrenadores):
    """Registra un entrenador con su nombre y experiencia."""
    identificador = pedir_entero("Identificador del entrenador: ", 1, 9999)

    if buscar_fila_por_id(entrenadores, identificador) != -1:
        print("Error: ya existe un entrenador con ese identificador.")
    else:
        nombre = pedir_texto("Nombre del entrenador: ")
        experiencia = pedir_entero("Años de experiencia: ", 0, 80)

        entrenadores.append([identificador, nombre, experiencia])
        print("Entrenador registrado correctamente.")


def registrar_material(material, stock_material):
    """Registra un material deportivo y sus cantidades iniciales."""
    identificador = pedir_entero("Identificador del material: ", 1, 9999)

    if buscar_fila_por_id(material, identificador) != -1:
        print("Error: ya existe un material con ese identificador.")
    else:
        nombre = pedir_texto("Nombre del material: ")
        tipo = ""

        while tipo != "Consumible" and tipo != "Reutilizable":
            tipo = pedir_texto("Tipo (Consumible/Reutilizable): ")
            tipo = tipo.capitalize()

            if tipo != "Consumible" and tipo != "Reutilizable":
                print("Error: escriba Consumible o Reutilizable.")

        total = pedir_entero("Stock total: ", 0, 9999)
        en_uso = pedir_entero("Cantidad de material en uso: ", 0, total)

        material.append([identificador, nombre, tipo])
        stock_material.append([identificador, total, en_uso])
        print("Material registrado correctamente.")


def asignar_entrenador(actividades, entrenadores, asignacion):
    """Asigna un entrenador existente a una actividad existente."""
    id_actividad = pedir_entero("Identificador de la actividad: ", 1, 9999)
    posicion_actividad = buscar_fila_por_id(actividades, id_actividad)

    if posicion_actividad == -1:
        print("Error: la actividad no existe.")
    else:
        id_entrenador = pedir_entero("Identificador del entrenador: ", 1, 9999)
        posicion_entrenador = buscar_fila_por_id(entrenadores, id_entrenador)

        if posicion_entrenador == -1:
            print("Error: el entrenador no existe.")
        else:
            posicion_asignacion = buscar_fila_por_id(asignacion, id_actividad)

            # Se cambia la segunda columna de la fila de asignación.
            asignacion[posicion_asignacion][1] = id_entrenador
            print("Entrenador asignado correctamente.")


def registrar_material_para_actividad(actividades, material, material_por_actividad):
    """Indica qué cantidad de material necesita una actividad."""
    id_actividad = pedir_entero("Identificador de la actividad: ", 1, 9999)

    if buscar_fila_por_id(actividades, id_actividad) == -1:
        print("Error: la actividad no existe.")
    else:
        id_material = pedir_entero("Identificador del material: ", 1, 9999)

        if buscar_fila_por_id(material, id_material) == -1:
            print("Error: el material no existe.")
        else:
            cantidad = pedir_entero("Cantidad necesaria por actividad: ", 1, 9999)
            encontrado = False

            # Revisa si la actividad ya tenía registrado ese mismo material.
            for fila in material_por_actividad:
                if fila[0] == id_actividad and fila[1] == id_material:
                    fila[2] = cantidad
                    encontrado = True

            if encontrado == False:
                material_por_actividad.append([id_actividad, id_material, cantidad])

            print("Material relacionado con la actividad correctamente.")


def realizar_actividad(actividades, uso_semanal, material_por_actividad, stock_material):
    """Registra una actividad si cuenta con todos los materiales necesarios."""
    id_actividad = pedir_entero("Identificador de la actividad: ", 1, 9999)

    if buscar_fila_por_id(actividades, id_actividad) == -1:
        print("Error: la actividad no existe.")
    else:
        tiene_material = False
        material_suficiente = True

        # Primero se revisan todos los materiales sin modificar el stock.
        for fila in material_por_actividad:
            if fila[0] == id_actividad:
                tiene_material = True
                posicion_stock = buscar_fila_por_id(stock_material, fila[1])

                if posicion_stock == -1:
                    material_suficiente = False
                else:
                    disponible = stock_material[posicion_stock][1] - stock_material[posicion_stock][2]

                    if disponible < fila[2]:
                        material_suficiente = False

        if tiene_material == False:
            print("Error: esta actividad no tiene materiales registrados.")
        elif material_suficiente == False:
            print("Error: no existe material suficiente para realizar la actividad.")
        else:
            dia = pedir_entero("Día (1=Lun, 2=Mar, 3=Mié, 4=Jue, 5=Vie): ", 1, 5)

            # Ahora se aumenta el material en uso porque sí hay disponibilidad.
            for fila in material_por_actividad:
                if fila[0] == id_actividad:
                    posicion_stock = buscar_fila_por_id(stock_material, fila[1])
                    stock_material[posicion_stock][2] = stock_material[posicion_stock][2] + fila[2]

            posicion_uso = buscar_fila_por_id(uso_semanal, id_actividad)
            uso_semanal[posicion_uso][dia] = uso_semanal[posicion_uso][dia] + 1
            print("Actividad realizada y material actualizado correctamente.")


def registrar_asistencia_semanal(actividades, asistencia_semanal):
    """Registra la asistencia de una actividad en un día de la semana."""
    id_actividad = pedir_entero("Identificador de la actividad: ", 1, 9999)

    if buscar_fila_por_id(actividades, id_actividad) == -1:
        print("Error: la actividad no existe.")
    else:
        dia = pedir_entero("Día (1=Lun, 2=Mar, 3=Mié, 4=Jue, 5=Vie): ", 1, 5)
        asistentes = pedir_entero("Cantidad de estudiantes asistentes: ", 0, 9999)
        posicion = buscar_fila_por_id(asistencia_semanal, id_actividad)

        # El día elegido corresponde a la columna donde se guarda la asistencia.
        asistencia_semanal[posicion][dia] = asistentes
        print("Asistencia registrada correctamente.")


def mostrar_actividades_disponibles(actividades, material_por_actividad, stock_material):
    """Muestra las actividades que cuentan con material suficiente."""
    hay_disponibles = False
    print("\nACTIVIDADES DISPONIBLES")

    for actividad in actividades:
        id_actividad = actividad[0]
        tiene_material = False
        suficiente = True

        # Revisa todos los materiales que necesita la actividad actual.
        for fila in material_por_actividad:
            if fila[0] == id_actividad:
                tiene_material = True
                posicion_stock = buscar_fila_por_id(stock_material, fila[1])

                if posicion_stock == -1:
                    suficiente = False
                else:
                    disponible = stock_material[posicion_stock][1] - stock_material[posicion_stock][2]

                    if disponible < fila[2]:
                        suficiente = False

        if tiene_material == True and suficiente == True:
            print("ID:", actividad[0], "-", actividad[1], "-", actividad[2])
            hay_disponibles = True

    if hay_disponibles == False:
        print("No hay actividades disponibles con material suficiente.")


def mostrar_matriz(titulo, matriz):
    """Muestra todas las filas de una matriz con un título."""
    print("\n" + titulo)

    if len(matriz) == 0:
        print("No existen datos registrados.")
    else:
        for fila in matriz:
            print(fila)


def modificar_actividad(actividades):
    """Modifica el nombre o la categoría de una actividad."""
    identificador = pedir_entero("Identificador de la actividad: ", 1, 9999)
    posicion = buscar_fila_por_id(actividades, identificador)

    if posicion == -1:
        print("Error: la actividad no existe.")
    else:
        print("1. Modificar nombre")
        print("2. Modificar categoría")
        opcion = pedir_entero("Seleccione una opción: ", 1, 2)

        if opcion == 1:
            nuevo_nombre = pedir_texto("Nuevo nombre: ")
            actividades[posicion][1] = nuevo_nombre
        else:
            nueva_categoria = ""

            while nueva_categoria != "Individual" and nueva_categoria != "Colectiva":
                nueva_categoria = pedir_texto("Nueva categoría (Individual/Colectiva): ")
                nueva_categoria = nueva_categoria.capitalize()

                if nueva_categoria != "Individual" and nueva_categoria != "Colectiva":
                    print("Error: escriba Individual o Colectiva.")

            actividades[posicion][2] = nueva_categoria

        print("Actividad modificada correctamente.")


def modificar_material(material, stock_material):
    """Modifica el nombre, tipo o cantidades de un material."""
    identificador = pedir_entero("Identificador del material: ", 1, 9999)
    posicion_material = buscar_fila_por_id(material, identificador)

    if posicion_material == -1:
        print("Error: el material no existe.")
    else:
        posicion_stock = buscar_fila_por_id(stock_material, identificador)
        print("1. Modificar nombre")
        print("2. Modificar tipo")
        print("3. Modificar stock total")
        print("4. Modificar cantidad en uso")
        opcion = pedir_entero("Seleccione una opción: ", 1, 4)

        if opcion == 1:
            material[posicion_material][1] = pedir_texto("Nuevo nombre: ")
        elif opcion == 2:
            nuevo_tipo = ""

            while nuevo_tipo != "Consumible" and nuevo_tipo != "Reutilizable":
                nuevo_tipo = pedir_texto("Nuevo tipo (Consumible/Reutilizable): ")
                nuevo_tipo = nuevo_tipo.capitalize()

                if nuevo_tipo != "Consumible" and nuevo_tipo != "Reutilizable":
                    print("Error: escriba Consumible o Reutilizable.")

            material[posicion_material][2] = nuevo_tipo
        elif opcion == 3:
            en_uso = stock_material[posicion_stock][2]
            nuevo_total = pedir_entero("Nuevo stock total: ", en_uso, 9999)
            stock_material[posicion_stock][1] = nuevo_total
        else:
            total = stock_material[posicion_stock][1]
            nuevo_en_uso = pedir_entero("Nueva cantidad en uso: ", 0, total)
            stock_material[posicion_stock][2] = nuevo_en_uso

        print("Material modificado correctamente.")


def eliminar_actividad(actividades, uso_semanal, asignacion, asistencia_semanal, material_por_actividad):
    """Elimina una actividad y toda su información relacionada."""
    identificador = pedir_entero("Identificador de la actividad a eliminar: ", 1, 9999)
    posicion = buscar_fila_por_id(actividades, identificador)

    if posicion == -1:
        print("Error: la actividad no existe.")
    else:
        # pop() elimina la fila completa de cada matriz relacionada.
        actividades.pop(posicion)
        uso_semanal.pop(buscar_fila_por_id(uso_semanal, identificador))
        asignacion.pop(buscar_fila_por_id(asignacion, identificador))
        asistencia_semanal.pop(buscar_fila_por_id(asistencia_semanal, identificador))

        indice = 0
        while indice < len(material_por_actividad):
            if material_por_actividad[indice][0] == identificador:
                material_por_actividad.pop(indice)
            else:
                indice = indice + 1

        print("Actividad eliminada correctamente.")


def eliminar_material(material, stock_material, material_por_actividad):
    """Elimina un material, su stock y sus relaciones con actividades."""
    identificador = pedir_entero("Identificador del material a eliminar: ", 1, 9999)
    posicion = buscar_fila_por_id(material, identificador)

    if posicion == -1:
        print("Error: el material no existe.")
    else:
        # Se elimina el material y la fila que contiene sus cantidades.
        material.pop(posicion)
        stock_material.pop(buscar_fila_por_id(stock_material, identificador))

        indice = 0
        while indice < len(material_por_actividad):
            if material_por_actividad[indice][1] == identificador:
                material_por_actividad.pop(indice)
            else:
                indice = indice + 1

        print("Material eliminado correctamente.")


def buscar_actividades(actividades):
    """Busca actividades por una parte del nombre o por categoría."""
    print("1. Buscar por nombre")
    print("2. Buscar por categoría")
    opcion = pedir_entero("Seleccione una opción: ", 1, 2)
    encontrado = False

    if opcion == 1:
        texto = pedir_texto("Escriba el nombre o una parte del nombre: ").lower()

        for actividad in actividades:
            if texto in actividad[1].lower():
                print(actividad)
                encontrado = True
    else:
        categoria = pedir_texto("Categoría (Individual/Colectiva): ").capitalize()

        for actividad in actividades:
            if actividad[2] == categoria:
                print(actividad)
                encontrado = True

    if encontrado == False:
        print("No se encontraron actividades.")


def buscar_entrenadores(entrenadores):
    """Busca entrenadores por una parte de su nombre."""
    texto = pedir_texto("Escriba el nombre o una parte del nombre: ").lower()
    encontrado = False

    for entrenador in entrenadores:
        if texto in entrenador[1].lower():
            print(entrenador)
            encontrado = True

    if encontrado == False:
        print("No se encontraron entrenadores.")


def buscar_materiales(material):
    """Busca materiales por nombre o por tipo."""
    print("1. Buscar por nombre")
    print("2. Buscar por tipo")
    opcion = pedir_entero("Seleccione una opción: ", 1, 2)
    encontrado = False

    if opcion == 1:
        texto = pedir_texto("Escriba el nombre o una parte del nombre: ").lower()

        for fila in material:
            if texto in fila[1].lower():
                print(fila)
                encontrado = True
    else:
        tipo = pedir_texto("Tipo (Consumible/Reutilizable): ").capitalize()

        for fila in material:
            if fila[2] == tipo:
                print(fila)
                encontrado = True

    if encontrado == False:
        print("No se encontraron materiales.")


def ordenar_actividades_por_nombre(actividades):
    """Muestra las actividades ordenadas alfabéticamente por nombre."""
    nombres = []

    for actividad in actividades:
        if actividad[1] not in nombres:
            nombres.append(actividad[1])

    # sort() ordena la lista de nombres de forma alfabética.
    nombres.sort()
    print("\nACTIVIDADES ORDENADAS POR NOMBRE")

    for nombre in nombres:
        for actividad in actividades:
            if actividad[1] == nombre:
                print(actividad)


def ordenar_actividades_por_uso(actividades, uso_semanal):
    """Muestra las actividades ordenadas de mayor a menor uso semanal."""
    datos_ordenados = []

    for fila in uso_semanal:
        total = 0

        for columna in range(1, 6):
            total = total + fila[columna]

        datos_ordenados.append([total, fila[0]])

    # sort(reverse=True) coloca primero los totales más altos.
    datos_ordenados.sort(reverse=True)
    print("\nACTIVIDADES ORDENADAS POR USO SEMANAL")

    for dato in datos_ordenados:
        posicion = buscar_fila_por_id(actividades, dato[1])
        print(actividades[posicion][1], "- Total semanal:", dato[0])


def ordenar_materiales_por_stock(material, stock_material):
    """Muestra los materiales de mayor a menor stock total."""
    datos_ordenados = []

    for fila in stock_material:
        datos_ordenados.append([fila[1], fila[0]])

    # sort(reverse=True) coloca primero los materiales con más stock.
    datos_ordenados.sort(reverse=True)
    print("\nMATERIALES ORDENADOS POR STOCK")

    for dato in datos_ordenados:
        posicion = buscar_fila_por_id(material, dato[1])
        print(material[posicion][1], "- Stock total:", dato[0])


def mostrar_analisis_semanal(actividades, uso_semanal):
    """Calcula totales, actividad más demandada y día de mayor uso."""
    if len(uso_semanal) == 0:
        print("No existen actividades registradas.")
    else:
        dias_totales = [0, 0, 0, 0, 0]
        nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        mayor_total = -1
        id_mayor = 0

        print("\nANÁLISIS SEMANAL")
        for fila in uso_semanal:
            total = 0

            # Suma los usos de lunes a viernes de una actividad.
            for columna in range(1, 6):
                total = total + fila[columna]
                dias_totales[columna - 1] = dias_totales[columna - 1] + fila[columna]

            posicion = buscar_fila_por_id(actividades, fila[0])
            print(actividades[posicion][1], "- Total semanal:", total)

            if total > mayor_total:
                mayor_total = total
                id_mayor = fila[0]

        posicion_mayor = buscar_fila_por_id(actividades, id_mayor)
        print("Actividad más demandada:", actividades[posicion_mayor][1], "con", mayor_total, "usos.")

        mayor_dia = dias_totales[0]
        posicion_dia = 0

        for indice in range(1, 5):
            if dias_totales[indice] > mayor_dia:
                mayor_dia = dias_totales[indice]
                posicion_dia = indice

        print("Día con más actividades realizadas:", nombres_dias[posicion_dia], "con", mayor_dia, "usos.")


def generar_reporte(material, stock_material, actividades, uso_semanal):
    """Genera el reporte de recursos y demanda de actividades."""
    print("\nREPORTE DE RECURSOS Y DEMANDA")
    hay_agotados = False
    hay_baja_utilizacion = False

    print("\nMateriales agotados:")
    for fila in stock_material:
        disponible = fila[1] - fila[2]

        if disponible == 0:
            posicion = buscar_fila_por_id(material, fila[0])
            print("-", material[posicion][1])
            hay_agotados = True

    if hay_agotados == False:
        print("- Ninguno")

    print("\nMateriales con baja utilización (1 unidad o menos en uso):")
    for fila in stock_material:
        if fila[2] <= 1:
            posicion = buscar_fila_por_id(material, fila[0])
            print("-", material[posicion][1])
            hay_baja_utilizacion = True

    if hay_baja_utilizacion == False:
        print("- Ninguno")

    hay_alta_demanda = False
    hay_baja_demanda = False
    print("\nActividades con alta demanda (10 usos o más):")

    for fila in uso_semanal:
        total = 0

        for columna in range(1, 6):
            total = total + fila[columna]

        if total >= 10:
            posicion = buscar_fila_por_id(actividades, fila[0])
            print("-", actividades[posicion][1], "con", total, "usos")
            hay_alta_demanda = True

    if hay_alta_demanda == False:
        print("- Ninguna")

    print("\nActividades con baja demanda (2 usos o menos):")
    for fila in uso_semanal:
        total = 0

        for columna in range(1, 6):
            total = total + fila[columna]

        if total <= 2:
            posicion = buscar_fila_por_id(actividades, fila[0])
            print("-", actividades[posicion][1], "con", total, "usos")
            hay_baja_demanda = True

    if hay_baja_demanda == False:
        print("- Ninguna")


def mostrar_promedios_asistencia(actividades, asistencia_semanal):
    """Calcula el promedio semanal de asistentes de cada actividad."""
    print("\nPROMEDIO SEMANAL DE ASISTENCIA")

    if len(asistencia_semanal) == 0:
        print("No existen actividades registradas.")
    else:
        for fila in asistencia_semanal:
            total = 0

            # Se suman los asistentes de los cinco días para calcular el promedio.
            for columna in range(1, 6):
                total = total + fila[columna]

            promedio = total / 5
            posicion = buscar_fila_por_id(actividades, fila[0])
            print(actividades[posicion][1], "- Promedio:", round(promedio, 2), "estudiantes")


def mostrar_actividad_mayor_asistencia(actividades, asistencia_semanal):
    """Muestra la actividad con más asistentes durante la semana."""
    if len(asistencia_semanal) == 0:
        print("No existen actividades registradas.")
    else:
        mayor_total = -1
        id_mayor = 0

        for fila in asistencia_semanal:
            total = 0

            for columna in range(1, 6):
                total = total + fila[columna]

            if total > mayor_total:
                mayor_total = total
                id_mayor = fila[0]

        posicion = buscar_fila_por_id(actividades, id_mayor)
        print("Actividad con mayor asistencia:", actividades[posicion][1])
        print("Total de asistentes durante la semana:", mayor_total)


def menu_principal():
    """Inicia el sistema y permite navegar por todas las opciones."""
    actividades = []
    entrenadores = []
    material = []
    stock_material = []
    uso_semanal = []
    asignacion = []
    material_por_actividad = []
    asistencia_semanal = []
    opcion = -1

    # El menú se repite hasta que el usuario decide salir.
    while opcion != 0:
        print("\n--- CENTRO DEPORTIVO ESCOLAR ---")
        print("1. Registrar actividad deportiva")
        print("2. Insertar actividad en una posición")
        print("3. Registrar entrenador")
        print("4. Registrar material y stock")
        print("5. Asignar entrenador a una actividad")
        print("6. Registrar material para una actividad")
        print("7. Realizar actividad y actualizar material")
        print("8. Registrar asistencia semanal")
        print("9. Mostrar información")
        print("10. Modificar actividad o material")
        print("11. Eliminar actividad o material")
        print("12. Buscar información")
        print("13. Ordenar información")
        print("14. Consultar análisis semanal")
        print("15. Generar reporte de recursos y demanda")
        print("16. Consultar análisis de asistencia")
        print("0. Salir")
        opcion = pedir_entero("Seleccione una opción: ", 0, 16)

        if opcion == 1:
            registrar_actividad(actividades, uso_semanal, asignacion, asistencia_semanal)
        elif opcion == 2:
            insertar_actividad(actividades, uso_semanal, asignacion, asistencia_semanal)
        elif opcion == 3:
            registrar_entrenador(entrenadores)
        elif opcion == 4:
            registrar_material(material, stock_material)
        elif opcion == 5:
            asignar_entrenador(actividades, entrenadores, asignacion)
        elif opcion == 6:
            registrar_material_para_actividad(actividades, material, material_por_actividad)
        elif opcion == 7:
            realizar_actividad(actividades, uso_semanal, material_por_actividad, stock_material)
        elif opcion == 8:
            registrar_asistencia_semanal(actividades, asistencia_semanal)
        elif opcion == 9:
            print("\n1. Actividades")
            print("2. Entrenadores")
            print("3. Materiales")
            print("4. Stock de materiales")
            print("5. Uso semanal")
            print("6. Asignaciones")
            print("7. Materiales por actividad")
            print("8. Asistencia semanal")
            print("9. Actividades disponibles")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 9)

            if subopcion == 1:
                mostrar_matriz("ACTIVIDADES", actividades)
            elif subopcion == 2:
                mostrar_matriz("ENTRENADORES", entrenadores)
            elif subopcion == 3:
                mostrar_matriz("MATERIALES", material)
            elif subopcion == 4:
                mostrar_matriz("STOCK DE MATERIALES", stock_material)
            elif subopcion == 5:
                mostrar_matriz("USO SEMANAL", uso_semanal)
            elif subopcion == 6:
                mostrar_matriz("ASIGNACIONES", asignacion)
            elif subopcion == 7:
                mostrar_matriz("MATERIALES POR ACTIVIDAD", material_por_actividad)
            elif subopcion == 8:
                mostrar_matriz("ASISTENCIA SEMANAL", asistencia_semanal)
            else:
                mostrar_actividades_disponibles(actividades, material_por_actividad, stock_material)
        elif opcion == 10:
            print("1. Modificar actividad")
            print("2. Modificar material")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 2)

            if subopcion == 1:
                modificar_actividad(actividades)
            else:
                modificar_material(material, stock_material)
        elif opcion == 11:
            print("1. Eliminar actividad")
            print("2. Eliminar material")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 2)

            if subopcion == 1:
                eliminar_actividad(
                    actividades,
                    uso_semanal,
                    asignacion,
                    asistencia_semanal,
                    material_por_actividad
                )
            else:
                eliminar_material(material, stock_material, material_por_actividad)
        elif opcion == 12:
            print("1. Buscar actividades")
            print("2. Buscar entrenadores")
            print("3. Buscar materiales")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 3)

            if subopcion == 1:
                buscar_actividades(actividades)
            elif subopcion == 2:
                buscar_entrenadores(entrenadores)
            else:
                buscar_materiales(material)
        elif opcion == 13:
            print("1. Ordenar actividades por nombre")
            print("2. Ordenar actividades por uso semanal")
            print("3. Ordenar materiales por stock")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 3)

            if subopcion == 1:
                ordenar_actividades_por_nombre(actividades)
            elif subopcion == 2:
                ordenar_actividades_por_uso(actividades, uso_semanal)
            else:
                ordenar_materiales_por_stock(material, stock_material)
        elif opcion == 14:
            mostrar_analisis_semanal(actividades, uso_semanal)
        elif opcion == 15:
            generar_reporte(material, stock_material, actividades, uso_semanal)
        elif opcion == 16:
            print("1. Mostrar promedios de asistencia")
            print("2. Mostrar actividad con mayor asistencia")
            subopcion = pedir_entero("Seleccione una opción: ", 1, 2)

            if subopcion == 1:
                mostrar_promedios_asistencia(actividades, asistencia_semanal)
            else:
                mostrar_actividad_mayor_asistencia(actividades, asistencia_semanal)

    print("Gracias por usar el sistema del centro deportivo escolar.")


if __name__ == "__main__":
    menu_principal()
