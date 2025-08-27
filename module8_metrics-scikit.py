import sys
import numpy as np
from sklearn.metrics import precision_score, recall_score


class BinaryPairs:
    def __init__(self, n):
        self.n = n
        self.x_true = np.empty(n)   # ground-truth labels (X)
        self.y_pred = np.empty(n)   # predicted labels (Y)

    def read_bit(self, prompt: str) -> int:
        while True:
            try:
                v = input(prompt).strip()
                if v in ("0", "1"):
                    return int(v)
                f = float(v)
                if f in (0.0, 1.0):
                    return int(f)
            except Exception:
                pass
            print("Please enter 0 or 1.", file=sys.stderr)

    def fill(self):
        for i in range(self.n):
            x_i = self.read_bit(f"Point {i+1}/{self.n} — enter X (ground truth, 0 or 1): ")
            y_i = self.read_bit(f"Point {i+1}/{self.n} — enter Y (prediction, 0 or 1): ")
            self.x_true[i] = x_i
            self.y_pred[i] = y_i

N = 0
try:
    N = int(input("Enter N (positive integer): ").strip())
except:
    sys.exit("please enter a integer.")
if N <=0:
    sys.exit("please enter a positive integer.")


data = BinaryPairs(N)
data.fill()

precision = precision_score(data.x_true, data.y_pred, zero_division=0)
recall = recall_score(data.x_true, data.y_pred, zero_division=0)

print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
