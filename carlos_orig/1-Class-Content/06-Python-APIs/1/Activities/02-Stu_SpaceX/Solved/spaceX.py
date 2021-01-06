# Dependencies
import requests as req
import json

# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v1/launchpads/"

# Pretty print JSON for all launchpads
# response = req.get(url).json()
# print(json.dumps(response, indent=4, sort_keys=True))

# Pretty print JSON for a specific launchpad
response = req.get(url + "vafb_slc_4w").json()
print(json.dumps(response, indent=4, sort_keys=True))
