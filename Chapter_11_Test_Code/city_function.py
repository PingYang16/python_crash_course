def get_city_country(city, country, population=''):
    """Generate a formatted city, country"""
    if population:
        formatted_city = f"{city}, {country} - population {population}"
    else:
        formatted_city = f"{city}, {country}"
    return formatted_city.title()

city = "corvallis"
country = "united states"
population = 500000
a = get_city_country(city, country, population)
print(a)