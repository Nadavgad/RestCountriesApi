import pytest
from utils import *

def test_get_all_countries():
    res = get_all_countries()
    assert(res.status_code == 200)
    assert(len(res.json()) > 0)

@pytest.mark.parametrize("country_name", [
    "Germany",
    "Israel",
    "France"
])
def test_get_country_by_name(country_name):
    res = get_country_by_name(country_name)
    assert(res.status_code == 200)
    data = res.json()
    assert(len(data) == 1)
    assert(data[0]["name"]["common"] == country_name)

@pytest.mark.parametrize("country_name", [
    "NonExist",
    "BadCountry",
    "SOMEthing"
])
def test_get_country_bad_name(country_name):
    res = get_country_by_name(country_name)
    assert(res.status_code == 404)

@pytest.mark.parametrize("country_code", [
    "DEU",
    "USA",
])
def test_get_country_by_code(country_code):
    res = get_country_by_code(country_code)
    assert(res.status_code == 200)
    data = res.json()
    assert(data[0]["cca3"] == country_code)

@pytest.mark.parametrize("country_code", [
    "XZA",
    "STS",
])
def test_get_country_bad_code(country_code):
    res = get_country_by_code(country_code)
    assert(res.status_code == 404)

@pytest.mark.parametrize("region", [
    "Europe",
    "Asia",
    "Africa",
])
def test_get_countries_by_region(region):
    res = get_countries_by_region(region)
    assert(res.status_code == 200)
    data = res.json()
    assert(len(data) > 0)
    assert(all(country["region"] == region for country in data))

if __name__ == "__main__":
    pytest.main()

