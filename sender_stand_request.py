import data
import configuration
import requests

def new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                             json=data.user_body,
                             headers=data.headers)

    if response.status_code == 201:
        return response.json().get("track")
    else:
        raise Exception(f"Failed to create order. Status code: {response.status_code}")


def response():
    return None