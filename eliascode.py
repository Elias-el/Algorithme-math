def PGCD(a, b):
    """Calcule le PGCD de deux entiers et affiche les étapes."""
    steps = []
    while b != 0:
        q = a // b
        d = a - q * b
        steps.append((a, b, q, d))
        a, b = b, d
    return a, steps

def bezout(a, b):
    """Calcule le PGCD et les coefficients de Bézout u, v tels que PGCD = u*a + v*b."""
    if b == 0:
        return a, 1, 0 
    else:
        g, u1, v1 = bezout(b, a % b)
        u = v1
        v = u1 - (a // b) * v1
        return g, u, v

if __name__ == "__main__":
    print("=== Calcul du PGCD, coefficients de Bézout et équation diophantienne ===")
    print("Tapez 'q' ou 'stop' pour quitter.\n")

    while True:
        a_input = input("Entier a : ").strip()
        if a_input.lower() in ("q", "stop"):
            print("Fin du programme.")
            break

        b_input = input("Entier b : ").strip()
        if b_input.lower() in ("q", "stop"):
            print("Fin du programme.")
            break

        c_input = input("Entier c : ").strip()
        if c_input.lower() in ("q", "stop"):
            print("Fin du programme.")
            break

        try:
            a = int(a_input)
            b = int(b_input)
            c = int(c_input)
        except ValueError:
            print("Entrée invalide , veuillez entrer des nombres entiers.\n")
            continue

        g, steps = PGCD(abs(a), abs(b))
        print("\nÉtapes de l'algorithme d'Euclide :")
        for A, B, Q, R in steps:
            print(f"{A} = {B} * {Q} + {R}")
        print(f"\nPGCD({a}, {b}) = {g}")

        if g == 1:
            print("Les deux nombres sont premiers entre eux.")
        else:
            print("Les deux nombres ne sont pas premiers entre eux.")
            
        g_bz, u, v = bezout(a, b)
        print(f"\nCoefficients de Bézout : u = {u}, v = {v}")
        print(f"Vérification : {g_bz} = ({u})*{a} + ({v})*{b}")
        print("\n=== Résolution de l'équation diophantienne ===")
        if c % g != 0:
            print(f"Pas de solution entière car {g} ∤ {c}.")
        else:

            k = c // g
            x_p = u * k
            y_p = v * k
            print(f"Solution particulière : x₀ = {x_p}, y₀ = {y_p}")
            print("Solution générale :")
            print(f"x = {x_p} + ({b//g})·t")
            print(f"y = {y_p} - ({a//g})·t   ; t ∈ Z")

            print("-" * 60 + "\n")
 