def  reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_words(s):
    return len(s.split())
