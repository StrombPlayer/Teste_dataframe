def primeira_parte(mix, numbers_list, formatted_numbers, fixed_pattern):
    for number_30 in range(30):
        mix += 1
        numbers_list.append(mix)
    for number in numbers_list:
        string_format = str(number)
        formatted_numbers.append(fixed_pattern + string_format)
        print(formatted_numbers)

def segunda_parte(mix, numbers_list, formatted_numbers, fixed_pattern):
    for number_30 in range(30):
        mix += 10000
        numbers_list.append(mix)
    for number in numbers_list:
        string_format = str(number)
        formatted_numbers.append(fixed_pattern + string_format)
        print(formatted_numbers)

def terceira_parte(mix, numbers_list, formatted_numbers, fixed_pattern):
    for number_30 in range(2):
        mix += 10000000000
        numbers_list.append(mix)
    for number in numbers_list:
        string_format = str(number)
        formatted_numbers.append(fixed_pattern + string_format)
        print(formatted_numbers)

def quarta_parte(mix, numbers_list, formatted_numbers, fixed_pattern):
    for number_30 in range(30):
        mix += 1000000000000
        numbers_list.append(mix)
    for number in numbers_list:
        string_format = str(number)
        formatted_numbers.append(fixed_pattern + string_format)
        print(formatted_numbers)