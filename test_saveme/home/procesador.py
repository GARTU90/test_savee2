# 🔍 Diccionario de síntomas agrupados
categoria_sintomas = {
    "umf": [
        "diabetes", "hipertension", "resfriado", "tos", "dolor cabeza", "alergia", "mareo", "gripa", "dolor muscular", "presion alta", "control"
    ],
    "urgencias": [
        "dolor pecho", "infarto", "desmayo", "convulsion", "sangrado", "fiebre alta", "accidente", "perdida conciencia", "dificultad respirar",
        "brazo dormido", "dolor corazon", "vomito sangre"
    ],
    "especialidad_privada": [
        "dermatologo", "fertilidad", "trastorno", "psiquiatra", "ansiedad", "depresion", "neurologo", "piel", "caida cabello"
    ],
    "hospital_privado": [
        "hospital privado", "atencion privada", "urgencia privada"
    ]
}

def preprocesar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    palabras = nltk.word_tokenize(texto, language='spanish')
    stop_words = set(stopwords.words('spanish'))
    stemmer = SnowballStemmer('spanish')
    return [stemmer.stem(palabra) for palabra in palabras if palabra not in stop_words]

def procesar_respuesta(problema):
    texto = preprocesar_texto(problema)
    texto_union = " ".join(texto)

    for categoria, sintomas in categoria_sintomas.items():
        for sintoma in sintomas:
            if sintoma in texto_union:
                return categoria  # Devuelve la primera coincidencia encontrada

    return "umf"  # Por defecto, si no detectamos nada grave, va a UMF
