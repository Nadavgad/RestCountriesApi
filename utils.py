import requests
from consts import BASE_URL

def get_all_countries():
    return requests.get(f"{BASE_URL}/all")

def get_country_by_name(country_name):
    return requests.get(f"{BASE_URL}/name/{country_name}")

def get_country_by_code(country_code):
    return requests.get(f"{BASE_URL}/alpha/{country_code}")

def get_countries_by_region(region):
    return requests.get(f"{BASE_URL}/region/{region}")
