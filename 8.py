spisok = [2, 4, 6, 8, 10]
position = 4

if position < 1 or position > len(spisok):
    result = "неверная позиция"
else:

    
    result = spisok[position - 1]

print(f"Элемент в позиции {position} - число: {result}")