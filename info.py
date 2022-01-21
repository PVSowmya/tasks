
import requests
import copy
requests.packages.urllib3.disable_warnings() # Disable SSL warnings in requests #
url = "https://grid-master/wapi/v2.11/record:host?_return_as_object=1"
response = requests.request("GET", url, auth=('admin', 'Infoblox'), verify=False)
authcookie = copy.copy(response.cookies[‘ibapauth’])
print(authcookie)

