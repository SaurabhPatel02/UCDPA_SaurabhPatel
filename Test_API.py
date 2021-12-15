import requests

# test first api to get current iss location
api11_data = requests.get("http://api.open-notify.org/iss-now.json")
print(api11_data)
print(api11_data.json())

parsed_api11_data = api11_data.json()
print(type(parsed_api11_data))
print(parsed_api11_data["iss_position"])
print(parsed_api11_data["message"])

# test first api to find number of person in space
api12_data = requests.get("http://api.open-notify.org/astros.json")
print(api12_data)
print(api12_data.json())
parsed_api12_data = api12_data.json()
print(type(parsed_api12_data))
print(parsed_api12_data["number"])
print(parsed_api12_data["message"])
print(parsed_api12_data["people"])
# print multiple values
for p in parsed_api12_data["people"]:
    print(p["name"])
for p in parsed_api12_data["people"]:
    print(p["craft"])

# api key CIBFBXPX8IO5DC5M



# implement type 2 API - stock - intraday trading with key
api2_data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=CIBFBXPX8IO5DC5M")
print(api2_data)
print(api2_data.json())
parsed_api2_data = api2_data.json()
print(type(parsed_api2_data))
print(parsed_api2_data["Meta Data"])
print(parsed_api2_data["Time Series (5min)"])

# implement type 2 API - company overview with key
api22_data = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=CIBFBXPX8IO5DC5M")
print(api22_data)
print(api22_data.json())
parsed_api22_data = api22_data.json()
print(type(parsed_api22_data))
print(parsed_api22_data["Symbol"])
print(parsed_api22_data["AssetType"])
print(parsed_api22_data["ProfitMargin"])