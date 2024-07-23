meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            "XD" : "Es una cara somriente, el X son los ojos y el D la boca",
            "WOW" : "Sorpresa de algo",
            ":V" : " cara de indiferencia"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("el significado de",word,"es=")
    print(meme_dict[word])
else:
    print("la palabra no existe...")
