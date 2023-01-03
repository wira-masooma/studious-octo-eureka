# d1 = int(input())
# d2 = int(input())
# d3 = int(input())
# d4 = int(input())
# d5 = int(input())

# def num_petals(d1, d2, d3, d4, d5):
#     sum = 0
#     if d1 % 2 != 0:
#         sum = sum + (d1 - 1)
#     if d2 % 2 != 0:
#         sum = sum + (d2 - 1)
#     if d3 % 2 != 0:
#         sum = sum + (d3 - 1)
#     if d4 % 2 != 0:
#         sum = sum + (d4 - 1)
#     if d5 % 2 != 0:
#         sum = sum + (d5 - 1)
#     return sum

# print(num_petals(d1,d2,d3,d4,d5))


# distance = float(input())
# amount = float(input())
# cost = float(input())
# target = float(input())

# def are_you_green(distance, amount, cost, target):
#     fuel_consumed = amount/cost
#     fuel_economy = (100 * fuel_consumed) / distance
#     if fuel_economy == target :
#         print('Your vehicle just met the target.')
#     elif fuel_economy < target:
#         t = target - fuel_economy
#         if round(t, 2) != 0.0 and round(t, 2) != 0.00:
#             print('Your vehicle exceeded the target by',round(t, 2),'L/100 km.')
#     elif fuel_economy > target:
#         t2 = fuel_economy - target
#         if round(t2, 2) != 0.0 and round(t2, 2) != 0.00:
#             print('Your vehicle missed the target by',round(t2, 2),'L/100 km.')
#     elif round(t, 2) == 0.0 or round(t2, 2) == 0.0 or round(t, 2) == 0.00 or round(t2, 2) == 0.00:
#         print('Your vehicle just met the target.')

#are_you_green(distance, amount, cost, target)


# def zhits(word):
#     length = len(word)
#     word1 = ""
#     word2 = unique_letters(word)
#     # if length >= 4:
#     #for i in range(factorial(length)):
#     letter = ""
#     for letter1 in word2:
#             for letter2 in word2:
#                 if letter2 != letter1:
#                     for letter3 in word2:
#                         if letter3 != letter2 and letter3 != letter1:
#                             for letter4 in word2:
#                                 if letter4 != letter2 and letter4 != letter1 and letter4 != letter3:
#                                     letter = letter4 + letter3 + letter2 + letter1
#                                     #if letter not in word:
#                                     word1 += letter + ", "
#     return word1

# def unique_letters(word):
#     unique_letters = ""
#     for letter1 in word:
#         if letter1 not in unique_letters:
#             unique_letters += letter1
#     return unique_letters

# word = input().split()
# print(zhits(word))

def left_strip(s):
    char = ""
    trail = ""
    for i in s:
        if not(i.isalpha()) and not(i.isnumeric()) or i=="n" or i=="t":
            char += i
        else:
            break
    word = s.replace("\\", " ")
    for i in char[::-1]:
        # if i == "n" or i == "t":
        #     trail += i
        if i == "n" or i == "t" or not(i.isalpha()) or not(i.isnumeric()):
            if i != " ":
                trail += i
        elif i == " ":
        # elif not(i.isalpha()) and not(i.isnumeric()):
                break
    return trail[::-1] + s[len(char):len(s)]

def right_strip(s):
    char = ""
    trail = ""
    for i in s[::-1]:
        if not(i.isalpha()) and not(i.isnumeric()) or i=="n" or i=="t":
            char += i
        else:
            break
    word = s.replace("\\"," ")
    for i in char[::-1]:
        if i == "n" or i == "t" or not(i.isalpha()) or not(i.isnumeric()):
            if i != " ":
                trail += i
        elif i==" ":
            break
        #if i == "n" or i == "t":
        #    trail += i
        #elif not(i.isalpha()) and not(i.isnumeric()):
        #    break
    return s[:len(s)-len(char)] + trail
    # if s[len(s)-len(char)] == "n" or s[len(s)-len(char)] == "t":
    #     return s[:len(s)-len(char) + 1]
    # else:
    #     return s[:len(s)-len(char)]
    
def my_strip(s):
    return right_strip(left_strip(s))

s = int(input())
print(my_strip(s))
    