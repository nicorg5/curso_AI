# Destacar o referenciar partes destacadas del input. Ejemplo

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
            {"role": "system", "content": "Eres un asistente, que realizas resúmenes concisos y proporcionas la ideas principales de un texto."}, 
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