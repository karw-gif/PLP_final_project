import requests

# Function to get weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete URL to fetch data
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Send a GET request to the API
        response = requests.get(complete_url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the response
        data = response.json()

        # Check if the city is valid (response code 404 means city not found)
        if data["cod"] != 200:
            print("Error: City not found or invalid API key.")
            return
        
        # Extract main weather data
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        clouds = data["clouds"]
        
        # Extract detailed weather data
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        description = weather["description"]
        wind_speed = wind["speed"]
        wind_direction = wind["deg"]
        cloudiness = clouds["all"]
        
        # Print detailed weather information
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Direction: {wind_direction}°")
        print(f"Cloudiness: {cloudiness}%")
        
        # Additional optional info
        visibility = data.get("visibility", "N/A")  # Some cities may not have this data
        print(f"Visibility: {visibility} meters")
        
        # Geographical information (latitude, longitude)
        coord = data["coord"]
        print(f"Coordinates: Latitude {coord['lat']}, Longitude {coord['lon']}")
    
    except requests.exceptions.RequestException as e:
        # Handle any requests exceptions (network issues, API errors)
        print(f"Error fetching data: {e}")

# Function to get the city name from the user with validation
def get_city_name():
    while True:
        city_name = input("Enter city name: ").strip()
        if not city_name:
            print("City name cannot be empty. Please try again.")
        else:
            return city_name

# Main function to execute the weather program
def main():
    # Your OpenWeatherMap API key (replace with your actual key)
    api_key = "your_api_key_here"
    
    # Get valid city name from user
    city_name = get_city_name()
    
    # Call the function to get weather data for the city
    get_weather(city_name, api_key)

# Start the program
if _name_ == "_main_":
    main()