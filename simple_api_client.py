import requests
  
URL = "http://0.0.0.0:55555/api/get_sample/cpu"
  
location = "USSC"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
  
# sending get request and saving the response as response object
#r = requests.get(url = URL, params = PARAMS)
r = requests.get(url = URL)
  
# extracting data in json format
data = r.json()

print(data['sample'])
