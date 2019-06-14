def ReverseString(sentence):
        sentence = sentence.split()

        sentence.reverse()

        return " ".join(sentence)

print(ReverseString(input("Enter a sentence: ")))



# #deras, den är bra
# def reverseWord(w):
#   return ' '.join(w.split()[::-1])

# print(reverseWord(input("enter a sentence: ")))





# print(stringlist.reverse())

# for elem in stringlist:
#         print(elem)


# sentence = [1, 2, 3]

# sentence.reverse()

# print(sentence)


# string = input("give me a string: ")

# length = len(string)

# platsbak = length - 1

# for plats in range(0, length):
#     if string[plats] != string[platsbak - plats]:
#         print("{} is not a palindrone".format(string))
#         exit(0)
# print(string, "is a palindrone")