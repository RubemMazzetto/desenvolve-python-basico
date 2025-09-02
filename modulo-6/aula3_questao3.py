import random

def find_max_negative_interval(numbers):
    max_neg_count = 0
    start_idx = 0
    end_idx = 0
    current_neg_count = 0
    current_start = 0

    for i in range(len(numbers)):
        if numbers[i] < 0:
            current_neg_count += 1
        else:
            if current_neg_count > max_neg_count:
                max_neg_count = current_neg_count
                start_idx = current_start
                end_idx = i
            current_neg_count = 0
            current_start = i + 1
    if current_neg_count > max_neg_count:
        start_idx = current_start
        end_idx = len(numbers)
    return start_idx, end_idx

original_list = [random.randint(-10, 10) for _ in range(20)]

start, end = find_max_negative_interval(original_list)
edited_list = original_list.copy()
del edited_list[start:end]

print("Original:", original_list)
print("Editada:", edited_list)