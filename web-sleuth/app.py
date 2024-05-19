import requests
from bs4 import BeautifulSoup
import builtwith
import whois
import socket
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()

API_KEY = os.getenv("API_KEY")
console = Console()

def display_welcome_message():
    """
    Displays a welcome message for the application.
    """
    console = Console()

    console.print("\n[bold magenta]----------------------------------------------------------[/bold magenta]")
    console.print("[bold magenta]| Welcome to WebSleuth, your go-to application analyzer! |[/bold magenta]")
    console.print("[bold magenta]----------------------------------------------------------[/bold magenta]\n")


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
    geolocation_data = response.json()
    return geolocation_data

def display_key(key, splitKey):
    return " ".join(key.split(splitKey)).capitalize()

def display_basic_info(title, meta_desc):
    """
    Displays basic information like title and meta description.
    """
    console.print("\n")
    table = Table(show_header=False, title="Basic Information", title_style="bold magenta", title_justify="left")
    table.add_row("Title:", title)
    table.add_row("Meta Description:", meta_desc)
    console.print(table)
    console.print("\n")

def display_tech_stack(tech_stack):
    """
    Displays the technology stack of the website.
    """

    table = Table(show_header=False, title="Technology Stack", title_style="bold magenta", title_justify="left")
    for tech in tech_stack:
        table.add_row(f"{display_key(tech, '-')}:", ",".join(tech_stack[tech]))
    console.print(table)
    console.print("\n")

def display_whois_info(whois_info):
    """
    Displays WHOIS information of the domain.
    """

    table = Table(title="WHOIS Information",  title_style="bold magenta", title_justify="left")
    table.add_column("Attribute", style="cyan", justify="center")
    table.add_column("Value", style="cyan", justify="center")

    for attribute, value in whois_info.items():
        table.add_row(display_key(attribute,"_"), str(value))

    console.print(table)
    console.print("\n")


def display_geolocation(geolocation):
    """
    Displays geolocation information of the IP address.
    """
    table = Table(show_header=False, title="Geolocation Information",  title_style="bold magenta", title_justify="left")
    table.add_row("Location:", f"{geolocation.get('city')}, {geolocation.get('region')}, {geolocation.get('country')}")
    table.add_row("Latitude:", geolocation.get("loc").split(",")[0])
    table.add_row("Longitude:", geolocation.get("loc").split(",")[1])
    table.add_row("Postal Code:", geolocation.get("postal"))
    console.print(table)
    console.print("\n")

def display_exception(e):
    console.print("\n")
    console.print(f"[bold red]Error:[/bold red] {e}")
    console.print("\n")

def main():
    try:
        display_welcome_message()

        url = input("Enter the website URL (e.g., https://www.example.com): ")
        domain = url.split("//")[-1].split("/")[0] #Basicallt, extracting www.example.com from https://www.example.com/xyz

        # Fetch basic information
        title, meta_desc = fetch_basic_info(url)
        display_basic_info(title, meta_desc)

        # Fetch technology stack
        tech_stack = fetch_tech_stack(url)
        display_tech_stack(tech_stack)

        # Fetch WHOIS information
        whois_info = fetch_whois_info(domain)
        display_whois_info(whois_info)

        # Fetch IP address
        ip_address = fetch_ip_address(domain)

        # Fetch geolocation information
        geolocation = fetch_geolocation(ip_address)
        display_geolocation(geolocation)

    except Exception as e:
        display_exception(e)

if __name__ == "__main__":
    main()
