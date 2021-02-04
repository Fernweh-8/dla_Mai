def best_wishes(name):
    with open(r'C:/Users/annad/wishes.txt', 'a+') as wish_list:
        wish = input(f'{name}, czego życzysz Mai?\n')
        wish_list.writelines(wish)
        wish_list.write("\n")
    with open(r'C:/Users/annad/wishes.txt', 'r') as wishes:
        global your_wishes
        your_wishes = wishes.read()
    return ""


name = input('Podaj swoje imię: \n')

wishes_num = int(input('Ile masz życzeń dla Mai? Wpisz cyfrę: \n'))

for num in range(wishes_num):
    print(best_wishes(name))
print(f'To lista Twoich życzeń: \n {your_wishes}')
print(f'{name}, dziękuję za te wszystkie życzenia!\n')
print("Pora nominiwać 3 osoby do akcji.")
