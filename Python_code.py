import json
import requests
import time
import pandas as ps
import re

jsonFile = open('test.json')
data = json.load(jsonFile)

url = "http://localhost:3002/people"

headers = {
    'Content-Type': 'application/json'
}



#Task 1: Create a file in your directory containing valid JSON data for your server, import it, and send it to the API using a POST request.

peopleResponse = requests.post(url, json=data, headers=headers)
time.sleep(0.01)


# #Task 2: Send a get request to your API and filter the data until you find the data you posted

peopleJson = requests.get(url)
time.sleep(0.01)
people = peopleJson.json()
for person in people:
    if person["fullName"] == "Ewan Laing":
        newEntry = person
        print(person)



# # #Task 3: Update the data using a PATCH and PUT request

id = person["id"]
newEntryUrl = (url + "/" + id)


updatedJob = {'job' : 'Senior Engineer'}
updatedPerson = requests.patch(newEntryUrl, updatedJob)
time.sleep(0.01)


updatedPersonJson = { 
    "fullName": "Ewan Laing",
    "email": "ewan.laing@2itesting.com",
    "job": "Prime Minister",
    "dob": "30/11/1989"}
updatedPerson = requests.put(newEntryUrl, updatedPersonJson)
time.sleep(0.01)


# #Task 4: Remove the data using a DELETE request


deleteNewEntry = requests.delete(newEntryUrl)
time.sleep(0.01)




#Task 5: Create a json file with various example of people data, within the data create several duplicates, 
# import this data, remove duplicates and POST to the API

newJsonFile = open('newData.json')
newData = json.load(newJsonFile)

if isinstance(newData, list):
    
    def all_duplicate(data):
        dd = ps.DataFrame(data)
        dd.drop_duplicates(inplace=True)
        return dd.to_dict(orient='records')
    uniqueList = all_duplicate(newData)
    time.sleep(0.01)

else:
    print("import is not a valid list")
    

for person in uniqueList:
    if isinstance(person, dict):
        if ("@" in person["email"]) and (re.search("\d{1,2}\/\d{1,2}\/\d{2,4}", person["dob"])):
            newPersonResponse = requests.post(url, json=person, headers=headers)
            time.sleep(0.01)
        else:
            print("data does not match")

        
    else:
        print(person)
        print("is not a valid object")




#Task 6: When importing the data, add some validation to ensure the data is structured how you would expect. Correct data types, etc.