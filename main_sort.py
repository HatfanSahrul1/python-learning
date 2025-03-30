from simpleOperator import SimpleMath

def main():
    math = SimpleMath()

    arr = [12, 9, 2, 4, 5, 1, 0, 89, 32, 54, 6]

    for x in range(0, len(arr)):
        for y in range(x+1, len(arr)):
            if arr[x] > arr[y] :
                arr[x], arr[y] = math.Tukar(arr[x], arr[y])

    for n in arr:
        print(n)



if __name__ == '__main__':
    main()

    