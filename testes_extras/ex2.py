def isPalindrome(x):
    #x = x.casefold()
    rev_str = reversed(x)
    if list(x) == list(rev_str):
      print("It is palindrome")
      return True
    else:
     print("It is not palindrome")
     return False

isPalindrome("SSAASS")