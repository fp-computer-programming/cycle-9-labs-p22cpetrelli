# author CJP 01/06/2022
def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = 2 * v
    return lst

print(double_stuff([1,2,3,4]) == [2,4,6,8])
print(double_stuff([1.2,2,3,4.1]) == [2.4,4,6,8.2])
print(double_stuff([1,"a",3,"b"]) == [2,"aa",6,"bb"])