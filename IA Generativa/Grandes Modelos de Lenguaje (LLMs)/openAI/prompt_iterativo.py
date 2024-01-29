from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
from openai import OpenAI
# Configurar el motor de OpenAI

engine = "gpt-3.5-turbo"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
def get_completion(prompt):
    messages = [
        {"role": "system", "content": "Eres un especialista en marketing, tienes grandes habilidades explicando un producto para su venta, teniendo en cuenta el público objetivo."}, 
        {"role": "user", "content": prompt}] 
    response = client.chat.completions.create(
        model=engine,
        messages=messages,
        temperature=0.5, # esta es la creatividad del modelo 
    )
    return response.choices[0].message.content

patiente_electrico = f"""
1. NOMBRE DEL PRODUCTO
- Marca: XIAOMI
- Modelo: M365


2. Peso y dimensiones
- Ancho: 1080 mm
- Profundidad: 430 mm
- Altura: 1140 mm
- Ancho de plegado: 108 cm
- Profundidad de plegado: 43 cm
- Altura de plegado: 49 cm

3. Control de energía
- Potencia del motor: 250 W
- Capacidad de batería: 18650 mAh
- Tecnología de batería: Ión de litio
- Voltaje de la pila: 42 V
- Tiempo de carga: 5 h

4. Contenido del embalaje
- Incluye asiento: No

5. Características
- Código IP (International Protection): IP54
- Distancia máxima por carga: 30 km
Sistema de freno trasero: Freno de disco
Tipo de ruedas: Ruedas sólidas
Faro frontal: Sí
Tamaño de la rueda trasera (sistema imperial): 21,6 cm (8.5")
Tipo de Motor: Sin escobillas
Motor position: Rueda trasera
Tamaño de la rueda delantera (sistema imperial): 21,6 cm (8.5")
A prueba de agua: Sí
Material de las ruedas: Caucho
Tipo: atinete clásico
Velocidad máxima: 25 kmh
Peso máximo de carga: 100 kg
Plegable: Sí
Edad recomendada (mín.): 16 año(s)
Edad recomendada (máx.): 50 año(s)
Color del producto: Negro
Pantalla incorporada: No

Audiencia:
Producto dirigido a personas que tienen actividades rutinarias que les requiere un desplazamiento de distancia media, en la que ir andando resulte más de media hora y \
busquen un medio de transporte alternativo al público, como puede ser un patinete eléctrico, ya que es prático.

Prerrequisitos:
La edad y el poder econónico del cliente ya que cada producto tiene un coste de 1.150 euros"

Objetivos:
Aumentar las ventas de este producto en un 10% mensual (actualmente se venden 55 patientes eléctricos de media al mes)
"""

prompt = f"""
Tu tarea es ayudar a un equipo de marketing a crear una descripción para un sitio web de ventas \
de un producto, basándote en una ficha técnica. 
Escribe una descripción del producto con base en la información proporcionada en la ficha técnica del patinete eléctrico delimitado por triple acento grave
No incluyas datos que ya aparecen en la ficha como la duración o el código.
Usa como máximo 80 palabras. Enfócate en los conceptos relativos al uso que se le puede dar a este producto, para que resulte atractivo a la audiencia.
Ficha de curso: ```{patiente_electrico}```
"""
response = get_completion(prompt) 
print(response)