numbers = [2, 4, 6, 8, 12, 16]
if len(numbers) == 0:
    result = None
else:
    ch = 0
    for num in numbers:
        ch += 1 / num
    result = len(numbers) / ch

print("Среднее гармоническое значение элементов:", result)