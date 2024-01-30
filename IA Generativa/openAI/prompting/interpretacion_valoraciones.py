from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
from openai import OpenAI

# Configurar el motor de OpenAI
#engine = "gpt-3.5-turbo"
engine = "gpt-4"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(prompt):
    completion = client.chat.completions.create(
        model=engine,
        messages=[
            {"role": "system", "content": "Eres un asistente, que realizas resúmenes concisos y proporcionas la ideas principales de un texto."}, 
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return completion

review1 = """
He comprado hace unos días este producto y sólo puedo decir una palabra tras su uso: alucinante. 
Si quieres comprar algo que te sirva para la nada, este es el producto adecuado
"""
review2 = """
Es un patinete robusto, con potencia suficiente para ir por la ciudad.
Xiaomi es una marca de confianza.
El Corte Inglés…envío perfecto, rápido y en tiempo
"""
reviews = ' \n'.join([review1, review2])

prompt = """Tu tarea es extraer información releavante de las voloraciones de usuario \ para proporcionar feedback al departamento de logística. \
Analiza estas valoraciones, delimitadas por triples acentos diacríticos \
y elabora un feedbac de al menos 30 palabras, haciendo foco en aspectos que mencionan \ 
la logística del producto. 
Valoracoines: ```{reviews}```
"""

response = get_completion(prompt)
print(response.choices[0].message.content)