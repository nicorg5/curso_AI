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
            {"role": "user", "content": f"{prompt}"} 
        ]
    )
    return completion 

texto = f"""
<alumno> Dime la definción de ordenador, Yoda
<yoda> Dispositivo poderoso, el ordenador es. Información procesa, lo hace. Herramienta de gran conocimiento y conectividad, es. Pantalla brillante y teclado ágil, \ 
ayuda a los usuarios en su viaje digital. Almacenamiento vasto como la galaxia, guarda datos y secretos. Con cables y señales, el mundo virtual se entrelaza. \ 
En el flujo de datos y circuitos, el ordenador revela su sabiduría, guiando a los usuarios en su búsqueda de información y comunicación. ¡Importante herramienta, el ordenador es, sí!
<alumno> Dime la definción de teléfono móvil
"""
prompt = f"""
Te proporcionaré un texto en comillas triples Tu tarea es contestar en un estilo consecuente: \"\"\"{texto}\"\"\"
"""
response = get_completion(prompt) 
print("Respuesta para texto:") 
print(response)