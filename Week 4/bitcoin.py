import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid Command line argurment")
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")
    api_key = "237edd615c7e54887c9a7ce0721d8e52ac21b24c722659f691a57bf996be4a89"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=237edd615c7e54887c9a7ce0721d8e52ac21b24c722659f691a57bf996be4a89"
    try:
        response = requests.get(url)
        response.raise_for_status
    except requests.RequestException:
        sys.exit("Could not retrieve data")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total_cost = number_of_bitcoins * price
    print(f"{total_cost:,.4f}")

if __name__ == "__main__":
    main()



    
