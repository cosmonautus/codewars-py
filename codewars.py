import os

##############################################################
# https://www.codewars.com/kata/rgb-to-hex-conversion/python
##############################################################
def rgb(r, g, b):
    def check(v):
        return min(255, max(v, 0))
    return ("{:02X}" * 3).format(check(r), check(g), check(b))


##############################################################
# https://www.codewars.com/kata/find-the-odd-int/train/python
##############################################################
def find_it(seq):
    for v in seq:
        if seq.count(v) % 2 != 0:
            return v
    return None


##############################################################
# https://www.codewars.com/kata/valid-braces/train/python
##############################################################
def validBraces(string):
    stack = []
    braces = {'(': ')', '{': '}', '[': ']'}
    for ch in string:
        if ch in braces:
            stack.append(braces[ch])
        else:
            if len(stack) == 0 or stack.pop() != ch:
                return False
    return len(stack) == 0

def validBraces2(string):
    while '{}' in string or '[]' in string or '()' in string:
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        string = string.replace('()', '')
    return len(string) == 0

##############################################################
# https://www.codewars.com/kata/longest-palindrome/train/python
##############################################################

def longest_palindrome (s):
    if len(s) == 1:
        return 1
    result = 0
    def _is_palindrome(_s):
        return _s == _s[-1::-1]
    for offs in range(len(s) - 1):
        to = len(s)
        while to - offs > result:
            if _is_palindrome(s[offs:to]):
                result = to - offs
                break
            to -= 1
    return result


def longest_palindrome2 (s):
    def _is_palindrome(_s):
        return _s == _s[-1::-1]
    result = 0
    for left in range(len(s)):
        for right in range(len(s), left, -1):
            if _is_palindrome(s[left:right]):
                result = max(right-left, result)
    return result

##############################################################
# https://www.codewars.com/kata/mexican-wave/train/python
##############################################################
def wave(s):
    result = []
    for i in range(len(s)):
        if s[i].isalpha():
            result.append(s[:i] + s[i].upper() + s[i + 1:])
    return result

def wave2(s):
    return [s[:i] + s[i].upper() + s[i + 1:] for i in range(len(s)) if s[i].isalpha()]


##############################################################
# https://www.codewars.com/kata/roman-numerals-encoder/train/python
##############################################################
def RomanEncoder(n):
    result = ""
    roman = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    for k in roman.keys():
        while n >= k:
            n -= k;
            result += roman[k];
    return result

##############################################################
# Get all files in a folder and subfolders
##############################################################
def getMediaFilesList(folder):
    file_paths = []
    for root, directories, files in os.walk(folder):
        for filename in files:
            if ".jpg" in filename.lower() or ".png" in filename.lower() or ".tif" in filename.lower():
                # Save full file path
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    return file_paths

##############################################################

print(rgb(255, 100, 0))
print(rgb(-155, 100, 0))
print(rgb(285, 300, 0))
print(rgb(255, 100, 0))
print(rgb(15, 10, 0))
print(rgb(1, 2, 15))
print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(validBraces2("[{[()]}{[()]}{[()]}]"))
#print(getMediaFilesList("d:\Downloads"))
print(longest_palindrome2("baablkj12345432133d"))
print(wave2("mexican waves!"))
print(RomanEncoder(3472)) # MMMCDLXXII
