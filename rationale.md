El funcionamiento del script está contenido en OpenIA_Grobid.py desde el cual se hace las llamadas necesarias a grobid para poder generar los ficheros .xml necesarios para la lectura de los documentos.

Utilizando las funciones findall() del modulo xml.etree.ElementTree podemos recorrer todo el árbol en búsqueda del tag necesario, en este caso
Acceder al elemento abstract  el cual contiene el elemento p donde están contenido el texto , usando el modulo Wordcloud podemos pasarle el texto
para generar la nube de palabras que se guardara en el directorio

Filtrando esta vez por el elemento figure obtenemos el numero de imagenes por documento , el resultado se mostrara por pantalla

Y por ultimo filtrando por todos los elementos de texto p y filtrando mediante una expresion regular obtenemos todos los links , el resultado
se mostrara por pantalla
