def check_sums():
    import math

    # Четем стойността на n
    n = int(input())

    # Създаваме празни списъци за двете групи от числа
    left_numbers = []
    right_numbers = []


    # Четем първите n числа
    for i in range(n):
        number = int(input())
        left_numbers.append(number)

    # Четем следващите n числа
    for i in range(n):
        number = int(input())
        right_numbers.append(number)

    # Изчисляваме сумата на всяка група
    left_sum = sum(left_numbers)
    right_sum = sum(right_numbers)

    # Проверяваме дали двете суми са равни
    if left_sum == right_sum:
        print(f"Yes, sum = {left_sum}")
    else:
        diff = abs(left_sum - right_sum)
        print(f"No, diff = {diff}")


# Извикваме функцията
check_sums()
