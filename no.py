for i in range(5): 
    meme_dict = {
        "CRINGE": "Algo excepcionalmente raro o embarazoso",
        "LOL": "Una respuesta común a algo gracioso",
        "LMAO": "si",
        "PABLO": "no",
        "yes": "no"
        }
        
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict)
    else:
        print("que pena no se ")
