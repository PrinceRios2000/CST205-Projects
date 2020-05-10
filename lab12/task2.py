#Authors: Prince Rios and Alex Espinoza
#Last modified: 10 March 2020
#Description: This code retrieves data of a specific user the fortnite tracker network API. First, the code imports requests to request the data
#from the tracker network. Next, a variable is created that represents the url link to a specific profile. After this, a headers dictionary is
#created with one key and the value being the api key. Finally, the code uses requests.get method that takes in the url and headers dictionary as 
#parameters to retrieve the data. The resulting data is printed using the .text() method. 
import requests

user = input("Enter a psn user\n")

URL = f"https://api.fortnitetracker.com/v1/profile/psn/{user}"

headers = {'TRN-Api-Key' : 'e1331dce-bf2b-4e07-a00f-728ff529edc0'}

res = requests.get(URL, headers=headers)

print(res.json()['lifeTimeStats'])