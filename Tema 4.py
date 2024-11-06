import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial
print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este: " + " ".join(progres))

# Buclă principală de joc
while "_" in progres and incercari_ramase > 0:
    # Cererea unei litere
    litera = input("\nIntrodu o literă: ").lower()

    # Verificarea validității literei
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue

    # Verificarea dacă litera a fost deja încercată
    if litera in litere_incercate:
        print("Ai mai încercat deja această literă.")
        continue

    # Adăugarea literei în lista celor încercate
    litere_incercate.append(litera)

    # Verificarea literei în cuvânt
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Bine ai ghicit!")
    else:
        incercari_ramase -= 1
        print(f"Litera nu se află în cuvânt! Mai ai {incercari_ramase} încercări.")

    # Afișarea progresului și încercărilor rămase
    print("Progres: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")

# Încheierea jocului
if "_" not in progres:
    print("\nFelicitări! Ai ghicit cuvântul: " + cuvant_de_ghicit)
else:
    print(f"\nAi pierdut! Cuvântul era: {cuvant_de_ghicit}")
