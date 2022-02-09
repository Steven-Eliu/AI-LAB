def Algoritmo_bayes(x):
    '''X es un arreglo de datos\nAltura\nPeso\nNoCalzado'''
    import csv

    Altura_hombre = []
    Altura_mujer = []
    Peso_hombre = []
    Peso_mujer = []
    Pie_hombre = []
    Pie_mujer = []
    No_hombre = 0
    No_mujer = 0

    with open('/clase_4/db.csv') as archivo:
        lector = csv.reader(archivo, delimiter = ',', quotechar = ',', quoting = csv.QUOTE_MINIMAL)
        for renglon in lector:
            if (len(renglon)!=0):
                if (renglon[0] == 'H'):
                    No_hombre = No_hombre + 1 
                    Altura_hombre.append(int(renglon[1]))
                    Peso_hombre.append(int(renglon[2]))
                    Pie_hombre.append(int(renglon[3]))
                elif (renglon[0] == 'M'):
                    No_mujer = No_mujer + 1 
                    Altura_mujer.append(int(renglon[1]))
                    Peso_mujer.append(int(renglon[2]))
                    Pie_mujer.append(int(renglon[3]))

    Media_alturas_H = sum(Altura_hombre) / len(Altura_hombre)
    Media_peso_H = sum(Peso_hombre) / len(Peso_hombre)
    Media_pie_H = sum(Pie_hombre) / len(Pie_hombre)

    Media_alturas_M = sum(Altura_mujer) / len(Altura_mujer)
    Media_peso_M = sum(Peso_mujer) / len(Peso_mujer)
    Media_pie_M = sum(Pie_mujer) / len(Pie_mujer)

    # Calculos de Varianzas

    def varianza(Arr, med):
        '''Arr-> Arreglo de datos \med-> media del arreglo'''
        t = len(Arr)
        s = 0
        for i in range (t):
            D = (Arr [i] - med) ** 2
            s = s + D
        v = s / float(t)
        return(v)

    var_altura_h = varianza(Altura_hombre,Media_alturas_H)
    var_peso_h = varianza(Peso_hombre,Media_peso_H)
    var_pie_h = varianza(Pie_hombre,Media_pie_H)

    var_altura_m = varianza(Altura_mujer,Media_alturas_M)
    var_peso_m = varianza(Peso_mujer,Media_peso_M)
    var_pie_m = varianza(Pie_mujer,Media_pie_M)

    # Vector DX (Vector de prueba)

    # x = [170, 68, 25] #Este vector a que clase corresponde

    # Calculos de las probabilidades

    P_hombre = No_hombre / float (No_hombre + No_mujer)
    P_mujer = No_mujer / float (No_hombre + No_mujer)

    def Funcion_prob (Var, Med, Dx):
        '''Varanza \nMedia \nDato'''
        import math
        P1 = 1 / (math.sqrt(2 * math.pi * Var))
        P2 = - ((Dx - Med)** 2) / (2 * Var)
        P3 = P1 * math.exp (P2)
        return(P3)

    P_altura_h = Funcion_prob(var_altura_h, Media_alturas_H, x[0])
    P_peso_h = Funcion_prob(var_peso_h, Media_peso_H, x[1])
    P_pie_h = Funcion_prob(var_pie_h, Media_pie_H, x[2])

    P_altura_m = Funcion_prob(var_altura_m, Media_alturas_M, x[0])
    P_peso_m = Funcion_prob(var_peso_m, Media_peso_M, x[1])
    P_pie_m = Funcion_prob(var_pie_m, Media_pie_M, x[2])

    Prioriti_H = P_hombre * P_altura_h * P_peso_h * P_pie_h
    Prioriti_M = P_mujer * P_altura_m * P_peso_m * P_pie_m

    Evidencia = Prioriti_H + Prioriti_M

    Posteriori_H = Prioriti_H / Evidencia
    Posteriori_M = Prioriti_M / Evidencia

    if (Posteriori_M > Posteriori_H):
        return(1)
            # print('Los datos son de una mujer en un: ', (Posteriori_M * 100), '%')

    elif(Posteriori_H > Posteriori_M):
            # print('Los datos son de una mujer en un: ', (Posteriori_H * 100), '%')
        return(2)
    else:
            # print('Los datos no pueden ser clasificados')
        return(3)