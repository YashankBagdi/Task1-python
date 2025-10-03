def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        return "Cannot multiply ."
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A): 
                C[i][j] += A[i][k] * B[k][j]
    return C
def print_matrix(matrix):
    for row in matrix:
        print(row)
print("Enter matrices. Eg: [[1, 2], [3, 4]] ")
try:
    matrix_A_input = input("Enter matrix A: ")
    A = eval(matrix_A_input)
    matrix_B_input = input("Enter matrix B: ")
    B = eval(matrix_B_input)
    result = multiply_matrices(A, B)
    print("Resulting Matrix:")
    if isinstance(result, str):
        print(result)
    else:
        print_matrix(result)
except (SyntaxError, NameError):
    print("Invalid input format. Please enter a valid list of lists.")
except Exception as e:
    print(f"An error occurred: {e}")
