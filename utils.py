import requests
from consts import BASE_URL


# Get all countries
def get_all_countries():
    return requests.get(f"{BASE_URL}/all")


# Get country by name
def get_country_by_name(country_name):
    return requests.get(f"{BASE_URL}/name/{country_name}")


# Get country by code
def get_country_by_code(country_code):
    return requests.get(f"{BASE_URL}/alpha/{country_code}")


# Get countries by region
def get_countries_by_region(region):
    return requests.get(f"{BASE_URL}/region/{region}")
