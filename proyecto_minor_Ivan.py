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
    cantidad=int(len(ages))

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
    print("La persona más feliz es",datosfeliz,"con",tem,"de felicidad.  El que tiene más barba es", datosbarba," con",tem2)

def  show_age_and_gender_quick(faces): #>>>>>>>>>>>>>>>><>>><<>>>>>><<>><<

    ages_faces=[]
    for face in faces: 
        temporal={}                       
        faceAttributes=face['faceAttributes']
        edad=faceAttributes['age']
        genero=faceAttributes['gender']
        temporal['age']= edad
        temporal['gender']= genero
        ages_faces.append(temporal)
    male=[]
    female=[]
    for genero in ages_faces:
        if genero['gender']=='female':
            female.append(genero)
        else:
            male.append(genero)
    female= quicksort_1(female)
    male= quicksort_1(male)
    female=delete_dict(female)
    male=delete_dict(male)
    male_female=[]
    if len(female) != 0:
        male_female.append(female)
    if len(male) != 0:
        male_female.append(male)
    print('La lista de edades y géneros, separados por género (quicksort) es:\n')
    print(male_female)

def delete_dict(lista): #>><<>>><
    pos=0
    for i in lista:
        temp=[]
        edad=i['age']
        genero=i['gender']
        temp.append(edad)
        temp.append(genero)
        lista[pos]= temp
        pos+=1
    return lista

#9. 
def particionado_1(lista):
    menores= []
    mayores= []
    saca_pivote= lista[-1]
    pivote= saca_pivote['age']
    for x in lista[:-1]:
        if x['age'] < pivote:
            menores.append(x)
        else:
            mayores.append(x)
    return [menores, saca_pivote, mayores]

def quicksort_1(lista):

    if len(lista) > 0:
        lista= particionado_1(lista)
        cont= 0
        while cont < len(lista):
            elemento= lista[cont]
            if type(elemento) == list:
                if len(elemento) == 0:
                    del lista[cont]
                elif len(elemento) == 1:
                    lista[cont]= elemento[0]
                else:
                    lista=lista[:cont]+ particionado_1(elemento)+ lista[cont+1:]
            else:
                cont+= 1
        return lista

def blonde_female(faces):    #<><<<<<<><><<<>><<<<<><>>><>>><<<><<<<>>>>>><<<<>>>><<<<>>>                                 
    blonde= 0
    faceId1 = ''
    estado = False
    for face in faces:
        faceId=face['faceId']
        faceAttributes = face['faceAttributes']
        gender = faceAttributes['gender']           
        hair= faceAttributes['hair']
        hairColor=hair['hairColor']
        if gender == 'male':
            continue
        estado=True
        for color in hairColor:
            if color['color']=='blond':
                color1=color['color']
                color2=color['confidence']
                break
        if color2 > blonde:
            blonde=color2
            faceId1=faceId
    if estado == True:
        print("\nLa mujer más rubia es: ",faceId1,
            "\n El porcentaje es de: ",blonde)
    else:
        print("\nNo se detectaron mujeres en la imagen") 

def show_image(picture,
        faces): #>><<><<>>><<<><<>><<>>>>><<><<
    image = Image.open(picture)
    for face in faces:
        fa = face['faceRectangle']
        top = fa['top'] 
        left = fa['left']  
        width = fa['width'] 
        height = fa['height']
        draw = ImageDraw.Draw(image)
        draw.rectangle((left, top, left+width, top+ height), outline= "blue", width = 4)
    image.show(image)  

def glasses_ungry(faces): #>><<<<<>>><>><<>>>><<<<<<>>><<<<
    angry1 = 0
    estado= False                                                        
    faceId1 = " "        
    for face in faces:
        faceId=face['faceId']
        faceAttributes = face['faceAttributes']
        glasses = faceAttributes['glasses']
        emotion = faceAttributes['emotion']  
        angry=emotion['anger']
        if glasses != 'NoGlasses':
            estado= True
            if angry >= angry1:   
               angry1 = angry                                  
               faceId1 = faceId    
    if estado == True:
        print("\n El más enojada/o es",faceId1,
            "EL porcentaje de enojo es: ",angry1)
    else:
        print("\n No se detectaron personas con lentes ")      

def historial_consultas(faces):   #>>><>>>><<>>>><>
    historial=[]
    for face in faces:
        dicc={}
        faceId=face['faceId']
        faceAttributes=face['faceAttributes']
        gender=faceAttributes['gender']
        age=faceAttributes['age']
        emotion=faceAttributes['emotion']
        faceRectangle=face['faceRectangle']
        dicc['faceId']= faceId
        dicc['gender']= gender
        dicc['age']= age
        dicc['emotion']= emotion
        dicc['faceRectangle']= faceRectangle
        historial.append(dicc)
    return historial

def young_emotions_rec(picture, faces): #>>><><<
    mas_joven=150
    faceId_real=""
    emociones= {}
    rostro_joven={}
    for face in faces:
        faceId=face['faceId']
        faceRectangle=face['faceRectangle']
        emotion=face['emotion']
        age=face['age']
        if age < mas_joven:
            mas_joven=age
            faceId_real= faceId
            emociones=emotion
            rostro_joven=face
    print('\nLa persona más joven es:', faceId_real)
    print('Edad:',mas_joven)
    print('Emociones: ')
    for x, y in emociones.items():
            print('\t',x + ':', y)
    show_image(picture, [rostro_joven])

def show_faceId_and_hair_color(faces): #><><><><>>><>>><<<><><>>>><>

    print('El faceId y el color de cabello de las personas son:\n')
    for face in faces:
        faceId = face['faceId']
        faceAttributes = face['faceAttributes']
        hair = faceAttributes['hair']
        hairColor = hair['hairColor']
        if len(hairColor) > 0:
            color = hairColor[0]
            color1 = color['color']
        else:
            color1 = '¡No se detecto color de cabello en esta persona!'      
        print("\nEl faceId es: ", faceId)
        print("El color del cabello es: ",color1)   

def show_accesories(faces): #>>>><<>>><<><<<><<<>>>><<<>><<><<<>>>><
    print('\n faceId y accesorios de cada persona:')
    for face in faces:
        faceId=face['faceId']
        faceAttributes=face['faceAttributes']
        accessories=faceAttributes['accessories']  
        print("\nFaceId:",faceId)  
        print('\nAccesorios:')
        if len(accessories)== 0:
            print("\t No tiene accesorios")
        else:
            for acce in accessories:
                print('\t', acce['type'])

def show_id_emotions(faces):     #<>><<<<<<><<>><<>>><<<<<<<>><>><<><
    print('el faceId y las emociones de las personas son:\n')
    for face in faces:
        faceId=face['faceId']
        faceAttributes=face['faceAttributes']  
        emotion=faceAttributes['emotion']
        print('\nfaceId:', faceId)
        print('\nEmociones:')
        for x, y in emotion.items():
            print('\t',x + ':', y) 



if __name__ == "__main__":  
    picture = input("Introduzca el path de la imagen: ")
    information=emotions(picture)
    hist=historial_consultas(information) #////
    young_emotions_rec(picture, hist)   #////
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
    #<>>><><<<<<<>>>>><<<<<>>><<<>><<<<>><<<>><<<>>>
    show_age_and_gender_quick(information) #////
    blonde_female(information) #/////
    show_image(picture, information)#////
    glasses_ungry(information) #><<<<<
    show_faceId_and_hair_color(information)
    show_id_emotions(information) 