import requests

# test first api to get current iss location
api1_data = requests.get("http://api.open-notify.org/iss-now.json")
print(api1_data)
print(api1_data.json())

parsed_api1_data = api1_data.json()
print(type(parsed_api1_data))
print(parsed_api1_data["iss_position"])
print(parsed_api1_data["message"])

# test first api to find number of person in space
api2_data = requests.get("http://api.open-notify.org/astros.json")
print(api2_data)
print(api2_data.json())
parsed_api2_data = api2_data.json()
print(type(parsed_api2_data))
print(parsed_api2_data["number"])
print(parsed_api2_data["message"])
print(parsed_api2_data["people"])
# print multiple values
for p in parsed_api2_data["people"]:
    print(p["name"])
