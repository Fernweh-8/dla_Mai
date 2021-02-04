def add_best_wishes(filename, name, wishes_num):
    with open(filename, 'a+') as wish_list:
        for num in range(wishes_num):
            wish = input(f'{name}, czego życzysz Mai?\n')
            wish_list.writelines(wish)
            wish_list.write("\n")

def get_best_wishes(filename):
    with open(filename) as wishes:
        return wishes.read()

filename = r'C:/Users/annad/wishes.txt'
name = input('Podaj swoje imię: \n')
wishes_num = int(input('Ile masz życzeń dla Mai? Wpisz cyfrę: \n'))

add_best_wishes(filename, name, wishes_num)

print(f'To lista Twoich życzeń: \n {get_best_wishes(filename)}')
print(f'{name}, dziękuję za te wszystkie życzenia!\n')
print('Pora nominiwać 3 osoby do akcji.')
