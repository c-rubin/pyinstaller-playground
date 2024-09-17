import pandas as pd
import requests as re

def use_pandas():
    addresses = pd.read_csv("addresses.csv")
    print(addresses)

def use_requests():
    resp = re.get("https://google.com")
    if resp.status_code == 404: print("google.com doesn't exist")
    else: print("google.com exists")

def main():
    use_pandas()
    use_requests()

if __name__ == "__main__":
    main()