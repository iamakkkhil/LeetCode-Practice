import requests

# Assume that you are building an analytics dashboard application that requires you to return volume chart data for exchanges subscribed by users


def getExchanges():
    response = requests.get("https://api.coingecko.com/api/v3/exchanges/list")
    if response.status_code != 200:
        print("Something went wrong")
        return []

    response_body = response.json()
    return response_body


def getVolumeChartData(exchangeID):
    # Get volume chart data by performing a get request
    api = (
        f"https://api.coingecko.com/api/v3/exchanges/{exchangeID}/volume_chart?days=10"
    )
    response = requests.get(api)
    if response.status_code != 200:
        print("Something went wrong")
        return []
    response_body = response.json()
    return response_body


# print(getVolumeChartData("1bch"))


def getExchangeDataForUsers(users):
    # Given: List of users and associated list of exchanges return corresponding exchange volume data
    # return_body example [(userid, {exchange 1: chart data, exchange 2: chart data})]
    ids_dict = {}

    for user in users:
        ids = user[1]
        for id_ in ids:
            if id_ not in ids_dict.keys():
                ids_dict[id_] = {}

    exchanges = getExchanges()
    for exchange in exchanges:
        if exchange["name"] in ids_dict.keys():
            ids_dict[exchange["name"]] = getVolumeChartData(exchange["id"])

    return ids_dict


users = [
    ("Bob", ["AAX", "AuroraSwap"]),
    ("Alice", ["Bitfinex"]),
    ("Sam", ["CoinDCX", "AAX"]),
]

users2 = [
    ("Bob", ["AAX", "AuroraSwap"]),
    ("Alice", ["Bitfinex"]),
    ("Sam", ["CoinDCX", "AAX"]),
    ("Akhil", ["asdas", "CoinDCX"]),
]

print(getExchangeDataForUsers(users2))

# Note Users can be subscribed to the same exchanges, Ensure that we do as little API calls as possible to increase latency
