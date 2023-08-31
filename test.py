def create_file():
    import pickle
    L = []
    while True:
        VNO = input('Enter VNo.: ')
        VDesc = input('Enter Description: ')
        price = int(input('Enter price:'))
        Lst = [VNO, VDesc, price]
        Lst.append(L)
        print('Want to add another record(yes/no): ', end='')
        choice = input()
        if choice.lower() == 'no':
            break
    with open('VINTAGE.dat', 'wb') as file:
        pickle.dump(L, file)
    print('File created....')


def search_file():
    import pickle
    with open('VINTAGE.dat', 'rb') as file:
        lst = pickle.load(file)
    for i in lst:
        if i[-1] > 200000 and i[-1] < 250000:
            print('Desired Result...')
            print(i)
            break
    else:
        print('Car not found')


create_file()
search_file()
