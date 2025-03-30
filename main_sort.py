from simpleOperator import SimpleMath

def main():
    math = SimpleMath()

    arr = [12, 9, 2, 4, 5, 1, 0, 89, 32, 54, 6]

    arr = math.BubbleSort(arr)

    for n in arr:
        print(n)



if __name__ == '__main__':
    main()

    