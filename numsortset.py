def uniqueE(L):
    unique_elements = []
    
    for item in L:
        if L.count(item) == 1:
            unique_elements.append(item)
    
    return sorted(unique_elements)

# Example input
input_list = [1, 2, 3, 3, 4, 4, 2, 5, 6, 7]
result = uniqueE(input_list)
print(result)  # Output: [1, 5, 6, 7]

#def uniqueE(L):
#  b=[]
#  a=sorted(list(dict.fromkeys(L)))
#  for i in a:
#   if L.count(i)<2:
#     b.append(i)
# return b
