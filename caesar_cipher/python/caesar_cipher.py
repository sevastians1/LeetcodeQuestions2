from operator import is_


def caesar_cipher(string, shift_amount):
    answer_string=[]
    for count, x in enumerate(string):
        if x.isalpha():
            is_uppercase=False
            if x!=x.lower():
                is_uppercase=True
            # print(x, "startingvalue")
            x=ord(x.lower())
            # print(x)
            x+=shift_amount
            # print(x)
            if x<97:
                x=123+(x-97)
            elif x>122:
                x=96+(x-122)
            x=chr(x)
            if is_uppercase==True:
                x=x.upper()
            # print(x, "endingvalue")
        answer_string.append(x)
    return "".join(answer_string)

# if ord(x)>96 and ord(x)<123:
# print(chr(122))

print(caesar_cipher("ABC DEFGHIJKLMNOPQURSTUVWXYZ", 5)) #"Wjt! Rcvo v nomdib!"
