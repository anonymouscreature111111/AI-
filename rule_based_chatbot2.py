import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hot spots!"
]

weather_data = {
    "bali": "Sunny, 30°C",
    "maldives": "Partly Cloudy, 28°C",
    "phuket": "Sunny, 31°C",
    "tokyo": "Rainy, 22°C",
    "paris": "Cloudy, 18°C",
    "newyork": "Sunny, 25°C",
    "swissalps": "Snowy, -2°C",
    "rockymountains": "Cool, 10°C",
    "himalayas": "Cold, 5°C"
}

city_times = {
    "sydney": "10:00 AM",
    "tokyo": "8:00 AM",
    "paris": "1:00 AM",
    "newyork": "7:00 PM",
    "bali": "7:00 AM"
}

travel_news = [
    "Japan has announced new tourism campaigns for international visitors.",
    "Several airlines are adding new routes to Southeast Asia.",
    "Popular European destinations expect record tourist numbers this year.",
    "Many airports are introducing faster biometric check-in systems.",
    "Beach destinations remain among the most booked holiday locations worldwide."
]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")

        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Enjoy {suggestion}!")

        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another destination.")
            recommend()

        else:
            print(Fore.RED + "TravelBot: I'll suggest another place.")
            recommend()

    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where are you going?")
    location = normalize_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"\nTravelBot: Packing tips for {days} days in {location.title()}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers and adapters")
    print(Fore.GREEN + "- Pack necessary toiletries")
    print(Fore.GREEN + "- Carry important travel documents")
    print(Fore.GREEN + "- Check weather forecast before leaving")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def weather_conditions():
    print(Fore.CYAN + "TravelBot: Which location?")
    location = normalize_input(input(Fore.YELLOW + "You: "))

    if location in weather_data:
        print(
            Fore.GREEN +
            f"TravelBot: Current weather in {location.title()} is {weather_data[location]}"
        )
    else:
        print(
            Fore.RED +
            "TravelBot: Sorry, I don't have weather information for that location."
        )

def local_time():
    print(Fore.CYAN + "TravelBot: Which city?")
    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in city_times:
        print(
            Fore.GREEN +
            f"TravelBot: Local time in {city.title()} is {city_times[city]}"
        )
    else:
        print(
            Fore.RED +
            "TravelBot: Sorry, I don't have time information for that city."
        )

def show_news():
    print(Fore.CYAN + "TravelBot: Latest travel news:")
    print(Fore.GREEN + random.choice(travel_news))

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "Offer packing tips (say 'packing')")
    print(Fore.GREEN + "Tell a joke (say 'joke')")
    print(Fore.GREEN + "Show weather information (say 'weather')")
    print(Fore.GREEN + "Show local time in cities (say 'time')")
    print(Fore.GREEN + "Provide travel news updates (say 'news')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "Your name? ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:

        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()

        elif "pack" in user_input or "packing" in user_input:
            packing_tips()

        elif "joke" in user_input or "funny" in user_input:
            tell_joke()

        elif "weather" in user_input:
            weather_conditions()

        elif "time" in user_input or "clock" in user_input:
            local_time()

        elif "news" in user_input or "update" in user_input:
            show_news()

        elif "help" in user_input:
            show_help()

        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break

        else:
            print(Fore.RED + "TravelBot: Could you rephrase that?")

if __name__ == "__main__":
    chat()