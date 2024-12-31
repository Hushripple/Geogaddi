# Geogaddi

Programa básico hecho en Tkinter que busca poder descargar videos, música, álbumes, entre otras cosas de diferentes plataformas.

Existen muchas herramientas de este tipo y esta no tiene ninguna particularidad, de hecho, su existencia es meramente para cubrir necesidades personales y practicar la creación de software con Tkinter.

bandcamp-dl es necesario para poder descargar cosas de Bandcamp. 

```pip install bandcamp-downloader```

yt-dlp es necesario para poder descargar cosas de YouTube.

```pip install yt-dlp```

# Consideraciones

- bandcamp-dl descarga las canciones a 128kbs, así que es recomendable utilizar la opción de descarga de la propia página de Bandcamp si se quiere descargar un álbum gratuito.
- bandcamp-dl se encarga de todos los metadatos, tanto tags para los archivos mp3 como la portada del álbum.
- yt-dlp utiliza el comando "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", lo cual hace que SIEMPRE se descargue siempre el vídeo en la mejor calidad de vídeo y audio posible. Es de esperarse que los archivos puedan pesar mucho dependiendo de su duración y en su calidad máxima.

# Futuro

Tengo planes para hacer que este programa funcione perfectamente tanto en Windows como en Linux, pero por el momento este «proyecto» está en una fase muy temprana y probablemente tardará mucho tiempo.

# Estado

Por el momento sólo se pueden descargar vídeos de YouTube y álbumes de Bandcamp. 

TODO:

- ~~Arreglar que los videos siempre se descarguen en muy baja calidad.~~
- ~~Arreglar que realmente no se pueda seleccionar la ruta de descarga al descargar desde Bandcamp.~~
- Descargar canciones/listas desde Soundcloud.
- Descargar álbumes desde Spotify
- Descargar vídeos y gifs de Twitter
- Descargar vídeos de Instagram
 
