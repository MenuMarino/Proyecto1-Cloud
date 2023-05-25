import face_recognition as fr
from rtree import index
import numpy as np
from  heapq import heapify, heappush, heappop
import os
import time

names = []
def crear_insertar():
    p = index.Property()
    p.dimension = 128
    idx = index.Rtree('rtree',properties=p)
    
    with open('names.txt') as f:
        aux = f.readlines()

    nombres = []
    for i in aux:
        i = i.rstrip()
        nombres.append(i)
        
        #print(i)

    feature_vectors = []
    np.savetxt('nombres.txt',nombres,fmt='%s')
    
    for i in nombres:
        image = fr.load_image_file('uploads/' + i)
        # No tiene cara o la leyo mal
        if not fr.face_encodings(image):
            continue

        encoding = fr.face_encodings(image)[0]
        feature_vectors.append(np.concatenate([encoding,encoding]))
        #print(encoding)


    cont =0
    for i in feature_vectors:
        idx.insert(cont,i)
        cont+=1


def knn_r(nombre, cant):
    p = index.Property()
    p.dimension = 128
    idx = index.Rtree('rtree', properties=p)
    names = np.loadtxt('nombres.txt',dtype=str)
    image = fr.load_image_file(nombre)
    encoding = fr.face_encodings(image)[0]
    vec = np.concatenate([encoding,encoding])
    
    ret = list(idx.nearest(vec, cant))

    pasto = []

    ret1 = {}
    cont = 1
    for i in ret:
        ret1[cont] = names[i]
        cont += 1
        # print(names[i])

    for key, value in ret1.items():
        pasto.append( {'id': key, 'name': value} )
    return pasto


    
def range_q(nombre, rango):
    rango = rango/100
    p = index.Property()
    p.dimension = 128
    idx = index.Rtree('rtree', properties=p)
    names = np.loadtxt('nombres.txt',dtype=str)
    image = fr.load_image_file(nombre)
    encoding = fr.face_encodings(image)[0]
    vec = np.concatenate([encoding-rango,encoding+rango])
    
    ret = list(idx.intersection(vec))

    ret1 = {}
    cont = 1
    for i in ret:
        ret1[cont] = names[i]
        cont += 1 
        # print(names[i])
    return ret1

def knn_h(nombre, cant):
    cant = cant-1;
    with open('names.txt') as f:
        aux = f.readlines()

    nombres = []
    
    for i in aux:
        i = i.rstrip()
        nombres.append(i)


    image1 = fr.load_image_file(nombre)
    encoding1 = fr.face_encodings(image1)[0]
    base = [encoding1]
    distances = []
    cont =0
    for i in nombres:
        image2 = fr.load_image_file('uploads/' + i)
        if not fr.face_encodings(image2):
            continue

        encoding2 = fr.face_encodings(image2)[0]
        distances.append([fr.face_distance(base, encoding2)[0]*-1,i])
        cont+=1
    

    heap = []
    heapify(heap)


  
    for i in distances:
        tamano = len(heap)
        
        if(tamano <= cant):
            #print('a')
            heappush(heap,i)
            
        elif(i > heap[0] and len(heap) >= cant):
            heappop(heap)
            heappush(heap,i)
        else:
            continue
        
        

    results = []

 
    
    while(len(heap)>0):
        i = heap[0]
        i[0] = i[0]*-1
        results.append(i)
        heappop(heap)
    
    results.reverse()

    pasto = []

    ret = {}
    cont = 1
    for i in results:
        #print(i)
        ret['id'] = cont
        ret['name'] = i[1]
        cont += 1
        pasto.append(ret)
        # print(i[1])
        
    return pasto
