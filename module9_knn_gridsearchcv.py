import sys
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_positive_int(prompt: str) -> int:
    while True:
        try:
            v = input(prompt).strip()
            f = int(v)
            if f <= 0:
                pass
            else:
                return f
        except Exception:
            pass
        print("Please enter a positive integer.", file=sys.stderr)

def read_non_negative_int(prompt: str) -> int:
    while True:
        try:
            v = input(prompt).strip()
            f = int(v)
            if f < 0:
                pass
            else:
                return f
        except Exception:
            pass
        print("Please enter a positive integer.", file=sys.stderr)

def read_real(prompt: str) -> int:
    while True:
        try:
            v = input(prompt).strip()
            f = float(v)
            return f
        except Exception:
            pass
        print("Please enter a real number.", file=sys.stderr)

def read_dataset(count, set_name):
    xs = np.empty(count)
    ys = np.empty(count)
    for i in range(count):
        x_i = read_real(f"Enter {set_name} pair #{i+1} - x (real): ")
        y_i = read_non_negative_int(f"Enter {set_name} pair #{i+1} - y (non-negative integer): ")
        xs[i] = x_i
        ys[i] = y_i
    return xs, ys

def main():
    N = read_positive_int("Enter N (number of training pairs): ")
    x_train, y_train = read_dataset(N, "TrainS")

    M = read_positive_int("Enter M (number of test pairs): ")
    x_test, y_test = read_dataset(M, "TestS")

    if x_train.shape[0] == 0:
        print("Training set is empty.")
        return
    best_k = None
    best_acc = -1.0

    for k in range(1, N + 1):
        clf = KNeighborsClassifier(n_neighbors=k, weights='uniform', algorithm='auto')
        clf.fit(x_train.reshape(-1, 1), y_train)
        y_pred = clf.predict(x_test.reshape(-1, 1))
        acc = accuracy_score(y_test, y_pred)

        if acc > best_acc or (acc == best_acc and (best_k is None or k < best_k)):
            best_k = k
            best_acc = acc
    
    print(f"Best k: {best_k}")
    print(f"Test accuracy: {best_acc:.4f}")

    

if __name__ == "__main__":
    main()
    

