str1 = "ghhkkhtfdaw4vbhjjjjhhgb5ffcscchjjkkjuhgggffvnnbbnmbczzwerfghhjj"


def is_alpha(str2):  # create the method
    result = ""  # create the string
    for i in str2:  # iterate through the string
        if i.isalpha():  # check if alpha
            result += i  # add to the string
    return result  # return the string


alphas = is_alpha(str1)  # add the method to the string
sorted_string = "".join(sorted(alphas))  # sort the string
print(sorted_string)


def is_digit(str2):
    result = ""
    for i in str2:
        if i.isdigit():
            result += i
    return result


print(is_alpha(str1))  # print the result
print(is_digit(str1))  # print the result
