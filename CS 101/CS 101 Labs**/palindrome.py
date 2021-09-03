def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while (left < right):
        if text[left] != text[right]:
            return False
        elif text[left] == text[right]:
            left += 1
            right -= 1
    return True
            

if __name__ == "__main__":
    text = input('Enter a word: ')
    if is_palindrome(text):
        print('{} is a palindrome'.format(text))
    else:
        print('{} is not a palindrome'.format(text))
