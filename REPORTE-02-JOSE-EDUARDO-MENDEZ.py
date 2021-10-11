# -*- coding: utf-8 -*-

"""

Analisis de Datos en sistema Synergy Logistics

"""

import csv

lista_datos = []
with open("synergy_logistics_database.csv", "r") as archivo: #Se abre archivo csv en modo lectura
    lector = csv.DictReader(archivo)      #Se utiliza archivo como diccionario
    for registro in lector: # Iteramos para obtener los registros a la lista de datos
        lista_datos.append(registro)      

# 1.- Rutas más demandadas
def rutas_exportacion_importacion(direccion):     #Definimos una función para recibir los parámetros de las Exportaciones e Importaciones
    contador = 0                        #La variable contador guardara el número de veces que aparece la ruta
    rutas_contadas = []                 #Creamos dos listas vacías para utilizar a continuación
    rutas_conteo = []                   
    
    for ruta in lista_datos:            #Recorremos la informacion en la lista para extraer los datos para nuestras listas vacias        
        if ruta["direction"] == direccion: # validando la dirección = True
            ruta_actual = [ruta["origin"], ruta["destination"]]  #Agrega origen y destino a la ruta
            
            if ruta_actual not in rutas_contadas: # Creamos condición para obtener las rutas que no se han contado.
                for ruta_base in lista_datos:      # Iteramos para validar que se sumen las rutas con los datos especificados:
                    if ruta_actual == [ruta_base["origin"], ruta_base["destination"]] and ruta_base["direction"] == direccion:
                        contador+=1
                
                rutas_contadas.append(ruta_actual) # Agregamos la información que obtuvimos a nuestra tabla final
                rutas_conteo.append([ruta["origin"], ruta["destination"], contador])  
                contador = 0  
           
    rutas_conteo.sort(reverse = True, key = lambda x:x[2])  #Ordenamos de mayor a menor el conteo por ruta
    rutas_conteo=rutas_conteo[0:10]   #Mostramos solo las 10 Rutas con más demanda de nuestra colección
    return rutas_conteo

conteo_exportaciones = rutas_exportacion_importacion("Exports")  # Variable que mandara a llamar la función para guardar los datos de rutas que contengan Exports
conteo_importaciones = rutas_exportacion_importacion("Imports")  # Variable que mandara a llamar la función para guardar los datos de rutas que contengan Imports

print(" Top 10 de rutas con más demanda en Exportaciones: \n ") # Iteramos para mostrar las 10 rutas con más demanda para exportaciones
for r_exp in conteo_exportaciones:
    print (r_exp)

print(" Top 10 de rutas con más demanda en Importaciones: \n ")  # Iteramos para mostrar las 10 rutas con más demanda para importaciones
for r_imp in conteo_importaciones :
    print (r_imp)

#2.- Valor de medios de transporte

def transporte_valor_exports_import(direccion):    # Creamos función que recibira parámetros Exportación o Importación
    contador = 0                                   # La variable contador guardara el número de veces
    total=0                                        # Variable total guardara la suma del valor por cada medio de transporte
    transporte_contadas = []                       # Creamos dos listas vacías para utilizar a continuación
    transportes_conteo = []                        
    
    for ruta in lista_datos:                       # Recorremos la informacion en la lista para extraer los datos necesarios para nuestras listas vacias
        if ruta["direction"] == direccion:         # Validación
            ruta_actual = [ruta["transport_mode"]] 
            
            if ruta_actual not in transporte_contadas: # Condición para nuestra variable contador, contara el número de veces que se encuentra el medio de transporte
                for ruta_bd in lista_datos:
                    if ruta_actual == [ruta_bd["transport_mode"]] and ruta_bd["direction"] == direccion:
                        contador +=1
                        total += int(ruta_bd["total_value"]) #Convertimos el dato a entero para realizar la suma
                
                transporte_contadas.append(ruta_actual) # Agreamos información obtenida a nuestra tabla final
                transportes_conteo.append([ruta["transport_mode"], contador,total]) 
                contador = 0
                total=0
        
    transportes_conteo.sort(reverse = True, key = lambda x:x[2])  # Ordenamos de mayor a menor con nuestra expresion lambda el valor total de cada medio de transporte
    transportes_conteo= transportes_conteo[0:3] # Mostramos solo los 3 principales medios de transporte considerando su valor
    return transportes_conteo
            
