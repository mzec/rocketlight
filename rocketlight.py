import steamapi
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

path = os.path.dirname(os.path.abspath(__file__))

with open(path + '/input/apikey.txt', 'r') as f:
    myapikey = f.read().strip()

with open(path + '/input/rocketfriends.txt', 'r') as f:
    rocketfriends = f.read().splitlines()

steamapi.core.APIConnection(api_key = myapikey, validate_key = True)

notifier = False
for friend in rocketfriends:
    user_rocket = False
    user = steamapi.user.SteamUser(friend)
    if user.currently_playing:
        if user.currently_playing.appid == '252950':
            notifier = True
            user_rocket = True
    print(user.name + ' - ' + str(user_rocket))

print(notifier)
GPIO.output(11, notifier)
