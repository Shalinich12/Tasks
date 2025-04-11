def is_palindrome(n):
    n = n.lower()
    word = n[::-1]
    if n == word:
        return True
    else:
        return False


print(is_palindrome("madam"))
print(is_palindrome("shalini"))