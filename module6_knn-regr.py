import sys
import numpy as np

class KNN:
    def __init__(self, x_values, y_values):
        if x_values.shape != y_values.shape:
            sys.exit("X and Y do not have same shape.")
        self.x = x_values.astype(float)
        self.y = y_values.astype(float)
        self.n = self.x.size

    def predict(self, x_query: float, k: int) -> float:
        if k <= 0:
            sys.exit("k must be a positive integer.")
        if k > self.n:
            sys.exit("k cannot be greater than the number of points (N).")
        dists = np.abs(self.x - x_query)
        # get ids with k smallest distance
        idx = np.argpartition(dists, k - 1)[:k]
        return float(np.mean(self.y[idx]))

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
        xinput = float(input("Enter query X (real number): ").strip())
    except:
        sys.exit("Error: please enter a real number")
    model = KNN(xs, ys)
    y_pred = model.predict(xinput, k)
    print(y_pred)

    
if __name__ == "__main__":
    main()
