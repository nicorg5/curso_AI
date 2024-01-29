from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configurar el motor de OpenAI
engine = "gpt-3.5-turbo"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(prompt):
    completion = client.chat.completions.create(
        model=engine,
            messages=[
                {"role": "system", "content": "Eres un experto en fondos de inversión con más de 10 años de experiencia, \
                tu conocimiento se extiende por múltipleas aspectos de diferentes tipos de fondos de inversión y dispones de \
                numerosas certificaciones en este campo. Además eres experto en macroeconomía."},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
    return completion

prompt = (
f"Explica qué tipos de fondos de inversión existe, como si estuvieras enseñando a un estudiante de primer año en banca de inversión."
)
respuesta = get_completion(prompt) 
print(respuesta.choices[0].message.content)

prompt_2 = (
f"Explica la diferencia entre un fondo mixto y un fondo indexado, de manera avanzada, como si se lo estuvieses explicando a un experto en banca de inversión."
)
respuesta_2 = get_completion(prompt_2) 
print(respuesta_2.choices[0].message.content)