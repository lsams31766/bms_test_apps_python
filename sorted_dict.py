#sorted_dict.py
from operator import itemgetter, attrgetter
def sort_with_keys(a_dict):
    keys = a_dict.keys()
    sorted_keys = sorted(keys)
    out_list = [(s,a_dict[s]) for s in sorted_keys]
    return out_list

def sort_with_lambda(a_dict):
    out_list =  [(k, v) for k, v in sorted(a_dict.items(), key=lambda x: x[0])]
    return out_list

def sort_by_value(a_dict):
    out_list =  [(k, v) for k, v in sorted(a_dict.items(), key=lambda x: x[1])]
    return out_list

def add_10(a):
    sum = lambda x: x+10
    return sum(a)

def mult(a,b):
    prod = lambda x,y: x*y
    return(prod(a,b))

def get_value(n):
    return itemgetter(n)

def sort_by_func(a_dict):
    #out_list =  [(k, v) for k, v in sorted(a_dict.items(), key=itemgetter(1))]
    out_list =  [(k, v) for k, v in sorted(a_dict.items(), key=get_value(1))]
    return out_list


d = {"head":5,"toe":2,"elbow":3}
print(d)
# sort by looking at keys
print(sort_with_keys(d))
print(sort_with_lambda(d))
print(sort_by_value(d))
print(add_10(5))
print(mult(3,9))
print(sort_by_func(d))
