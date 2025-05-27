# Inputs.py
def validar_nombre() -> str:
    """
    Solicita un nombre, valida que tenga al menos 3 caracteres y contenga solo letras y espacios.
    Retorna el nombre válido.
    """
    while True:
        nombre = input("Ingrese el nombre del participante: ")
        # Eliminar espacios al inicio y final manualmente
        inicio = 0
        fin = len(nombre) - 1
        while inicio <= fin and nombre[inicio] == " ":
            inicio += 1
        while fin >= inicio and nombre[fin] == " ":
            fin -= 1
        nombre_limpio = nombre[inicio:fin+1]

        # Validar longitud
        if len(nombre_limpio) >= 3:
            solo_letras_espacios = True
            for c in nombre_limpio:
                es_letra = ('a' <= c <= 'z') or ('A' <= c <= 'Z')
                es_espacio = c == " "
                if not (es_letra or es_espacio):
                    solo_letras_espacios = False
                    break
            if solo_letras_espacios:
                return nombre_limpio
        print("Error: El nombre debe tener al menos 3 caracteres y contener solo letras y espacios.")

def validar_puntaje() -> int:
    """
    Solicita un puntaje, valida que esté entre 1 y 10.
    Retorna el puntaje válido.
    """
    while True:
        entrada = input("Ingrese el puntaje (1-10): ")
        # Validar manualmente si la entrada es un número entero
        es_entero = True
        if len(entrada) == 0:
            es_entero = False
        else:
            for c in entrada:
                if not ('0' <= c <= '9'):
                    es_entero = False
                    break
        if es_entero:
            puntaje = 0
            for c in entrada:
                puntaje = puntaje * 10 + (ord(c) - ord('0'))
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("Error: El puntaje debe estar entre 1 y 10.")
        else:
            print("Error: Ingrese un número entero.")