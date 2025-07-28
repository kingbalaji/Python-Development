cars = [
    {'brand': 'Toyota', 'model': 'Corolla', 'type': 'Sedan', 'color': 'Red', 'variant': 'Petrol'},
    {'brand': 'Ford', 'model': 'Mustang', 'type': 'Coupe', 'color': 'Blue', 'variant': 'EV'},
    {'brand': 'Honda', 'model': 'Civic', 'type': 'Sedan', 'color': 'Black', 'variant': 'Diesel'},
    {'brand': 'Toyota', 'model': 'Corolla', 'type': 'Sedan', 'color': 'Red', 'variant': 'Petrol'},
    {'brand': 'Ford', 'model': 'Mustang', 'type': 'Coupe', 'color': 'Blue', 'variant': 'Petrol'},
    {'brand': 'Honda', 'model': 'Civic', 'type': 'Sedan', 'color': 'Black', 'variant': 'Petrol'},
    {'brand': 'Hyundai', 'model': 'Elantra', 'type': 'Sedan', 'color': 'White', 'variant': 'Petrol'},
    {'brand': 'Chevrolet', 'model': 'Camaro', 'type': 'Coupe', 'color': 'Yellow', 'variant': 'Petrol'},
    {'brand': 'BMW', 'model': 'X5', 'type': 'SUV', 'color': 'Black', 'variant': 'Petrol'},
    {'brand': 'Mercedes-Benz', 'model': 'C-Class', 'type': 'Sedan', 'color': 'Silver', 'variant': 'Petrol'},
    {'brand': 'Kia', 'model': 'Sorento', 'type': 'SUV', 'color': 'Blue', 'variant': 'Petrol'},
    {'brand': 'Audi', 'model': 'A4', 'type': 'Sedan', 'color': 'Gray', 'variant': 'Petrol'},
    {'brand': 'Volkswagen', 'model': 'Golf', 'type': 'Hatchback', 'color': 'Green', 'variant': 'Petrol'},
    {'brand': 'Mazda', 'model': 'CX-5', 'type': 'SUV', 'color': 'Red', 'variant': 'Petrol'},
    {'brand': 'Nissan', 'model': 'Altima', 'type': 'Sedan', 'color': 'White', 'variant': 'Petrol'},
    {'brand': 'Subaru', 'model': 'Outback', 'type': 'Wagon', 'color': 'Silver', 'variant': 'Diesel'},
    {'brand': 'Tesla', 'model': 'Model 3', 'type': 'Sedan', 'color': 'Blue', 'variant': 'Electric'},
    {'brand': 'Jeep', 'model': 'Wrangler', 'type': 'SUV', 'color': 'Green', 'variant': 'Diesel'},
    {'brand': 'Dodge', 'model': 'Charger', 'type': 'Sedan', 'color': 'Red', 'variant': 'Petrol'},
    {'brand': 'Honda', 'model': 'CR-V', 'type': 'SUV', 'color': 'Silver', 'variant': 'Petrol'},
    {'brand': 'Toyota', 'model': 'Camry', 'type': 'Sedan', 'color': 'Black', 'variant': 'Petrol'},
    {'brand': 'Ford', 'model': 'Explorer', 'type': 'SUV', 'color': 'White', 'variant': 'Diesel'},
    {'brand': 'Chevrolet', 'model': 'Equinox', 'type': 'SUV', 'color': 'Blue', 'variant': 'Diesel'}
]
def search_cars(cars, key, value):
    return [car for car in cars if car[key].lower() == value.lower()]

def menu():
    print("Search for cars by:")
    print("1. Brand")
    print("2. Model")
    print("3. Type")
    print("4. Color")
    print("5. Variant")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

key_map = {
    '1': 'brand',
    '2': 'model',
    '3': 'type',
    '4': 'color',
    '5': 'variant'
}

while True:
    choice = menu()
    if choice == '0':
        print("Exiting program.")
        break
    elif choice in key_map:
        search_term = input(f"Enter {key_map[choice].capitalize()}: ")
        results = search_cars(cars, key_map[choice], search_term)
        if results:
            print("\nSearch Results:")
            for car in results:
                print(car)
        else:
            print("No results found.")
    else:
        print("Invalid choice. Please select a valid option.")
