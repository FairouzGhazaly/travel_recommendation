import pandas as pd

users_data = pd.read_csv(r"C:\Users\HP\Documents\archive.csv\users.csv.csv")
flights_data = pd.read_csv(r"C:\Users\HP\Documents\archive.csv\flights.csv.csv")
hotels_data = pd.read_csv(r"C:\Users\HP\Documents\archive.csv\hotels.csv.csv")

final_users = users_data[["code", "name"]]
final_hotels = hotels_data[["userCode","name" , "place" , "price"]]
final_flights = flights_data[["userCode",'from','to','price']]


filtered_hotelscsv = final_hotels.drop_duplicates()
filtered_flightscsv = final_flights.drop_duplicates()



def recommended_cities(user_code, budget, num_cities, user_location):

    # Filter by user's location
    filtered_flights = filtered_flightscsv.loc[filtered_flightscsv['from'] == user_location]

    # Sort flights dataset by price
    sorted_flights = filtered_flights.sort_values('price')

    # Select cities by lowest prices
    selected_cities = []
    for _, flight in sorted_flights.iterrows():
        city = flight['to']
        if city not in selected_cities:
            selected_cities.append(city)
            if len(selected_cities) == num_cities:
                break

    # Retrieve recommended cities within budget
    recommended_cities = []
    remaining_budget = budget
    for city in selected_cities:
        city_price = filtered_flights.loc[(filtered_flights['to'] == city)]['price'].iloc[0]
        if city_price <= remaining_budget:
            recommended_cities.append(city)
            remaining_budget -= city_price

    return recommended_cities


user_code = '0'
budget = 4000
num_cities = 5
user_location = 'Brasilia (DF)' 

rec_cities = recommended_cities(user_code, budget, num_cities, user_location)
print("Recommended cities:", rec_cities)