import requests
from datetime import datetime as dt

# Function to fetch and display weather information
def weather(location, API_key):
    try:
        # Construct the API URL using the location and API key
        url = ('https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+API_key)
        # Make a GET request to the API
        response = requests.get(url)
        # Check if the location is valid
        if response.status_code == 404:
            print('Invalid location! Please enter a valid location.')
            return

        # Extract relevant weather data from the API response
        data = response.json()
        tempk = data['main']['temp']
        temp = tempk - 273.15
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        windSpeed = data['wind']['speed']
        sunset2 = dt.fromtimestamp(data['sys']['sunset']).time()
        sunrise2 = dt.fromtimestamp(data['sys']['sunrise']).time()

        # Ask user for temperature unit preference with validation
        while True:
            unit = input('Enter unit (C/F): ').upper()
            if unit == 'C':
                # Display temperature in Celsius
                print('\nWeather: '+ desc)
                print('Temperature: ' + str(round(temp, 2))+' C')
                print("WindSpeed: "+str(windSpeed)+" Km/Hr")
                print("Sunrise :- "+str(sunrise2.strftime("%I:%M %p"))+"\nSunset :- "+str(sunset2.strftime("%I:%M %p")))
                print('Humidity: '+str(humidity)+"%\n\n")
                break
            elif unit == 'F':
                # Convert temperature to Fahrenheit if requested
                temp = (temp * 9/5) + 32
                print('\nWeather: '+ desc)
                print('Temperature: ' + str(round(temp, 2))+' F')
                print("WindSpeed: "+str(windSpeed)+" Km/Hr")
                print("Sunrise :- "+str(sunrise2.strftime("%I:%M %p"))+"\nSunset :- "+str(sunset2.strftime("%I:%M %p")))
                print('Humidity: '+str(humidity)+"%\n\n")
                break
            else:
                print('Invalid unit! Please enter either "C" or "F".')
    except requests.exceptions.RequestException as e:
        print('Error connecting to the internet. Please check your internet connection.')

# Api key
API_key = 'f6229f19b325c9e897b405371ea333ea'

# Main loop to search for weather in multiple locations
while True:
    # Prompt user to enter a location
    location = input('Location: ')
    # Check if user has entered a location
    if not location:
        print("Please enter a location.")
        continue

    # Call the weather function to fetch and display weather information
    weather(location, API_key)

    # Prompt user if they want to search for another location
    lastInput = input('Do you want to search another location? (Y/N): ')
    # If user doesn't want to search another location, exit the loop
    if lastInput.upper() != 'Y':
        print('Thank you for using our service')
        break

# Wait for user to press Enter before exiting
input('\nPress Enter to exit')
