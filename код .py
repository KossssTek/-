
def filter_strings(input_array):
    result_array = []
    for string in input_array:
        if len(string) <= 3:
            result_array.append(string)
    return result_array

# Ввод исходного массива
initial_array = ["яблоко", "кошка", "собака", "птица", "слон", "я", "идти"]

# Вызов функции для фильтрации строк
filtered_result = filter_strings(initial_array)

# Вывод или использование отфильтрованного результата
print(filtered_result)