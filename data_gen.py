import requests 
import pandas as pd 
import os 
from dotenv import load_dotenv

API_KEY = os.getenv("apikey")
SYMBOL = "AAPL"

url = "https://www.alphavantage.co/query"

params = {
    "function" : "TIME_SERIES_DAILY",
    "apikey" : API_KEY,
    "symbol"  : SYMBOL,         # docx based params 
    "outputsize" : "compact"
}

response = requests.get(url,params=params)

# pull out the data :
data = response.json()

# check if the data is properly pulled :
print(data.keys())

ts = data["Time Series (Daily)"] # -> Documentation based 

# Convert the api response into dataframes (currently is a dict -> dataframe)
df = pd.DataFrame.from_dict(ts, orient ="index")

# VALID DATA CONVERSIONS :

# Convert to date and time
df.index = pd.to_datetime(df.index)

# Convert strings -> float:
df = df.astype(float)

# Define the columns 
df.columns = ["open", "high", "low", "close", "volume"]

# Convert to csv to save from api limit issues 
df.to_csv(r"C:/Users/admin/Downloads/trad_data.csv")

print("Data sucessfully fetched from API and saved to csv")

