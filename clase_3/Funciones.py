# Funciones sin retorno y sin argumenro 
# Funciones sin retorno con argumentos
# Funciones con retorno sin argumentos 
# Funciones con retorno con argumentos


def impresion ():
    '''Esta es una funcion sin argumentos '''
    print('Estoy dentro de la funcion')

def algoritmo(a, b, c, d):
    '''Funcion con argumentos/nTodos son enteros'''
    res = (a + b) * (c + d)
    print('El resultado de la operacion es: ', res)

def algoritmo2(a, b, c, d):
    '''Funcion con argumentos/nTodos son enteros'''
    res = (a + b) * (c + d) * (a)
    return(res)
 
# impresion()
# x = []
# for i in range(4):
    # x.append(int(input('Ingresa un dato: ')))

# algoritmo(x[0], x[1], x[2], x[3])

# y = algoritmo2(x[0], x[1], x[2], x[3])
# print('El resultado es: ', y)
