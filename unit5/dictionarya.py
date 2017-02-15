from pprint import pprint 
d = {
    
}    

def get_add(d):
    key = input("Input key: ")
    value = input("Input value: ")
    d[key] = value
print(get_add(d))