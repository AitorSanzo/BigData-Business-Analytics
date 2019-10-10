# Programa para interpretar la carga sentimental de tweets
from googletrans import Translator  #https://pypi.org/project/ggtrans/#files
translator = Translator()

sentimientos = open("C:/Users/aitor/Documents/FORMACIÓN/IMF Máster BIG DATA & BUSINESS ANALYTICS/1_Fundamentos de Tratamiento de Datos para Data Science/Unidad 9 - Evaluación final/Sentimientos.txt")

valores_sent = {}  # valores es un diccionario vacío. También se puede escribir: valores = dict()

for line in sentimientos:
    termino, valor = line.split("\t")  # "\t" es el delimitador de cada palabra.
    valores_sent[termino] = int(valor)
print(valores_sent.items())  # valores.items()= lista de tuplas y cada tupla es una pareja clave:valor.
print('Nº sentimientos:' ,len(valores_sent),'\nArchivo Sentimientos leído. \n' )

Tweets = open("C:/Users/aitor/Documents/FORMACIÓN/IMF Máster BIG DATA & BUSINESS ANALYTICS/1_Fundamentos de Tratamiento de Datos para Data Science/Unidad 9 - Evaluación final/salida_tweets.txt")
count = 0
Tweets_list = []
Tweet_list_2 = []
Tweets_en = []
print("Tweet:", count)
for line in Tweets:
    texto = line.split(',')  # "\t" es el delimitador de cada palabra.
    #print(texto)
    #print('Pulse INTRO para continuar...')
    #input()
    Tweets_list.append(texto)
    x = texto.pop(3)
    if "text" in x:
        print(x)
        count = count + 1
        #print(count)
        Tweet_list_2.append(x)
        #for line in Tweet_list_2:
        #    x=line.split("\t")
        #    Tweet_list_2 = Tweet_list_2.remove ("text:")
    #print('Pulse INTRO para continuar...')
    #input()
print("Total líneas:", len(Tweets_list), ";", "Total tweets:", len(Tweet_list_2))


#for linea in Tweet_list_2:

print('Pulse INTRO para continuar...')
input()

# Una vez identificado el idioma pasando el string completo, hay que pasar palabra por palabra para que
# Google Translator no deduzca más palabras que puedan falsear el "sentimiento" del tweet.
# string = u'\u307e\u3042\u3001\u305d\u3053\u3089\u8fba\u306f\u307e\u305f\uff08\u7b11\uff09'
# print('\nMuestra tweet Unicode:\t',string) # python unicode convert to Japanese character
# st = '\\u2764\\ufe0f\\u2764\\ufe0f\\u2764\\ufe0f\\u2764\\ufe0f\\u2764\\ufe0f\\ud83d\\ude4f\\ud83d\\ude4f'.decode('utf-8', "replace")
# print('\nMuestra tweet Unicode:\t',st)
#count=0
#for linea in Tweet_list_2:
    #print('linea: ', Tweet_list_2[count])

    #texto=Tweet_list_2[count]

    #print(texto)
    # Traducción tweet
    #print('Traducción: ')

    #print(translator.detect('이 문장은 한글로 쓰여졌습니다.')) # <Detected lang=ko confidence=0.27041003>
    #print(translator.translate(texto, dest='en'))

Tweets_en = [translator.translate(a,dest='en')for a in Tweet_list_2]
    # count = count + 1
for linea in Tweets_en:
    print(linea)
#  Un tweet está definido entre "text": ..... ,"source".
#  No todos los tweets están en el mismo idioma -> Necesario traducir con Translator!!!
# https://pypi.org/project/ggtrans/
# API oficial: https://cloud.google.com/translate/docs/apis

print('Pulse INTRO para continuar...')
input()

for linea in Tweet_list_2:
    texto = linea.split('\u0020')

    print(texto)
#print('EL SIGUIENTE TWEET:, 'tweet', x de un total de y,  TIENE UN SENTIMIENTO ASOCIADO DE:'valor_tweet')

# salida = {:, :, :, }

# tuplas_tweet_sent = salida.items ()
# for clave in tuplas_tweet_sent
#    print(clave, tuplas_tweet_sent [clave]
