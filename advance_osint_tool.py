#!/usr/bin/env python3

import requests
from termcolor import colored
import pyfiglet
from bs4 import BeautifulSoup

# Function to print text in rainbow colors
def print_rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, char in enumerate(text):
        print(colored(char, colors[i % len(colors)]), end='')
    print()

# Function to get IP address details using ipinfo.io
def get_ip_address_details(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch social media profiles
def get_social_media_profiles(username):
    profiles = {
        "Twitter": f"https://twitter.com/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}",
        "GitHub": f"https://github.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "WhatsApp": f"https://wa.me/{username}",
        "Truecaller": f"https://www.truecaller.com/search/global/{username}"
    }
    return profiles

# Function to scrape data from a public website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else "No title found"

if __name__ == "__main__":
    text = pyfiglet.figlet_format("Advanced OSINT Tool")
    print_rainbow_text(text)

    while True:
        print("\nSelect an OSINT task:")
        print("1. Get IP address details")
        print("2. Get social media profiles")
        print("3. Scrape website data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            ip_address = input("Enter IP address: ")
            details = get_ip_address_details(ip_address)
            if details:
                print(details)
            else:
                print("Failed to retrieve IP address details.")
        elif choice == "2":
            username = input("Enter username: ")
            profiles = get_social_media_profiles(username)
            for platform, url in profiles.items():
                print(f"{platform}: {url}")
        elif choice == "3":
            url = input("Enter website URL: ")
            title = scrape_website(url)
            print(f"Website Title: {title}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
