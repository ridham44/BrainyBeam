#Ridham Patel
#17/12/2024
import requests
import csv

def get_cities_of_india():
    api_url = "https://api.countrystatecity.in/v1/countries/IN/states/MH/cities"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        cities_data = response.json()

        cities = []
        for city in cities_data:
            cities.append([city['name'], city['state'], city['country'], city['latitude'], city['longitude']])

        with open('cities_of_india.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['City Name', 'State', 'Country', 'Latitude', 'Longitude'])  # Write headers
            writer.writerows(cities)  # Write city data

        print("Cities data has been saved to 'cities_of_india.csv'.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching city data: {e}")

get_cities_of_india()
