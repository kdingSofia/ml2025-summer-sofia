N = int(input("Enter a positive integer N: "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Enter number to search (X): "))

indices = [i + 1 for i in range(N) if numbers[i] == X]

if indices:
    if len(indices) > 1:
        print("Found at positions:", indices)
    else:
        print("Found at position:", indices)
else:
    print("-1")
