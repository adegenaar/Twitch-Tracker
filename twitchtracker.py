import os
from pprint import pprint
from twitchAPI import Twitch

twitchid = os.environ.get("TWITCH_ID")
# print(twitchid)

twitchsecret = os.environ.get("TWITCH_SECRET")
# print(twitchsecret)

twitch = Twitch(twitchid, twitchsecret)  # token and secret
twitch.authenticate_app([])
# get the streams call
# print(twitch.get_streams(game_id=33214))


# get ID of user
# user_info = twitch.get_users(logins=['my_username'])
# user_id = user_info['data'][0]['id']

user_logins = ["al_degenaar"]

# get user information
users = twitch.get_users(logins=user_logins)

# print("Users:")
# pprint(users)

broadcasters = []

# get the follows for a given user
for user in users["data"]:
    # print("user:")
    # pprint(user["id"])
    follows = twitch.get_users_follows(from_id=user["id"])
    #    print("Follows:")
    #    pprint(follows)
    cursor = follows["pagination"]["cursor"]
    data = follows["data"]
    #    pprint(data)
    for broadcaster in data:
        # print("Broadcaster:")
        # print(broadcaster["to_name"] + ":" + broadcaster["to_id"])
        broadcasters.append(broadcaster["to_name"])
        # pprint(twitch.get_streams(user_login=broadcaster["to_name"]))

print("Broadcasters:")
pprint(broadcasters)
# get Live Stream information, not offline streams
streams = twitch.get_streams(user_login=broadcasters)
pprint(streams)
