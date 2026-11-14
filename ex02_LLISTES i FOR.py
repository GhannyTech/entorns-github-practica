# 1. Validar la mida de la llista (entre 2 i 10)
while True: 
    try: 
        mida = int(input("Introdueix la mida de la llista (entre 2 i 10): ")) 
        if 2 <= mida <= 10: 
            break 
        else: 
            print("Error: La mida ha d'estar entre 2 i 10.") 
    except ValueError: 
        print("Error: Introdueix un número enter vàlid.")
        
# 2. Omplir la llista assegurant que s'introdueixen nombres
llista_usuari = []
for i in range(mida): 
    # Bucle while anuat per validar cada element individualment    
    while True: 
        try:  
            element = float(input(f"Introdueix el número per a la posició {i+1}: ") )
            llista_usuari.append(element) 
            break
        except ValueError: 
            print("Error: Has d'introduir un número vàlid.")
            
# Mostrem la llista creada per pantalla
print("\nLlista entrada:", llista_usuari)

# 3. Calcular la suma i la multiplicació de tots els elements
suma_total = 0
multiplicacio_total = 1

for num in llista_usuari: 
    suma_total += num 
    multiplicacio_total *= num
    
# Mostrar els resultats finals
print(f"El resultat de sumar és: {suma_total}")
print(f"El resultat de multiplicar és: {multiplicacio_total}")