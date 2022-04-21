class Dad:
    def __init__(self, arr):
        self.arr = arr

    def date(self):
        print(self.arr, end=" ")

class Son(Dad):
    def __init__(self, arr, brr):
        Dad.__init__(self, arr)
        self.brr = brr

    def date(self):
        super().date()
        print(self.brr)

def main():
    we = Son(1000, 1)
    we.date()


if __name__ == "__main__":
    main()
