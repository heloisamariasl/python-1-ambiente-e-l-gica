def area_circulo(raio): 
    n = 3.14159
    area = n* raio* raio
    print(f"A={area:.4f}")

raio = float(input())
area_circulo(raio)