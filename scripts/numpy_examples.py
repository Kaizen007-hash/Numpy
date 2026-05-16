"""Cleaned examples extracted from Numpy.ipynb

Run as a script to execute grouped examples.
"""
from __future__ import annotations

import numpy as np
import math
import datetime
try:
    from scipy import linalg as scipy_linalg
    from scipy import sparse as scipy_sparse
except Exception:
    scipy_linalg = None
    scipy_sparse = None
try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None
try:
    import pandas as pd
except Exception:
    pd = None


def vector_ops():
    print("--- Vector operations ---")
    u = np.array([1, 2])
    v = np.array([3, 4])
    print("u+v =>", u + v)
    alpha = 3
    v2 = np.array([2, -1])
    print("alpha * v =>", alpha * v2)
    print("dot(u, v) =>", np.dot(u, v))
    u3 = np.array([1, 0, 0])
    v3 = np.array([0, 1, 0])
    print("cross(u3, v3) =>", np.cross(u3, v3))
    print("norm([3,4]) =>", np.linalg.norm(np.array([3, 4])))


def matrix_ops():
    print("--- Matrix operations ---")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("A + B:\n", A + B)
    print("A * 2:\n", 2 * A)
    print("A.T:\n", A.T)
    print("A @ B:\n", A.dot(B))
    print("det(A):", np.linalg.det([[3, 8], [4, 6]]))
    try:
        invA = np.linalg.inv(np.array([[4, 7], [2, 6]]))
        print("inv(A):\n", invA)
    except np.linalg.LinAlgError:
        print("Matrix not invertible")


def linear_algebra_examples():
    print("--- Linear algebra examples ---")
    A = np.array([[2, 1], [1, 3]])
    b = np.array([5, 7])
    det_A = np.linalg.det(A)
    print("det(A):", det_A)
    if det_A != 0:
        # Cramer's rule
        A_x = A.copy()
        A_x[:, 0] = b
        A_y = A.copy()
        A_y[:, 1] = b
        x = np.linalg.det(A_x) / det_A
        y = np.linalg.det(A_y) / det_A
        print(f"Cramer's rule solution: x={x}, y={y}")


def elementwise_and_products():
    print("--- Elementwise and outer products ---")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Hadamard (elementwise):\n", np.multiply(A, B))
    u = np.array([1, 2])
    v = np.array([3, 4, 5])
    print("outer(u, v):\n", np.outer(u, v))
    print("kron(A, B):\n", np.kron(A, B))


def norms_and_trace():
    print("--- Norms and trace ---")
    A = np.array([[1, 2], [3, 4]])
    print("Frobenius norm:", np.linalg.norm(A, 'fro'))
    X = np.array([1, 1])
    left = np.linalg.norm(A.dot(X))
    right = np.linalg.norm(A) * np.linalg.norm(X)
    print("Operator inequality: left <= right =>", left <= right)
    print("trace(AB) == trace(BA):", np.trace(A.dot(A)) == np.trace(A.dot(A)))


def block_and_kronecker():
    print("--- Block and Kronecker examples ---")
    A11 = np.array([[1, 2], [3, 4]])
    A12 = np.array([[5, 6], [7, 8]])
    A21 = np.array([[9, 10], [11, 12]])
    A22 = np.array([[13, 14], [15, 16]])
    B11 = np.array([[17, 18], [19, 20]])
    B12 = np.array([[21, 22], [23, 24]])
    B21 = np.array([[25, 26], [27, 28]])
    B22 = np.array([[29, 30], [31, 32]])
    C11 = A11.dot(B11) + A12.dot(B21)
    C12 = A11.dot(B12) + A12.dot(B22)
    C21 = A21.dot(B11) + A22.dot(B21)
    C22 = A21.dot(B12) + A22.dot(B22)
    C = np.block([[C11, C12], [C21, C22]])
    print("Block product shape:", C.shape)


def plotting_examples():
    if plt is None:
        print("matplotlib not available — skipping plotting examples")
        return
    print("--- Plotting example (sine) ---")
    X = np.linspace(-10, 10, 100)
    Y = np.sin(X)
    plt.plot(X, Y, marker='+', color='purple')
    plt.title('Sine wave')
    plt.show()


def pandas_example():
    if pd is None:
        print("pandas not available — skipping DataFrame example")
        return
    print("--- Pandas DataFrame example ---")
    data = {
        'Name': ["John", "Anna", "Peter", "Linda", "Samuela", "George", "Jon Snow"],
        'Location': ["New York", "Paris", "Berlin", "London", "Japan", "Ghana", "Winterfell"],
        'Age': [24, 13, 53, 33, 36, 39, 40],
        'Occupation': ["Engineer", "Nurse", "Trader", "Consultant", "Professor", "Pilot", "Doctor"],
    }
    df = pd.DataFrame(data)
    print(df.to_string(index=False))


def misc_examples():
    print("--- Misc examples ---")
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([1.0, 2.00001, 2.99999])
    print("isclose(a,b):", np.isclose(a, b))
    now = datetime.datetime.today()
    print("Today's date:", now.strftime('%A %B %d %Y %H:%M:%S'))


def main():
    vector_ops()
    matrix_ops()
    linear_algebra_examples()
    elementwise_and_products()
    norms_and_trace()
    block_and_kronecker()
    pandas_example()
    misc_examples()
    # plotting_examples()  # Uncomment to run plotting examples


if __name__ == '__main__':
    main()
