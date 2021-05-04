"""
================================================================

******PROGRAMA******: 
Vida media del muón

******INSTITUCION******:
Universidad del Valle de Guatemala
Introduccion  a la Fisica de Particulas

*****AUTORES******:
-Christian Ramirez
-Luis Mijangos
-Pablo Marroquín
-Erick Alvarez
-Juan Arroyave
-Javier Mejia
-César Meza
-Julio Monzón
-Alberto Ortega
-Valeria Paiz
-Adam Rios
-Paula Valdes
-Juan Zelada

================================================================
"""
#FUNCIONES
def LecturaArchivo():
        
    #Se abre el archivo .dat con los datos
    #Datos disponibles en: https://drive.google.com/file/d/1JNdSDK6nUtivXMkhYhhEf404BN2XVCEm/view?usp=sharing
    archivo = open("vida-media-datos.dat", "r")
        
    #Se ignoran las primeras 41 lineas de encabezado del archivo
    for i in range(1,41):
        archivo.readline()
    
    linea = "vacía"
    i = 0
    #Se recorre todo el archivo guardando el tiempo en que ocurrieron los eventos
    while (len(linea) > 0) and (i < 40000000):  
        #Se busca cada registro de tiempo  
        maximo = 0
        while (len(linea) > 0) and linea[0].isnumeric():
            linea = archivo.readline()
    
     #Se toma únicamente el valor de la cantidad de cuentas de reloj transcurridas
            if linea[0:1].isnumeric() and len(linea) > 5:
                posible_max = int(linea[6:len(linea)])
                if posible_max > maximo:
                    maximo = posible_max
    
        if (len(linea) > 0) and (linea[2] == 't'):
            eventos.append(int(linea[6:len(linea)])) 
            amplitud.append(maximo)
              
        linea = archivo.readline()
        i = i + 1
    archivo.close()

def Identificacion_Muon():
    #Deteccion de decaimientos entre 20 y 500 cuentas de reloj de 40 MHz
    n = 0
    for indice in range(0,maximo + 2):
        bins.append(0)
        tiempos.append(n/40000000.0)
        n += 1
    
    #Se revisa si hay un pico de detección grande seguido de uno de menor tamaño
    for r in range(1,len(eventos)):
        delta = eventos[r] - eventos[r-1]
        razon = amplitud[r] / amplitud[r-1]
        
        #Se toma el intervalo de tiempo y se agrega a los bines del histograma
        if delta < 0:
            delta = eventos[r] + 40000000 - eventos[r-1]
        if (delta > minimo) and (delta < maximo) and (razon < 1.0):
            detecciones.append(r)
            bins[delta] = bins[delta] + 1

def Exportar_datos(): 
    exportado = open("bines.txt","w")
    for r in range(0,len(bins)):
        exportado.write(str(tiempos[r]) + ", " + str(bins[r]) + "\n" )
    exportado.close()

#==============================================================================

# INICIO PROGRAMA
#se declaran las variables a utilizar
eventos = []
amplitud = []
detecciones = []  
minimo = 20
maximo = 500
bins = []
tiempos = []
razon = 0.0

LecturaArchivo()
Identificacion_Muon()
Exportar_datos()

#FIN DEL PROGRAMA