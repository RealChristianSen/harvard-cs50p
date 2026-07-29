import requests
import sys


try:

    # takes command-line arg and assigns it to n
    n = float(sys.argv[1])

    # assigns response the query response from the coincap api
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=05b478cb1b1691fe8dc122495088edb3ba471eba20318a88d6e3a1d229cd4651")

    # assigns content the json formatted data of response
    content = response.json()

    # assigns price the current price of bitcoin
    price = float(content["data"]["priceUsd"])

    # assigns total_cost the product of the current price of bitcoin and the command-line argument
    total_cost = price * n

    # prints the total cost, to 4 decimal places, with a $ in front of it, seperated every thousands place by a comma
    print(f"${total_cost:,.4f}")

# exits the program if there is a RequestException with exit code 1
except requests.RequestException:
    sys.exit(1)

# exits the program if there is a IndexError with exit code 1
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)

# exits the program if there is a ValueErrorwith exit code 1
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
