import requests

# Base URL of the FastAPI service
base_url = "http://localhost:8000"

# Make a GET request
get_response = requests.get(base_url, params={"param1": "value1", "param2": "value2"})
print("GET response:")
print(get_response.json())

# Make a POST request
post_data = {"key1": "value1", "key2": "value2"}
post_response = requests.post(base_url, json=post_data)
print("POST response:")
print(post_response.json())
