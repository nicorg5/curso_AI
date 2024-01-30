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


# Ejemplo en el que el formato de salida van a ser instrucciones. Se usa una receta como input y se espera que el output sean los pasos de la misma
def get_completion_pasos(prompt):
    completion = client.chat.completions.create( 
        model=engine,
        messages=[
            {"role": "user", "content": f"{prompt}"} ]
        )
    return completion 
receta = f"""
Mezcla en un tazón apto para microondas 4 cucharadas de azúcar, 2 cucharadas de harina, 2 cucharadas de cacao puro en polvo, una \ pizca de sal y 1/4 de cucharadita de levadura. Añade un huevo batido y 2 cucharadas de aceite de oliva. Remueve bien hasta \ obtener una masa uniforme. Si deseas, puedes agregar chispas de chocolate o nueces al gusto. Una vez mezclado, aplana la \ superficie con una cuchara. Cocina en el microondas a máxima potencia durante aproximadamente 1 minuto. Mantén un ojo en él \ microondas para evitar que se reseque. Deja enfriar un poco antes de comer, ya que estará muy caliente.
"""
prompt = f"""
Te proporcionaré un texto en comillas triples
Si contiene una secuencia de instrucciones, \
re-escribe esas instrucciones en el siguiente formato:
Paso 1 - ...
Paso 2 - …
…
Paso N - …
Si el texto no contiene una secuencia de instrucciones, \ entonces simplemente escribe \"No se proporcionan instrucciones.\" \"\"\"{receta}\"\"\"
"""
response = get_completion_pasos(prompt)
print("Respuesta para receta:") 
print(response.choices[0].message.content)


# Ejemplo de uso de get_completion_pasos para que devuelva "No se proporcionan instrucciones"
texto = f"""
En un día cálido de primavera, el prado se despliega como un tapiz de flores silvestres, \ pintando el campo con pinceladas de amarillo, rosa y azul. El aire está impregnado del \
dulce aroma de la lavanda y el jazmín. El lindero del bosque cercano proporciona un contraste \ sereno, con sus árboles altos y robustos que parecen susurrar secretos con el viento. La brisa \ suave acaricia tu piel, invocando una sensación de paz inmediata. El trino de los pájaros \
se mezcla con el murmullo de un arroyo cercano, creando una sinfonía natural que parece celebrar \ la renovación de la vida. El mundo aquí es un remanso de tranquilidad y belleza simple.
"""
prompt = f"""
Te proporcionaré un texto en comillas triples
Si contiene una secuencia de instrucciones, \
re-escribe esas instrucciones en el siguiente formato:
Paso 1 - ...
Paso 2 - …
…
Paso N - …
Si el texto no contiene una secuencia de instrucciones, \ entonces simplemente escribe \"No se proporcionan instrucciones.\" \"\"\"{texto}\"\"\"
"""
response = get_completion_pasos(prompt) 
print("Respuesta para texto:") 
print(response)