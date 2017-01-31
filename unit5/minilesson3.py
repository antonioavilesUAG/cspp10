def extend(original,extension):
    for element in extension:
        original.append(element)
    print(original)
    
original = []
extension = [1,2,3]

extend(original, extension)