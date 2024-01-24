def arrondir(x):
    x = x + 0.5
    arrondi = int(x)

    return arrondi


x, y = 0.6, 3.1
arr1 = arrondir(1.4)
arr2 = arrondir(x + y)
arr3 = arrondir(-x) + arrondir(y)

print(arr1, arr2, arr3)
