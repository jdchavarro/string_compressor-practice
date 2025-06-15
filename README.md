# Compresión de texto simple en Python

Este proyecto fue creado como respuesta a un reto durante el curso de **Fundamentos de Ingeniería de Software** de [Platzi](https://platzi.com/). En una de las clases, el profesor **Freddy Vega** propuso implementar un algoritmo de compresión de texto, y este es el resultado.

## Descripción

El script implementa una técnica de compresión personalizada inspirada en la codificación por frecuencias. La lógica consiste en:

1. **Contar la frecuencia de cada letra** en una frase de entrada.
2. **Ordenar las letras** por frecuencia (de mayor a menor).
3. **Codificar la frase original** usando una representación binaria donde:
   - Cada letra se representa por una secuencia de ceros seguida de un uno (`000...1`), donde el número de ceros depende de su posición en el ranking de frecuencia.
4. **Convertir la cadena de bits en caracteres ASCII** para "comprimir" la frase en texto imprimible.
5. **Reconstruir la frase original** a partir de la cadena comprimida y la tabla de frecuencias.

> ⚠️ Este algoritmo es experimental y no garantiza compresión real ni eficiencia. Es un ejercicio educativo para entender cómo funcionan las representaciones binarias y la codificación basada en frecuencia.

## Ejemplo

Entrada original:

```
"manzanas_amarillas_de_ana"
```

Salida comprimida en caracteres

```
"Âc
                    $&À"
```

## Archivos

- `compressor_and_decompressor.py`: Contiene toda la lógica de compresión y descompresión.
- `README.md`: Este archivo con la explicación del proyecto.

## Cómo usarlo

1. Asegúrate de tener Python 3 instalado.
2. Clona este repositorio.
3. Ejecuta el archivo con:

```bash
> python3 compressor_and_decompressor.py
```

## Próximos pasos (opcional)

- Implementar una estructura de árbol para simular Huffman real.
- Medir el nivel real de compresión.
- Adaptar para otros alfabetos o archivos completos.
