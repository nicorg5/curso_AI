# Proyecto recomendador de películas

En este proyecto se trabaja con dos conjuntos de datos: tmdb_5000_credits.csv y tmdb_5000_movies.csv para realizar un recomendador de películas.

Se realiza un EDA, en el que destaca un filtro para obtener las películas con un número elevado de votos, ya que así se descartan las películas 'poco valoradas', y la combinación de las columnas overview, cast, genres y keywords, ya que esta combinación va a ser el dato usado para ver la similitud entre películas.

En cuanto a proceso del lenguaje natural (NPL), se realiza una tokenización de las palabras y se eliminan las stopwords.

Dado que los conjuntos de datos no tienen una review de las películas, se generan dichas reviews con la API de OpenAI. Esta generación requiere bastante tiempo (en torno a 2 horas), por ello se guardan los resultados en un .csv para no tener que ejecutar esa generación siempre. Una vez se tienen estas reviews, se realiza un análisis de sentimiento con BERT.

Por último, se genera el sistema de recomendación con el método TFIDF combinado de un cosine_similitary para buscar las películas más parecidas a la introducida por el usuario y así poder ofrecerlas como recomendación. Esto se muestra a través de una interfaz de Gradio, en la que el usuario introduce o selecciona una película, además de elegir si quiere ver la review y el sentimiento de las 10 películas que se le recomendarán, y el output obtenido serán esas películas junto a la información extra si el usuario lo desea.
