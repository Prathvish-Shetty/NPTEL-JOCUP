def count_letters(S):
    letter_count = {}
    for char in S:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
input_string = "The Joy of computing"
output_dict = count_letters(input_string)
print(output_dict)



#You are given a string S. Write a function count_letters which will return a dictionary containing letters (including special character) in string S as keys and their count in string S as values.
#def count_letters(l):
#  a=list(dict.fromkeys(l))
#  c={}
#  for i in a:
#   c[i]=l.count(i)
# return c
