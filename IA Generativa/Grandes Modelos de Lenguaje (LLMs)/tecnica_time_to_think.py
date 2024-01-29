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

text_1 = f"""
En un encantador pueblo, los hermanos Juan y Julia emprendieron una misión para buscar agua en un pozo situado en la cima de \
una colina. Mientras subían cantando alegremente, la desgracia les golpeó: Juan tropezó con una piedra y rodó \
cuesta abajo, seguido de Julia. Aunque un poco magullados, el par regresó a casa a abrazos reconfortantes. A pesar del contratiempo, \
su espíritu aventurero permaneció intacto, y continuaron explorando con alegría.
"""
# Ejemplo 1
prompt_1 = f"""
Realiza las siguientes acciones:
1 - Resume el siguiente texto delimitado por triples comillas invertidas en una sola oración.
2 - Traduce el resumen al francés.
3 - Enumera cada nombre en el resumen francés.
4 - Muestra un objeto json que contenga las siguientes claves: resumen_frances, num_nombres.
Separa tus respuestas con saltos de línea.
Texto:
```{text_1}```
"""

response = get_completion(prompt_1)
print("Respuesta para el ejemplo 1:") 
print(response.choices[0].message.content)


# Ejemplo 2
text_2 = f"""
Como ya hemos analizado, la idea de la catábasis aparece en Interstellar. Cooper se embarca en el viaje junto a su tripulación y atraviesa el agujero de gusano entrando en \
una lejana galaxia del mismo modo en el que tantos héroes clásicos se adentraron en el inframundo a modo de portal a lo desconocido con la intención de tener éxito en sus \
peligrosas empresas y regresar con vida. Un ejemplo podría ser Hércules cuando capturó a Cerbero como parte de sus doce pruebas. El viaje que emprende Cooper es espacial, \
pero tiene muchas similitudes con un viaje marítimo como el de Odiseo. Cooper navega por el espacio en su nave y va parando en los distintos planetas, viviendo aventuras y \
enfrentándose a todo tipo de problemas mientras busca una forma de solucionar el problema de la Tierra y regresar a su hogar. Remolinos, oleaje, navegación turbulenta, \
averías en la nave…, son muchos los avatares de la navegación con los que se encuentra la tripulación. Estos avatares argumentales de los relatos míticos están jalonados de \
microhistorias, que cumplen la función de pruebas.
"""

prompt_2 = f"""
Realiza las siguientes acciones:
1 - Resume el siguiente texto delimitado por triples comillas invertidas en una sola oración.
2 - Traduce el resumen al francés.
3 - Enumera cada nombre en el resumen francés.
4 - Muestra un objeto json que contenga las siguientes claves: resumen_frances, num_nombres.
Separa tus respuestas con saltos de línea.
Texto:
```{text_2}```
"""

response = get_completion(prompt_2)
print("Respuesta para el ejemplo 2:") 
print(response.choices[0].message.content)