from pprint import pprint 
d = {
    
}    

def get_add(d):
    key = input("Input key: ")
    value = input("Input value: ")
    d[key] = value
get_add(d)
pprint(d)

def get_remove_key(d):
    remove = input("What do you want to delete: ")
    del d[remove]
get_remove_key(d)
pprint(d)
