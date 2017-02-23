def preparador ( ncaches, tamaniocache, request , n):
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
    return [i[1]for i in array]
