#!/usr/bin/env python3

import requests
from termcolor import colored
import pyfiglet

# Function to print text in rainbow colors
def print_rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, char in enumerate(text):
        print(colored(char, colors[i % len(colors)]), end='')
    print()

# Function to get phone number details using numverify API
def get_phone_number_details(api_key, phone_number):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get IP address details using ipinfo.io API
def get_ip_address_details(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch social media profiles (dummy implementation)
def get_social_media_profiles(username):
    # This is a placeholder function. Implement actual logic for fetching social media profiles.
    return {
        "Twitter": f"https://twitter.com/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}",
        "GitHub": f"https://github.com/{username}"
    }

if __name__ == "__main__":
    text = pyfiglet.figlet_format("Advanced OSINT Tool")
    print_rainbow_text(text)

    api_key = "API_KEY"  #if you are a cybersecurity student please  help me to  fill api key because i have login issues

    while True:
        print("\nSelect an OSINT task:")
        print("1. Get phone number details")
        print("2. Get IP address details")
        print("3. Get social media profiles")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            phone_number = input("Enter phone number: ")
            details = get_phone_number_details(api_key, phone_number)
            if details:
                print(details)
            else:
                print("Failed to retrieve phone number details.")
        elif choice == "2":
            ip_address = input("Enter IP address: ")
            details = get_ip_address_details(ip_address)
            if details:
                print(details)
            else:
                print("Failed to retrieve IP address details.")
        elif choice == "3":
            username = input("Enter username: ")
            profiles = get_social_media_profiles(username)
            for platform, url in profiles.items():
                print(f"{platform}: {url}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
