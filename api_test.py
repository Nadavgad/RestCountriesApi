import pytest
from utils import *


# Test to get all countries and check that the response is successful
# and that the list of countries is not empty.
def test_get_all_countries():
    res = get_all_countries()
    assert (res.status_code == 200)
    assert (len(res.json()) > 0)


# Parametrized test to get a country by its name and check that the response
# is successful, the result contains exactly one country, and the country's name matches the input.
@pytest.mark.parametrize("country_name", [
    "Germany",
    "Israel",
    "France"
])
def test_get_country_by_name(country_name):
    res = get_country_by_name(country_name)
    assert (res.status_code == 200)
    data = res.json()
    assert (len(data) == 1)
    assert (data[0]["name"]["common"] == country_name)


# Parametrized test to get a country by a non-existent or bad name
# and check that the response is a 404 (not found).
@pytest.mark.parametrize("country_name", [
    "NonExist",
    "BadCountry",
    "SOMEthing"
])
def test_get_country_bad_name(country_name):
    res = get_country_by_name(country_name)
    assert (res.status_code == 404)


# Parametrized test to get a country by its code and check that the response
# is successful, and the country's code matches the input.
@pytest.mark.parametrize("country_code", [
    "DEU",
    "USA",
])
def test_get_country_by_code(country_code):
    res = get_country_by_code(country_code)
    assert (res.status_code == 200)
    data = res.json()
    assert (data[0]["cca3"] == country_code)


# Parametrized test to get a country by a non-existent or bad code
# and check that the response is a 404 (not found).
@pytest.mark.parametrize("country_code", [
    "XZA",
    "STS",
])
def test_get_country_bad_code(country_code):
    res = get_country_by_code(country_code)
    assert (res.status_code == 404)


# Parametrized test to get countries by a region and check that the response
# is successful, the list of countries is not empty, and all countries in the list
# belong to the specified region.
@pytest.mark.parametrize("region", [
    "Europe",
    "Asia",
    "Africa",
])
def test_get_countries_by_region(region):
    res = get_countries_by_region(region)
    assert (res.status_code == 200)
    data = res.json()
    assert (len(data) > 0)
    assert (all(country["region"] == region for country in data))


if __name__ == "__main__":
    pytest.main()
