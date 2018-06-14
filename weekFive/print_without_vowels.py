def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    new_str = ''
    for letter in s:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_str += letter
    print(new_str)

print_without_vowels("This is great!")