def preparadorgeneral ( ncaches, tamaniocache, request , n):
    # datacenter --> array de latencias por endpoint
    # request ---> array de diccionarios --> indicevideo: (tamanio, indiceendpoint, numrequest)
    # n --> numero de videos que necesito
    # Comprobar si la latencia del datacenter es mayor que alguna cache--> lo hace el a estrella?
    # Retorna lista de indices de videos a distribuir
    # Si hay algun video de mayor peso que las caches, se va a quedar en el datacenter
    array = []
    for i in request.keys():
        if request[i][0] <= tamaniocache:
            #arrayvideos.append(i)
            #arraytamanios.append(request[i][0])
            array.append([sum(request[i][2]), i, request[i][0])])
    #Array : (sumarequest, indicevideo, tamanio)
    #Ahora tengo los que en teoria caben en la caches
    tamaniototal= ncaches * tamaniocache
    array = sorted(array)
    while sum([i[2]for i in array]) > tamaniototal or len(array)> n:
        #Estrechamos los videos que pasamos:
        indice = 0
        if array[0][0] == array [1][0]:
            if array [1][2] > array[0][0]:
                indice = 1
        del array[indice]
    return array


def preparadorendpoint ( array, endpoint, request, tamaniocache):
    # datacenter --> array de latencias por endpoint
    #endpoint --> indiceendpoint: (indicecahches[0,1..], latencias[100, 200..])
    # request ---> array de diccionarios --> indicevideo: (tamanio, indiceendpoint, numrequest)
    # n --> numero de videos que necesito
    # Comprobar si la latencia del datacenter es mayor que alguna cache--> lo hace el a estrella?
    # Retorna lista de indices de videos a distribuir
    # Si hay algun video de mayor peso que las caches, se va a quedar en el datacenter
    resultado = dict()
    for i in array:
        indicevideo = i[1]
        #Para cada video veo los endpoints que lo piden:
        indicesendpoints = request[indicevideo][1]
        for j in indicesendpoints:
            if j in resultado.keys():
                temp = resultado[j]
                temp.append([sum(request[i][2]), i, request[i][0])])
                resultado[j] = temp
            else:
                resultado[j] = [[sum(request[i][2]), i, request[i][0])]]
    #Aqyui tengo un diccionarios de endpoints: [(request, indice, tamanio)]
    for i in resultado.keys():
        datos = resultado[i]
        datos = sorted(datos)
        while sum([x[2] for x in datos]) > (len(endpoints[i][0])*tamaniocache):
            del datos[0]
        resultados[i]= datos
    return resultados
