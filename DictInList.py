travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# add new country to the travel_log
def add_new_country(countries_visited, times_visited, cities_visited):
    new_entry = {}
    new_entry["country"] = countries_visited
    new_entry["visits"] = times_visited
    new_entry["cities"] = list(cities_visited)
    travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)