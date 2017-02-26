import string
import sys

fichero = sys.argv[1]

# datacenter --> array de latencias por endpoint
# endpoint --> indiceendpoint: (indicecahches[0,1..], latencias[100, 200..])
# request ---> array de diccionarios --> indicevideo: (tamanio, indiceendpoint, numrequest)
# n --> numero de videos que necesito

def parser():
    with open (fichero) as f:
        r =  f.read()
        return r.splitlines()        

def setLin(new_val):
    global linfin
    linfin = new_val
    
# va rellenando la lista que le pasemos con tuplas (endpoint, latencia)
def recParserDatacenter(n_endpoint, l_t_dc, lineas, lin_actual):
    if n_endpoint == 0:
        setLin(lin_actual)
        return l_t_dc
    else:
        mainep = lineas[lin_actual].split(" ")
        lat_ep = int(mainep[0])
        # en la tupla por ep el segundo elem es la lista de tuplas cache-lat
        pEP = parserEndpoint(lin_actual, lin_actual + int(mainep[1]), lineas)
        l_t_dc.append((lat_ep, pEP))
        return recParserDatacenter(n_endpoint - 1, l_t_dc, lineas, lin_actual + int(mainep[1]) + 1)

        
def parserEndpoint(lin_actual, linea_final, lineas):
    lista_tuplas = []
    for i in range(lin_actual + 1, linea_final + 1):
        linea_actual = lineas[i].split(" ")
        lista_tuplas.append((linea_actual[0], linea_actual[1]))
    return sorted(lista_tuplas)


def parserRequests(lineas, linea_in, n_vid, vid_size):
    l_vid = [{i:[]} for i in range(n_vid)]
    for i in range(0, len(l_vid)):
        l_vid[i].get(i).append(vid_size[i])
    for i in range(linea_in, len(lineas)):
        mainline = lineas[i].split(" ")
        l_vid[int(mainline[0])].get(int(mainline[0])).append((mainline[1], mainline[2]))
    return l_vid


def main ():
    lineas = parser()
    config =  lineas[0].split(" ")
    n_vid = int(config[0])
    n_ep = int(config[1])
    n_req = config[2]
    t_cache = config[3]
    vid_size = list(lineas[1].split(" "))
    # a la salida del metodo recursivo esto tendra la linea de inicio del parser de requests
    datacenter = recParserDatacenter(n_ep, [], lineas, 2)
    requests = parserRequests(lineas, linfin, n_vid, vid_size)
    print(datacenter)
    print(requests)
    
main()
    
