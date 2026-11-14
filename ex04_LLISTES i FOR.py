# Llista de mostres codificada de manera fixa
llista = ["abc", "xyz", "aba", "1221", "a"]

comptador = 0

# Recorre cada element de la llista
for paraula in llista:

    # Comprova si la longitud és igual o superior a 2 i comença per 'a'
    if len(paraula) >= 2 and paraula.startswith("a"):
        comptador += 1

print(f"Hi ha {comptador} elements")
