frase = "manzanas_amarillas_de_ana"

# Contar letras
def contar_letras(frase):
    contador = {}
    for letra in frase:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

# Organizar letras de mayor a menor
def ordenar_letras(contador):
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)

# Reescribir la frase usando bits revisando la posicion de cada letra ordenada
def reescribir_frase(frase, letras_ordenadas, contador):
    bits = ""
    for letra in frase:
        index = letras_ordenadas.index((letra, contador[letra]))
        # agregar un cero por la cantidad que tiene index
        while index > 0:
            index -= 1
            bits += '0'
        bits += '1'  # agregar un uno al final
    return bits

# convertir bits a string
def bits_a_string(bits):
    resultado = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')  # Rellenar con ceros si es necesario
        resultado += chr(int(byte, 2))
    return resultado


letras_contadas = contar_letras(frase)
frase_ordenada = ordenar_letras(letras_contadas)
frase_en_bits = reescribir_frase(frase, frase_ordenada, letras_contadas)
frase_comprimida = bits_a_string(frase_en_bits)
print("Frase original:", frase)
print("Frase comprimida:", frase_comprimida)

# convetir string a bits
def string_a_bits(frase):
    bits = ""
    for char in frase:
        bits += format(ord(char), '08b')  # Convertir cada caracter a su representación binaria de 8 bits
    return bits

# Recontruir la frase original a partir de los bits, con la posicion del 1
def reconstruir_frase(bits, letras_ordenadas):
    frase_reconstruida = ""
    index = 0
    for bit in bits:
        if bit == '1':
            letra = letras_ordenadas[index][0]
            frase_reconstruida += letra
            index = 0
        else:
            index += 1  # Mover al siguiente índice
    return frase_reconstruida

frase_comprimida_en_bits = string_a_bits(frase_comprimida)
frase_reconstruida = reconstruir_frase(frase_en_bits, frase_ordenada)
print("Frase reconstruida:", frase_reconstruida)