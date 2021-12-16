import requests
#  https://www.alphavantage.co/documentation/
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

# implement type 2 API - inflation with key
api23_data = requests.get("https://www.alphavantage.co/query?function=INFLATION&apikey=CIBFBXPX8IO5DC5M")
print(api23_data)
print(api23_data.json())
parsed_api23_data = api23_data.json()
print(type(parsed_api23_data))
print(parsed_api23_data["name"])
print(parsed_api23_data["data"])
# print all dates for which inflation rate is available
for p in parsed_api23_data["data"]:
    print(p["date"])

# implement type 2 API - inflation expectation with key
api24_data = requests.get("https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey=CIBFBXPX8IO5DC5M")
print(api24_data)
print(api24_data.json())
parsed_api24_data = api24_data.json()
print(type(parsed_api24_data))
print(parsed_api24_data["name"])
print(parsed_api24_data["data"])
# print all dates for which inflation rate is available
for p in parsed_api24_data["data"]:
    print(p["date"])