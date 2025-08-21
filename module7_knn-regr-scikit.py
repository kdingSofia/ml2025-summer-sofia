import sys
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = 0
    try:
        N = int(input("Enter N (positive integer): ").strip())
    except:
        sys.exit("please enter a integer.")
    if N <=0:
        sys.exit("please enter a positive integer.")

    k = 0
    try:
        k = int(input("Enter k (positive integer): ").strip())
    except:
        sys.exit("please enter a integer.")
    if k <=0:
        sys.exit("please enter a positive integer.")

    xs = np.empty(N, dtype=float)
    ys = np.empty(N, dtype=float)

    for i in range(N):
        try:
            xi = float(input(f"  x[{i+1}]: ").strip())
            yi = float(input(f"  y[{i+1}]: ").strip())
        except:
            sys.exit("Error: please enter a real number")
        xs[i] = xi
        ys[i] = yi
    try:
        xinput = np.array([[float(input("Enter query X (real number): ").strip())]])
    except:
        sys.exit("Error: please enter a real number")
    # model = KNN(xs, ys)
    model = KNeighborsRegressor(n_neighbors=k)
    # ValueError: Expected 2D array, got 1D array instead:
    X_train = xs.reshape(-1, 1)
    model.fit(X_train, ys)
    y_pred = model.predict(xinput)[0]

    print(f"k-NN Regression prediction at X={xinput}: {y_pred}")
    print(f"Variance of labels (sample): {np.var(ys)}")

    print(y_pred)

    
if __name__ == "__main__":
    main()