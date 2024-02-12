
# Обратите внимание, что ингредиенты могут повторяться
def my_cook_book():
    with open('recipies.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
    return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dish in dishes:
        for book in cook_book[dish]:
            dishes_dict[book['ingredient_name']] = {'measure': book['measure'], 'quantity':book['quantity'] * person_count}
    return dishes_dict


cook_book = my_cook_book()
print(get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2))
