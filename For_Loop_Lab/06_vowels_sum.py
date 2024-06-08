def calculate_vowel_value(text):
    # Създаваме речник със стойностите на гласните букви
    vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

    # Инициализираме сумата
    total_sum = 0

    # Преглеждаме всеки символ в текста
    for char in text:
        # Превръщаме символа в малка буква, за да се справим с главни букви
        lower_char = char.lower()

        # Ако символът е гласна буква, добавяме стойността му към сумата
        if lower_char in vowel_values:
            total_sum += vowel_values[lower_char]

    return total_sum


# Четем текст от потребителя
user_input = input()

# Изчисляваме сумата от стойностите на гласните букви
result = calculate_vowel_value(user_input)

# Отпечатваме резултата
print(f"{result}")