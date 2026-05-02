import sympy as sp

def main():
    print("=========================================")
    print("    Matrix Diagonalization Calculator    ")
    print("=========================================\n")
    
    # 1. Get Matrix Size
    while True:
        try:
            n = int(input("Enter the size of the matrix (e.g., 2 for 2x2, 3 for 3x3): "))
            if n <= 0:
                print("Matrix size must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nEnter the elements of the {n}x{n} matrix.")
    print("You can enter integers, fractions (e.g., 1/2), or even symbolic expressions.")
    
    # 2. Get Matrix Elements
    elements = []
    for i in range(n):
        row = []
        for j in range(n):
            while True:
                val_str = input(f"Enter a{i+1}{j+1}: ")
                try:
                    # sympify safely converts string to sympy expression
                    val = sp.sympify(val_str)
                    row.append(val)
                    break
                except Exception:
                    print("Invalid mathematical expression. Please try again.")
        elements.append(row)

    A = sp.Matrix(elements)
    
    print("\n=========================================")
    print("              Your Matrix A              ")
    print("=========================================")
    sp.pprint(A)
    print("\nCalculating...\n")

    # Define symbol for lambda
    lam = sp.Symbol('lambda')

    # 3. Characteristic Equation
    char_poly = A.charpoly(lam)
    char_eq = sp.Eq(char_poly.as_expr(), 0)
    
    print("-----------------------------------------")
    print("        Characteristic Equation          ")
    print("-----------------------------------------")
    print("|A - \u03bbI| = 0")
    sp.pprint(char_eq)
    print()

    # 4. Eigenvalues
    eigenvals = A.eigenvals()
    print("-----------------------------------------")
    print("              Eigenvalues                ")
    print("-----------------------------------------")
    # eigenvals is a dict: {eigenvalue: algebraic_multiplicity}
    for val, mult in eigenvals.items():
        print(f"\u03bb = {val} (Algebraic Multiplicity: {mult})")
    print()

    # 5. Eigenvectors
    eigenvects = A.eigenvects()
    print("-----------------------------------------")
    print("              Eigenvectors               ")
    print("-----------------------------------------")
    # eigenvects is a list: [(eigenvalue, algebraic_multiplicity, [eigenvectors])]
    for val, mult, vects in eigenvects:
        print(f"For \u03bb = {val}:")
        for i, v in enumerate(vects):
            print(f"  v{i+1}:")
            sp.pprint(v)
            print()

    # 6. Modal Matrix & Diagonalization
    print("-----------------------------------------")
    print("      Modal Matrix & Diagonalization     ")
    print("-----------------------------------------")
    
    if A.is_diagonalizable():
        P, D = A.diagonalize()
        
        print("Modal Matrix (P) [Columns are eigenvectors]:")
        sp.pprint(P)
        print()
        
        print("Diagonal Matrix (D) [Eigenvalues on diagonal]:")
        sp.pprint(D)
        print()
        
        print("Formula: A = P * D * P\u207B\u00B9")
        print("Or:      D = P\u207B\u00B9 * A * P")
        print()
        
        # Verification to ensure correctness
        verification = sp.simplify(P * D * P.inv())
        if verification == A:
            print("[Verification] Successful: P * D * P\u207B\u00B9 exactly matches Matrix A.")
        else:
            print("[Verification] Warning: Could not easily verify P * D * P\u207B\u00B9 = A symbolically.")
            
    else:
        print("The matrix is NOT diagonalizable.")
        print("Reason: The geometric multiplicity of at least one eigenvalue is less than its algebraic multiplicity.")
        print("(i.e., there are not enough linearly independent eigenvectors to form the Modal Matrix P).")
        
    print("\n=========================================")

if __name__ == "__main__":
    main()
