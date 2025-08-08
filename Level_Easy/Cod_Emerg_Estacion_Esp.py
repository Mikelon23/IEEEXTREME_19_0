#Los astronautas deben transmitir códigos en formato binario, pero la radiación cósmica invierte algunos bits. Dada una cadena binaria corrompida (donde '*' indica bits dañados), reemplaza cada '*' por '0' o '1' para que el número de '1' sea mínimo.
#Entrada:
#Cadena binaria con 0, 1 y '*' (longitud ≤ 1000).
#Salida:
#Cadena reparada con mínimo de '1'.
#Ejemplo:
#Entrada: 1*0*1*
#Salida: 100001
#Explicación: 100001 tiene solo 2 '1' (otra opción como 110011 tendría 4)
def reparar_bits(s):
    return ''.join('0' if c == '*' else c for c in s)
