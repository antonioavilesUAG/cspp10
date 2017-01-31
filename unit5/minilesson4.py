original = [3]
to_replace = 3
replace_with = 6 
def replace_all(original, to_replace, replace_with):
    for index in range(len(original)):
       if original[index] == to_replace:
           original[index] = replace_with
replace_all(original, to_replace, replace_with)        
print(original)