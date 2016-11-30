def hotel_cost(days):
    return 140 * days

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475

def rental_car_cost(days):
    if days < 3:
        return days * 40
    elif days < 7:
        return (days * 40) - 20
    else:
        return (days * 40) - 50

def trip_cost(city, days, spending_money):
    print plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money

trip_cost('Tampa', 7, 220)
trip_cost('Los Angeles', 5, 600)
