class NumberProcessor:
    def __init__(self):
        self.n = 0
        self.numbers = []

    def get_number_n(self):
        self.n = int(input("Enter a positive integer N: "))
    
    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, target):
        return [i + 1 for i in range(self.n) if self.numbers[i] == target]
    def intert_number_top(self):
        for i in range(self.n):
            num = int(input(f"Enter number {i + 1}: "))
            self.insert_number(num)
    def search_number_top(self):
        X = int(input("Enter number to search (X): "))
        num_index = self.search_number(X)
        if num_index:
            if len(num_index) > 1:
                print("Found at positions:", num_index)
            else:
                print("Found at position:", num_index)

    def main(self):
        self.get_number_n()
        self.intert_number_top()
        self.search_number_top()


if __name__ == "__main__":
    tmp = NumberProcessor()
    tmp.main()
