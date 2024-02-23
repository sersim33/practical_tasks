
def all_sub_lists(data):
    sub_lists = [[]]  # Початковий список з порожнім підсписком
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            sub_lists.append(data[i:j])  # Додаємо всі підсписки від індексу i до j
    return sub_lists

# Приклад використання:
input_list = [4, 6, 1, 3]
result = all_sub_lists(input_list)
print(result)