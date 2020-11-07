import sys
import requests
import json

import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = None

SUBSCRIPTION_KEY = 'bd6c79bb7a4c418a9444d2cf7304de08'
BASE_URL = 'https://proyectocarabrrr.cognitiveservices.azure.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)


#Obtener las emociones de una persona
#picture recibe la foto de la persona que se desea obtener las emociones
def emotions(picture):
    #headers = {'Ocp-Apim-Subscription-Key': 'e70e11c9cb684f21b8b37313fd60e5bc'}
    image_path = picture
    #https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-disk
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    response = requests.post(
                             BASE_URL + "detect/", headers=headers, params=params, data=image_data)
    analysis = response.json()
    #quitar el # para que el sistema imprima la lista con los datos
    #print(analysis)
    return analysis

def metodosort(lista):
    indexacion = range(1,len(lista))
    for a in indexacion:
        entrada= lista[a]
        while lista[a-1] > entrada and a > 0:
            lista[a],lista[a-1]= lista[a-1], lista[a]
            a=a-1
    print(lista)
    return lista
   
def metodoquicksort(lista):
    
    cantidad=len(lista)
    if cantidad <= 1:
        return lista
    else:
        
        pivot=lista.pop()
    mayor=[]
    menor=[]
    for x in lista:
        if int(x[1]) > pivot[1]:
            mayor.append(x)
        else:
            menor.append(x)
    return print(metodoquicksort(menor) + [pivot] + metodoquicksort(mayor))


def facesperimage(imageinformation):
    cont=0
    for a in imageinformation:
        cont=cont+1
    print("En la imagen hay ",cont, "personas")
    return cont

def masjoven(imageinformation):
    tem=100000.0
    ages=[]
    for a in imageinformation:
        carac=a["faceAttributes"]
        age= carac["age"]
        ages.append(age)
        if age<tem:
            tem=age
    print("las edades de las personas en las lista son:",ages,"y el más joven tiene",tem)
    return ages, tem

def jovengenerosort(imageinformation):
    
    listafin=[]
    for a in imageinformation:
        personas=[]
        carac=a["faceAttributes"]
        age=carac["age"]
        gender=carac["gender"]
        personas.append(age)
        personas.append(gender)
        listafin.append(personas)
    
    return listafin

def agender10x10(listaperso):
    conta=10
    lista10x10=[]
    listafin=[]

    for a in listaperso:
        tem=a
        if tem[0] >= conta:
            conta=conta+10
            listafin.append(lista10x10)
            lista10x10=[]
            lista10x10.append(tem)
        elif tem[0] < 0:
            lista10x10.append(tem)
    if lista10x10 != []:
        listafin.append(lista10x10)

    print(listafin)
    return listafin

def agesaverage(imageinformation):
    ages=[]
    suma=0
    for a in imageinformation:
        carac=a["faceAttributes"]
        age= carac["age"]
        ages.append(age)
        valor=int(age)
        suma=valor+suma
    cantidad=len(ages)

    divi=suma//cantidad
    print(ages,"el promedio de edades es de ",divi)
    return divi

def faceIdgenderage(imageinformation):
    
    listafin=[]
    for a in imageinformation:
        listageneral=[]
        carac=a["faceAttributes"]
        faceId=a["faceId"]
        age=carac["age"]
        gender=carac["gender"]
        listageneral.append(faceId)
        listageneral.append(age)
        listageneral.append(gender)
        listafin.append(listageneral)
    
    return listafin

def happiness(imageinformation):
    tem=0
    
    for a in imageinformation:
        carac=a["faceAttributes"]
        faceid=a["faceId"]
        age=carac["age"]
        emotion=carac["emotion"]
        gender=carac["gender"]
        hlevel=emotion["happiness"]
        if hlevel > tem:
            lista=[]
            tem=hlevel
            lista.append(faceid)
            lista.append(age)
            lista.append(gender)

    print("la persona con mayor nivel de felicidad es",lista, "y tiene", tem, "de felicidad")
    return tem

def happyunderage(imageinformation,average):
    datos=[]
    for a in imageinformation:
        carac=a["faceAttributes"]
        faceid=a["faceId"]
        age=carac["age"]
        emotion=carac["emotion"]
        gender=carac["gender"]
        hlevel=emotion["happiness"]
        if age < average:
            datos.append(faceid)
            datos.append(age)
            datos.append(gender)
    print("la persona con mayor felicida y que esta por debajo del rango de edad es",datos,"y tiene",hlevel,"de felicidad")

def beardandhappy(imageinformation):
    datosfeliz=[]
    datosbarba=[]
    tem=0.0
    tem2=0.0
    for a in imageinformation:
        carac=a["faceAttributes"]
        faceid=a["faceId"]
        age=carac["age"]
        emotion=carac["emotion"]
        gender=carac["gender"]
        hlevel=emotion["happiness"]
        facialHair=carac["facialHair"]
        beard=facialHair["beard"]
        if hlevel > tem:
            datosfeliz.append(faceid)
            datosfeliz.append(age)
            datosfeliz.append(gender)
        if beard > tem2:
            datosbarba.append(faceid)
            datosbarba.append(age)
            datosbarba.append(gender)
    print("la persona con mayor felicidad es",datosfeliz,"y tiene",tem,"de felicidad. y el que tiene más barba es", datosbarba," con",tem2)

if __name__ == "__main__":  
    picture = input("Introduzca el path de la imagen: ")
    information=emotions(picture)
    totalfaces=facesperimage(information)
    masjoven(information)
    metodosort(jovengenerosort(information))
    agender10x10(metodosort(jovengenerosort(information)))
    average=agesaverage(information)
    metodoquicksort(faceIdgenderage(information))
    happiness(information)
    happyunderage(information,average)
    beardandhappy(information)