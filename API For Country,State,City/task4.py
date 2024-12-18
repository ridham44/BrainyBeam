import requests
import csv

def get_cities_of_india():
    # API URL to get cities in India (replace with a working API URL)
    api_url = "https://api.countrystatecity.in/v1/countries/IN/states/MH/cities"

    try:
        # Send GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        cities_data = response.json()

        # List to hold city information
        cities = []
        for city in cities_data:
            cities.append([city['name'], city['state'], city['country'], city['latitude'], city['longitude']])

        # Save to CSV file
        with open('cities_of_india.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['City Name', 'State', 'Country', 'Latitude', 'Longitude'])  # Write headers
            writer.writerows(cities)  # Write city data

        print("Cities data has been saved to 'cities_of_india.csv'.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching city data: {e}")

# Call the function to get cities
get_cities_of_india()
