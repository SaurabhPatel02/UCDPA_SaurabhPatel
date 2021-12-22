# -------------- Analyse data using API as source -----------------------
# Dataset URL :
# http://api.open-notify.org/iss-now.json
# http://api.open-notify.org/astros.json
# https://www.alphavantage.co/documentation/

# import library
import requests

# test api to get current iss location
api_issloc_df = requests.get("http://api.open-notify.org/iss-now.json")
print(api_issloc_df)                            # print response
print(api_issloc_df.json())                     # print json output
parsed_api_issloc_df = api_issloc_df.json()     # parsed json output
print(type(parsed_api_issloc_df))               # print type of api
print(parsed_api_issloc_df["iss_position"])     # print respective key values
print(parsed_api_issloc_df["message"])          # print respective key values

# test api to find number of person in space
api_pis_df = requests.get("http://api.open-notify.org/astros.json")
print(api_pis_df)                               # print response
print(api_pis_df.json())                        # print json output
parsed_api_pis_df = api_pis_df.json()           # parsed json output
print(type(parsed_api_pis_df))                  # print type of api
print(parsed_api_pis_df["number"])              # print respective key values
print(parsed_api_pis_df["message"])             # print respective key values
print(parsed_api_pis_df["people"])              # print respective key values
# print multiple values
for p in parsed_api_pis_df["people"]:
    print(p["name"])
for p in parsed_api_pis_df["people"]:
    print(p["craft"])

# implement API from alphavantage
# api key CIBFBXPX8IO5DC5M

# implement type 2 API - stock - intraday trading with key
api_intra_trade_df = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=CIBFBXPX8IO5DC5M")
print(api_intra_trade_df)                               # print response
print(api_intra_trade_df.json())                        # print json output
parsed_api_intra_trade_df = api_intra_trade_df.json()   # parsed json output
print(type(parsed_api_intra_trade_df))                  # print type of api
print(parsed_api_intra_trade_df["Meta Data"])           # print respective key values
print(parsed_api_intra_trade_df["Time Series (5min)"])  # print respective key values

# implement type 2 API - company overview with key
api_comp_ov_df = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=CIBFBXPX8IO5DC5M")
print(api_comp_ov_df)                                   # print response
print(api_comp_ov_df.json())                            # print json output
parsed_api_comp_ov_df = api_comp_ov_df.json()           # parsed json output
print(type(parsed_api_comp_ov_df))                      # print type of api
print(parsed_api_comp_ov_df["Symbol"])                  # print respective key values
print(parsed_api_comp_ov_df["AssetType"])               # print respective key values
print(parsed_api_comp_ov_df["ProfitMargin"])            # print respective key values

# implement type 2 API - inflation with key
api_inflation_df = requests.get("https://www.alphavantage.co/query?function=INFLATION&apikey=CIBFBXPX8IO5DC5M")
print(api_inflation_df)                                 # print response
print(api_inflation_df.json())                          # print json output
parsed_api_inflation_df = api_inflation_df.json()       # parsed json output
print(type(parsed_api_inflation_df))                    # print type of api
print(parsed_api_inflation_df["name"])                  # print respective key values
print(parsed_api_inflation_df["data"])                  # print respective key values
# print all dates for which inflation rate is available
for p in parsed_api_inflation_df["data"]:
    print(p["date"])

# implement type 2 API - inflation expectation with key
api_inf_exp_df = requests.get("https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey=CIBFBXPX8IO5DC5M")
print(api_inf_exp_df)                           # print response
print(api_inf_exp_df.json())                    # print json output
parsed_api_inf_exp_df = api_inf_exp_df.json()   # parsed json output
print(type(parsed_api_inf_exp_df))              # print type of api
print(parsed_api_inf_exp_df["name"])            # print respective key values
print(parsed_api_inf_exp_df["data"])            # print respective key values
# print all dates for which inflation rate is available
for p in parsed_api_inf_exp_df["data"]:
    print(p["date"])

# Write api data to csv file
csvfile = open('Output Data/4_Parsed_API_Data.csv', "w")
csvfile.write(api_inf_exp_df.text)
csvfile.close()
