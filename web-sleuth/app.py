import requests
from bs4 import BeautifulSoup
import builtwith
import whois
import socket
import json
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY=os.getenv("API_KEY")

def fetch_basic_info(url):
    """
    Fetches the basic information of a website like title and meta description.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('title').string if soup.find('title') else 'N/A'
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_desc['content'] if meta_desc else 'N/A'
    
    return title, meta_desc

def fetch_tech_stack(url):
    """
    Fetches the technology stack of a website using builtwith.
    """
    tech_stack = builtwith.parse(url)
    return tech_stack

def fetch_whois_info(domain):
    """
    Fetches the WHOIS information of a domain.
    """
    whois_info = whois.whois(domain)
    return whois_info

def fetch_ip_address(domain):
    """
    Fetches the IP address of a domain.
    """
    ip_address = socket.gethostbyname(domain)
    return ip_address

def fetch_geolocation(ip_address):
    """
    Fetches the geolocation information of an IP address using ipinfo API.
    """
    response = requests.get(f"https://ipinfo.io/{ip_address}/json?token={API_KEY}")
    # NOTE: 50k lookups per month is free, but beyond that you would be billed. Refer https://ipinfo.io/account/billing/subscriptions for more information
    geolocation_data = response.json()
    return geolocation_data

def main():
    try:
        url = input("Enter the website URL (e.g., https://www.example.com): ")
        domain = url.split("//")[-1].split("/")[0]
        
        # Fetch basic information
        title, meta_desc = fetch_basic_info(url)
        print(f"Title: {title}")
        print(f"Meta Description: {meta_desc}")
        
        # Fetch technology stack
        tech_stack = fetch_tech_stack(url)
        print("Tech Stack:")
        for tech in tech_stack:
            print(f"  - {tech}: {tech_stack[tech]}")
        
        # Fetch WHOIS information
        whois_info = fetch_whois_info(domain)
        print("WHOIS Information:")
        print(whois_info)
        
        # Fetch IP address
        ip_address = fetch_ip_address(domain)
        print(f"IP Address: {ip_address}")
        
        # Fetch geolocation information
        geolocation = fetch_geolocation(ip_address)
        print("Geolocation Information:")
        print(json.dumps(geolocation, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
