def list_to_dict():
    print("list is converted to dictionary")
    keys=[1,2,3]
    values=['one','two','three']
    dictionary=dict(zip(keys,values))
    print(dictionary)
def dict_to_list():
    print("dictionary is converted to list")
    x={1: 'one', 2: 'two', 3: 'three'}   
    for i in x.items():
        print(i) 
list_to_dict()
dict_to_list()   
    