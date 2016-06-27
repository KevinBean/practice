# coding=utf-8
import random, string
'''简单做法
+f = open('Promo_code.txt', 'wb')
 +for i in range(200):
 +    chars = string.letters + string.digits
 +    s = [random.choice(chars) for i in range(10)]
 +    f.write(''.join(s) + '\n')
 +f.close()
'''
# random 库中的 randint(inf, sup) 函数可以在指定的范围内产生一个随机整数；choice(sequence) 可以在一个有序的类型中（比如 list、tuple 或 string）随机选取一个元素。
class LengthError(ValueError):
    def __init__(self, arg):
        self.args = arg

def pad_zero_to_left(inputNumString, totalLength):
    '''
    takes inputNumString as input,
    pads zero to its left, and make it has the length totalLength
    1. calculates the length of inputNumString
    2. compares the length and totalLength
        2.1 if length > totalLength, raise an error
        2.2 if length == totalLength, return directly
        2.3 if length < totalLength, pads zeros to its left
    '''
    lengthOfInput = len(inputNumString)
    if lengthOfInput > totalLength:
        raise LengthError("The length of input is greater than the total\ length.")
    else:
        return '0' * (totalLength - lengthOfInput) + inputNumString


poolOfChars = string.ascii_letters + string.digits #string.ascii_letters 是所有字母,string.digits是所有数字
random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])
''' lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数'''


def invitation_code_generator(quantity, lengthOfRandom, LengthOfKey):
    '''
    generate `quantity` invitation codes
    '''
    placeHoldChar = "L"
    for index in range(quantity):
        tempString = ""
        try:
            yield random_codes(poolOfChars, lengthOfRandom) + placeHoldChar + \
                  pad_zero_to_left(str(index), LengthOfKey)
        except LengthError:
            print "Index exceeds the length of master key."


for invitationCode in invitation_code_generator(200, 16, 4):
    print invitationCode