transporte_exportaciones = transporte_valor_exports_import("Exports") # Variable que mandara a llamar la función para guardar los datos de transporte que contengan Exports
transporte_importaciones = transporte_valor_exports_import("Imports") # variable que mandara a llamar la función para guardar los datos de transporte que contengan Imports

print(" Top 3 de mejores medios de transporte en exportaciones: \n ") # Iteramos para mostrar los 3 mejores medios de tranporte en Exportaciones
for t_exp in transporte_exportaciones:
    print (t_exp)
    
print(" Top 3 de mejores medios de transporte en importaciones: \n ") # Iteramos para mostrar los 3 mejores medios de tranporte en Importaciones
for t_imp in transporte_importaciones:
    print (t_imp)
    
# 3.- Países que generan 80% de valor

def paises_exports_imports(direccion):   # Función que obtendra como parámetro Exportación o Importación
    contador=0                           # Variable que guardará cuantas veces aparece el país
    total=0                              # Variable que guardara valor total generado por país
    paises_contados=[]                   # Listas vacias 
    valor_paises=[]                      
       
    for pais in lista_datos:             # Se recorre lista de datos
        if pais["direction"] == direccion:
            pais_actual= [pais["origin"]] # Guardamos la variable a comparar
            
            if pais_actual not in paises_contados: #Conteo pais y total
                for pais_b in lista_datos:
                    if pais_actual== [pais_b["origin"]] and pais_b["direction"]== direccion:
                        contador +=1
                        total += int (pais_b["total_value"]) # Convertimos el dato a entero para realizar la suma
                        
                paises_contados.append(pais_actual)
                valor_paises.append([pais["origin"],total,contador]) # Agregamos la información obtenida a la tabla final
                contador=0
                total=0
                
    valor_paises.sort(reverse=True, key = lambda x:x[1]) #Ordena de mayor a menor el valor total de cada país
    return valor_paises

# Creamos otra función para obtener el porcentaje y conocer los países que forman parte de dicho porcentaje
def porcentaje_paises_exports_imports (lista_paises, porcentaje = 0.8): 
    valor=0             
    valor_actual=0      
    paises=[]
    porcentajes_calculados=[]  
    
    for pais in lista_paises:  # Recorremos nuestra lista de datos por pais
        valor += pais[1]       # Sumamos por pais
        
    for pais in lista_paises:   # Recorremos nuestra lista de datos por pais
        valor_actual += pais[1] # Sumamos valor de operación
        porcentaje_actual = round(valor_actual / valor, 3) # Dividimos valor del país entre el valor total para obtener porcentaje
        paises.append(pais)
        porcentajes_calculados.append(porcentaje_actual) #Se agrega la información obtenida a la tabla final
        
        if porcentaje_actual <= porcentaje: #Condición para cumplir con el porcentaje solicitado
            continue
        else:
            if porcentaje_actual - porcentaje <= porcentajes_calculados[-2] - porcentaje: # Porcentaje que se desea
                break
            else:
                paises.pop(-1) #Si se rebasa el porcentaje que se desea, se borrará el último elemento sumado
                porcentajes_calculados.pop(-1)
                break
    
    return paises

paises_80_exportaciones = porcentaje_paises_exports_imports(paises_exports_imports("Exports")) # Variable que mandara a llamar la funcion de porcentaje para guardar los porcentajes por pais que contengan Exports
paises_80_importaciones = porcentaje_paises_exports_imports(paises_exports_imports("Imports")) # Variable que mandara a llamar la funcion de porcentaje para guardar los porcentajes por pais que contengan Imports

print(" Países que cumplen con el Porcentaje de exportaciones son: ")  # Iteramos para mostrar los Paises que cumplen con el 80% en exportaciones
for p_exp in paises_80_exportaciones:
    print(p_exp)

print(" Paises que cumplen con el Porcentaje de importaciones son: ")  # Iteramos para mostrar los Paises que cumplen con el 80% en importaciones 
for p_imp in paises_80_importaciones:
    print(p_imp)