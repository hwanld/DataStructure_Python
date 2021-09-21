houses = ['Ana', 'Claire', 'Elin', 'Jay']


def santa_delivers_presents_iteratively(houses):
    for house in houses:
        print("Delivering presents to "+house+" 's home")


def santa_delivers_presenets_recursively(houses):
    if (len(houses) == 1):
        print("Delivering presents to "+houses[0]+" 's home")
    else:
        santa_delivers_presenets_recursively(houses[:len(houses)//2])
        santa_delivers_presenets_recursively(houses[len(houses)//2:])


def santa_delivers_presents_another_recursively(houses):
    if (len(houses) >= 1):
        print("Delivering presents to "+houses[0]+" 's home")
        santa_delivers_presents_another_recursively(houses[1:])


santa_delivers_presents_iteratively(houses)
print("--------------------------------------------")
santa_delivers_presenets_recursively(houses)
print("--------------------------------------------")
santa_delivers_presents_another_recursively(houses)
