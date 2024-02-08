# Proyecto recomendador de películas

Este proyecto se centra en la creación de un recomendador de películas utilizando dos conjuntos de datos: tmdb_5000_credits.csv y tmdb_5000_movies.csv.

Comenzamos con un Análisis Exploratorio de Datos (EDA), donde se destaca un filtro para seleccionar las películas con un alto número de votos, descartando así aquellas "poco valoradas". Además, se combina la información de las columnas overview, cast, genres y keywords, ya que esta combinación servirá como base para medir la similitud entre las películas.

En el procesamiento del lenguaje natural (NLP), se realiza una tokenización de las palabras y se eliminan las llamadas "stopwords".

Dado que los conjuntos de datos no incluyen reseñas de las películas, se generan mediante la API de OpenAI. Esta tarea lleva bastante tiempo (alrededor de 2 horas), por lo que los resultados se guardan en un archivo CSV para evitar tener que generarlos cada vez. Posteriormente, se realiza un análisis de sentimientos utilizando BERT.

Finalmente, se crea el sistema de recomendación utilizando el método TFIDF combinado con la similitud del coseno para encontrar películas similares a la que el usuario introduce. Esto se presenta a través de una interfaz de Gradio, donde el usuario puede seleccionar o introducir una película y elegir si desea ver la reseña y el sentimiento de las 10 películas recomendadas. El resultado son las películas recomendadas junto con la información adicional, si el usuario así lo desea.