string = input("give me a string: ")

length = len(string)

platsbak = length - 1

for plats in range(0, length):
    if string[plats] != string[platsbak - plats]:
        print("{} is not a palindrone".format(string))
        exit(0)
print(string, "is a palindrone")


#online lösning
# wrd=input("Please enter a word")
# wrd=str(wrd)
# rvs=wrd[::-1]
# print(rvs)
# if wrd == rvs:
#     print("This word is a palindrome")
# else:
# print("This word is not a palindrome")

# for i in string:
#     if string[plats] == string[platsbak]:
#         allaRätt += 1
#     plats += 1
#     platsbak = platsbak - 1

# if allaRätt == length:
#     print(string, "is a palindrone")
# else:
#     print(string, "is not a palindrone")




#fungerade inte
# for i in string:
#     length += 1

# length = length / 2
# length = int(length)

# förstaHalvan = string[0:length]
# if length % 2 != 0:
#     length += 1
#     andraHalvan = string[length:]
# else:
#     andraHalvan = string[length:]

# plats = 0
# platsbak = length - 1
# allaRätt = 0

# for i in andraHalvan:
#     if förstaHalvan[plats] == andraHalvan[platsbak]:
#         allaRätt += 1
#     plats += 1
#     platsbak = length - plats
#     platsbak = platsbak - 1
#     print(alla rätt)


# if allaRätt == andraHalvan:
#     print(string, "is a palindrone")
