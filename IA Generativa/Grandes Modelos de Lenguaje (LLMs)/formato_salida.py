# Solicitar instrucciones de formateo de salida. Ejemplo

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
            {"role": "system", "content": "Eres un asistente, que realizas resúmenes concisos y proporcionas la ideas principales de un texto. \
            Estas ideas las procporciones en una lista con puntos. Finalmente agregas una conclusión general a partir de la idea principal del texto."},
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return completion

text = f"""
La inflación, en economía, es el aumento generalizado y sostenido de los precios de los bienes y servicios existentes en el mercado durante un determinado período de tiempo. Cuando el nivel general de precios sube, con cada unidad de moneda se adquieren menos bienes y servicios. Es decir, que la inflación refleja la disminución del poder adquisitivo de la moneda: una pérdida del valor real del medio interno de intercambio y unidad de medida de una economía. Una medida frecuente de la inflación es el índice de precios, que corresponde al porcentaje por año de la variación general de precios en el tiempo (el más común es el índice de precios al consumidor).
Los efectos de la inflación en una economía son diversos, y pueden ser tanto positivos como negativos. Los efectos negativos de la inflación incluyen la disminución del valor real de la moneda a través del tiempo, el desaliento del ahorro y de la inversión debido a la incertidumbre sobre el valor futuro del dinero, y la escasez de bienes. Los efectos positivos incluyen la posibilidad de los bancos centrales de los estados de ajustar las tasas de interés nominal con el propósito de mitigar una recesión y de fomentar la inversión en proyectos de capital no monetarios.
"""
prompt = f"""
Resume el texto delimitado por triples acentos graves en una sóla frase.
```{text}```
"""
response = get_completion(prompt) 
print(response.choices[0].message.content)


# Ahora un ejemplo en el que el formato de salida va a ser un diccionario de Python
def get_completion_json(prompt):
    completion = client.chat.completions.create(
        model=engine,
        messages=[
            {"role": "system", "content": "Eres un asistente, que realizas resúmenes concisos y proporcionas la ideas principales de un texto. \
            Estas ideas las proporciones en un objeto diccionario de Python con la clave 'ideas', que contendrá un str con esas ideas. Finalmente agregas una conclusión \ general a partir de la idea principal del texto y lo agregas al objeto diccionario en una clave llamada 'conclusion' "},
            {"role": "user", "content": f"{prompt}"}
        ]
    )
    return completion

text_2 = f"""
La propiedad de una vivienda probablemente marca la diferencia en este gráfico, ya que las personas en algunos países prefieren ser propietarios de su casa en  \ lugar de alquilarla. Pero esto demuestra que la casa en la que vives no es realmente una inversión porque no puedes sacar provecho de ella a menos que la vendas y te \ mudes a un lugar más barato, o decidas alquilar. Y seamos realistas, la mayoría de las personas no buscan vender su casa sólo porque su valor ha aumentado. Es una \ lástima que por una vez estemos superando a Alemania en la tabla de riqueza, pero eso no significa que tengamos más dinero para gastar.
"""
prompt = f"""
Resume el texto delimitado por triples acentos graves: ```{text_2}```
"""
response = get_completion_json(prompt) 
print(response.choices[0].message.content)