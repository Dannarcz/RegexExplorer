import re
# Números enteros (positivos y negativos)
texto = texto = """En la programación manejamos diversos tipos de datos para representar información de forma estructurada; por ejemplo, los números enteros, que pueden ser positivos o negativos como 15 o -7, y los números flotantes que incluyen decimales, como 3.14 o -0.5. Para representar estados o condiciones lógicas utilizamos valores booleanos, que solo pueden ser True o False, lo cual es útil para tomar decisiones en el código, como saber si es_valido = True. Además, trabajamos con cadenas de texto (strings), que son secuencias de caracteres encerradas entre comillas, por ejemplo, "Hola, mundo" .  Finalmente, tenemos las listas, que son colecciones ordenadas de elementos, a menudo números, como la lista [10, 20, 30]. Cada uno de estos tipos de datos nos permite almacenar y manipular información de manera específica y efectiva dentro de un programa."""
patron_enteros = r"(?<![\.\d-])-?\b\d+\b(?!\.\d)"
enteros = re.findall(patron_enteros, texto)
# Números flotantes
clave =  r"-?\b\d+\.\d+\b"
flotantes = re.findall(clave, texto)
# Booleanos (`True`/`False`)
patron_booleanos = r"\b(True|False)\b"
booleanos = re.findall(patron_booleanos, texto)
# Strings (entre comillas dobles)
patron_strings = r'"([^"]*)"'
strings = re.findall(patron_strings, texto)
# Listas de números (ejemplo: `[1, 2, 3]`)
patron_listas = r"\[(?:\s*-?\d+\s*,)*\s*-?\d+\s*\]"
listas = re.findall(patron_listas, texto)
print("Enteros encontrados:", enteros)
print("Flotantes encontrados:", flotantes)
print("Booleanos encontrados:", booleanos)
print("Strings encontrados:", strings)
print("Listas encontradas:", listas)