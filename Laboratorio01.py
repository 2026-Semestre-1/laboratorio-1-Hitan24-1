"""
1: Calculadora
E: operacion, numero1 y numero 2
S: Resultado de la operacion
R: Solo numeros enteros
"""
def calculadora(operacion, op1, op2):
    if not isinstance(op1, int) or not isinstance(op2, int):
        return "Los parametros deben ser tipo entero"
    if not isinstance(operacion, int):
        return "El parametro operacion debe ser un nemero entero"
    if operacion > 0 and operacion <= 4:
        return calculadora_aux(operacion, op1, op2)
    else:
        return "Las opciones de operecion son de 1 a 4"


def calculadora_aux(operacion, op1, op2):
    res = 0
    if operacion == 1:
        res = op1 + op2
        return res
    if operacion == 2:
        res = op1 - op2
        return res
    if operacion == 3:
        res = op1 * op2
        return res
    if operacion == 4:
        res = op1 // op2
        return res
    return res


"""
2: contadorDigitos
E: Numero
S: Cantidad de digitos del numero seleccionado
R: numero y digito deben ser enteros
"""

def contadorDigitos(num, digito):
    if not isinstance(digito, int):
        return "Error: El parametro digito debe ser de tipo entero"
    if not isinstance(num, int):
        return "Error: el parametro num debe ser tipo entero"
    if digito > 9 or digito < -9:
        return "Erro: El parametro debe ser un valor menor a 10"
    else:
        return contadorDigitos_aux(num, digito)

def contadorDigitos_aux(num, digito):
    if num < 0:
        num = num * -1
    if digito < 0:
        digito = digito * -1
    res = 0
    if num == digito:
        return 1
    while num > 0:
        if digito == num %10:
            res += 1
        num = num // 10
    return res        


"""
3: sumatoria_v2
E: inicio ,
S: suma de los numeros
R:
todos los parametros deben ser enteros.
La distancias y excepcion debe un numero entre 1 y 9.
inicio y fin deben ser positivos.
si distancia es un num negativo, el valor fin debe ser menor a inicio.
si distancia es un num positivo, el valor fin debe ser mayor a inicio.
"""

def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not isinstance(inicio, int) or not isinstance(fin, int) or not isinstance(distancia, int) or not isinstance(excepcion, int):
        return "Todos los parametros deben ser enteros"
    if not inicio < 10 or not inicio > 0:
        return "Inicio deber ser  un parametro de 1 a 9"
    if not fin < 10 or not fin > 0:
        return "Fin deber ser  un parametro de 1 a 9"
    if not (distancia < 10) or (distancia > 0) and (distancia > -10) or (distancia<0):
        return "El parametro distancia debe ser un valor de -9 a 9"
    else:
        return sumatoria_V2_auc(inicio, fin, distancia, excepcion)


def sumatoria_V2_aux(inicio, fin, distancia, excepcion):
    res = 0
    i = 1
    while fin >= inicio:
        if fin % expcepcion != 0:
            res = res + fin
            fin -= 1
        res = res + fin
        fin -= 1
    return res
        
        
        
    
    
