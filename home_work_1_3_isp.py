def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low

def main():
    user_input = input("Введите последовательность чисел через пробел: ")
    sequence = list(map(int, user_input.split()))
    sequence.sort()

    user_number = int(input("Введите любое число: "))

    if user_number < sequence[0] or user_number > sequence[-1]:
        print("Число не соответствует условию")
    else:
        position = binary_search(sequence, user_number)
        print(f"Номер позиции элемента: {position}")

if __name__ == "__main__":
    main()