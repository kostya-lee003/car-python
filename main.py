cars = []
max_speed = []
car_description = ['Car: ', 'Speed: ']
c = 0
a = 0
i = 1
while i > 0:
    car = input(car_description[0])
    ms = input(car_description[1])
    cars.append(car)
    max_speed.append(ms)
    # car_description_input = [car[c], ms[c]]
    # b = car_description_input[c]

    cont = input('Do you want to continue: ')

    if cont == 'no':
        while c < len(car_description) * len(cars):
            print(car_description[0] + cars[c])
            print(car_description[1] + max_speed[c])
            c = c + 1
        break

    elif cont == 'yes':
        a = a + 1
        continue