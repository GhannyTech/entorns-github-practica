# Llista original que cal modificar
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bucle per validar que el número introduït sigui un enter positiu (> 0)
while True: 
    try: 
        numero = int(input("Introdueix un número enter positiu: ")) 
        if numero > 0: 
            break # Si és correcte, sortim del bucle de validació        
        else: 
            print("El número ha de ser positiu (major que 0).") 
    except ValueError: 
        print("Això no és un número enter vàlid. Torna-ho a intentar.")
        
# Bucle for utilitzant range() per modificar la llista original mitjançant el seu índex
for i in range(len(llista)): 
    llista[i] += numero
    
# Mostrem el resultat final de la llista modificada
print("La llista modificada és:", llista)