import requests
import json

# Set the URL of our endpoint
url = "https://api.ciscospark.com/v1/rooms"

# Set your spark token here
SPARK_TOKEN = "CHANGEME"

# Change this to be the room name as it appears in your spark client
SPARK_ROOM_NAME = "Demo Spark Room"


# create headers which will be used in all requests
headers = {
    'authorization': "Bearer {}".format(SPARK_TOKEN),
    'content-type': "application/json",
    }

# get a list of rooms
print ("SENDING A MESSAGE TO SPARK ROOM")
print ("==============================================")

response = requests.request("GET", url, headers=headers)

print ("Status Code received from server: {}".format(response.status_code))
print ("Text Response Recieved from server: {}".format(response.text))

# load text into json
room_data = json.loads(response.text)

# assign a variable for the list in response
list_of_rooms = room_data['items']

# iterate over room list and match based on Room name
for room in list_of_rooms:
    # find our room
    if room['title'] == SPARK_ROOM_NAME:
        # display room id
        print(room['id'])
        # save it for later
        our_room_id = room['id']


# only execute this code if we found a room id in the previous block
if our_room_id:

    print ("SENDING A MESSAGE TO SPARK ROOM")
    print ("==================================")

    # craft the body of our message using a python dictionary
    our_message = {"roomId": our_room_id,
                   "text": "this is a test message from python"
                   }

    # dump our dictionary to JSON
    json_message = json.dumps(our_message)

    # send a message to the spark room
    message_url = "https://api.ciscospark.com/v1/messages"
    response = requests.post(message_url, headers=headers, data=json_message)

    # display from information about the request
    print ("Status Code received from server: {}".format(response.status_code))
    print ("Text Response Recieved from server: {}".format(response.text))

    print("GETTING MESSAGES")
    print ("==================================")

    # get messages from room
    params = {"roomId": our_room_id}
    response = requests.get(message_url, headers=headers, params=params)

    # display from information about the request
    print ("Status Code received from server: {}".format(response.status_code))
    print ("Text Response Recieved from server: {}".format(response.text))

    # list each messages text value
    for msg in response.json()['items']:
        print msg['text']

else:

    print("Could not find room named {}".format(SPARK_ROOM_NAME))
