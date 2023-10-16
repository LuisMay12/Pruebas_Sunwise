import random

def find_direction(N, M):
    if N >= M:
        if N % 2 == 0:
            return "L"
        else:
            return "R"
    else:
        if N % 2 == 0:
            return "U"
        else:
            return "D"

# PRUEBAS RANDOM
T = random.randint(1, 5000)

print(f"Número prueba: {T}\n")

# RESPUESTAS
respuestas = []

# CASOS RANDOM
for _ in range(T):
    N = random.randint(1, 10**9) 
    M = random.randint(1, 10**9)
    respuestas.append(find_direction(N, M))
    print(f"Caso de prueba: N = {N}, M = {M}, Dirección: {respuestas[-1]}")

