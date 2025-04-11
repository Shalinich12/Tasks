def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


result = count_vowels("Shalini")
print(result)