def a(nums):
    max_nums = []
    max_index = []

    max_value = max(nums)
    for i, num in enumerate(nums):
        if num == max_value:
            max_index.append(i)

    if len(max_index) < 2:
        return []

    start_index = min(max_index)

    end_index = max(max_index)

    return nums[start_index + 1:end_index]


spisok = [5, 3, 9, 7, 2, 9, 6, 1, 9]
result = a(spisok)
print(result)