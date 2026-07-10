def validar_codigo(codigo, dicc_juegos):
    if not codigo or codigo.strip() == "":
        return False
    for c in dicc_juegos.keys():
        if c.lower() == codigo.lower():
            return False  
    return True

def validar_titulo(titulo):
    return bool(titulo and titulo.strip() != "")

def validar_plataforma(plataforma):
    return bool(plataforma and plataforma.strip() != "")

def validar_genero(genero):
    return bool(genero and genero.strip() != "")

def validar_clasificacion(clasificacion):
    return clasificacion in ['E', 'T', 'M']

def validar_multiplayer(multiplayer):
    return multiplayer.lower() in ['s', 'n']

def validar_editor(editor):
    return bool(editor and editor.strip() != "")

def validar_precio(precio):
    return precio > 0

def validar_stock(stock):
    return stock >= 0

def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar valores enteros")

def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Valor no aceptado, el campo no puede estar vacío.")
        elif valor.isdigit():
            print("Valor no aceptado, debe ingresar un texto válido.")
        else:
            return valor

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def buscar_codigo(codigo, dicc_inventario):
    for c in dicc_inventario.keys():
        if c.lower() == codigo.lower():
            return c
    return False

def stock_plataforma(plataforma, dicc_juegos, dicc_inventario):
    total_stock = 0
    plataforma_buscada = plataforma.strip().lower()
    
    for codigo, datos in dicc_juegos.items():
        plat_juego = datos[1].lower()
        if plat_juego == plataforma_buscada:
            if codigo in dicc_inventario:
                total_stock += dicc_inventario[codigo][1]
                
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max, dicc_juegos, dicc_inventario):
    resultados = []
    
    for codigo, datos_inv in dicc_inventario.items():
        precio = datos_inv[0]
        stock = datos_inv[1]
        
        if p_min <= precio <= p_max and stock > 0:
            if codigo in dicc_juegos:
                titulo = dicc_juegos[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if resultados:
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios.")

def actualizar_precio(clave_exacta, nuevo_precio, dicc_inventario):
    dicc_inventario[clave_exacta][0] = nuevo_precio
    return True

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dicc_juegos, dicc_inventario):
    if not validar_codigo(codigo, dicc_juegos):
        return False
        
    bool_multiplayer = True if multiplayer.lower() == 's' else False
    
    dicc_juegos[codigo] = [titulo, plataforma, genero, clasificacion, bool_multiplayer, editor]
    dicc_inventario[codigo] = [precio, stock]
    return True

def eliminar_juego(clave_exacta, dicc_juegos, dicc_inventario):
    dicc_juegos.pop(clave_exacta)
    dicc_inventario.pop(clave_exacta)
    return True

dicc_juegos_principal = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}

dicc_inventario_principal = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2]
}

ejecutando = True

while ejecutando:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")
    
    opc = leer_opcion()
    
    if opc == 1:
        plat = leer_texto("Ingrese plataforma a consultar: ")
        stock_plataforma(plat, dicc_juegos_principal, dicc_inventario_principal)
        
    elif opc == 2:
        intentando_precios = True
        while intentando_precios:
            p_min = leer_entero("Ingrese precio mínimo: ")
            p_max = leer_entero("Ingrese precio máximo: ")
            
            if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max, dicc_juegos_principal, dicc_inventario_principal)
                intentando_precios = False
            else:
                print("Error: El precio mínimo debe ser menor o igual al máximo y ambos ser positivos.")
            
    elif opc == 3:
        procesando_edicion = True
        while procesando_edicion:
            cod = input("Ingrese código del juego: ").strip()
            
            clave_encontrada = buscar_codigo(cod, dicc_inventario_principal)
            
            if clave_encontrada:
                nuevo_p = leer_entero("Ingrese nuevo precio: ")
                if validar_precio(nuevo_p):
                    actualizar_precio(clave_encontrada, nuevo_p, dicc_inventario_principal)
                    print("Precio actualizado")
                else:
                    print("El precio debe ser mayor que cero.")
            else:
                print("El código no existe")
            
            resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            if resp != 's':
                procesando_edicion = False
                
    elif opc == 4:
        cod = input("Ingrese código del juego: ").strip()
        
        if validar_codigo(cod, dicc_juegos_principal):
            tit = leer_texto("Ingrese título: ")
            plat = leer_texto("Ingrese plataforma: ")
            gen = leer_texto("Ingrese género: ")
            clas = input("Ingrese clasificación (E, T, M): ").strip().upper()
            
            if validar_clasificacion(clas):
                mult = input("¿Es multiplayer? (s/n): ").strip().lower()
                if validar_multiplayer(mult):
                    edit = leer_texto("Ingrese editor: ")
                    prec = leer_entero("Ingrese precio: ")
                    
                    if validar_precio(prec):
                        stk = leer_entero("Ingrese stock: ")
                        if validar_stock(stk):
                            if agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk, dicc_juegos_principal, dicc_inventario_principal):
                                print("Juego agregado")
                            else:
                                print("El código ya existe")
                        else:
                            print("Error: El stock no puede ser negativo.")
                    else:
                        print("Error: El precio debe ser un número mayor a cero.")
                else:
                    print("Error: En multiplayer solo se acepta 's' o 'n'.")
            else:
                print("Error: Clasificación no válida. Debe ser exactamente E, T o M.")
        else:
            print("El código ya existe")
            
    elif opc == 5:
        cod = input("Ingrese código del juego que desea eliminar: ").strip()
        
        clave_encontrada = buscar_codigo(cod, dicc_inventario_principal)
        
        if clave_encontrada:
            eliminar_juego(clave_encontrada, dicc_juegos_principal, dicc_inventario_principal)
            print("Juego eliminado")
        else:
            print("El código no existe")
            
    elif opc == 6:
        print("Programa finalizado.")
        ejecutando = False