def second_largest(lst):
    unique_sets = set(lst)
    unique_lst = list(unique_sets)
    unique_lst.sort(reverse=True)
    if len(unique_lst)<2:
        return "list"
    return unique_lst[1]
print(second_largest([10,20,30,40]))
print(second_largest([3,3,3]))