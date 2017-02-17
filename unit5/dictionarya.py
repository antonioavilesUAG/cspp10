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
def get_update(d):
    update_key1 = input("What key do you want to update: ")
    update_value2 = input("What value do you want to update: ")
    d[update_key1] = update_value2
get_update(d)
pprint(d)
def exit(d):
    print(d)