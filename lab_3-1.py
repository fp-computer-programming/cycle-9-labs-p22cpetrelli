# author CJP 01/11/2022

sixth_letter = []
not_foods = []
short_foods = []

def add_foods(lst):
    for x in lst:
        try:
            sixth_letter.append(x[5])
        except IndexError:
            short_foods.append(x)
        except TypeError:
            not_foods.append(x)

        

add_foods(['potatoes','salsa','cherries','banana','apple'])
add_foods(['naan','celery','buckwheat',7,'clementine'])
add_foods(['cheeseburger',True,'chicken','rice','radish'])

print("sixth_letter: {0}.".format(sixth_letter))
print("short_foods: {0}.".format(short_foods))
print("not_foods: {0}.".format(not_foods))