import json
import requests
token='EAAFoZCgPEfNkBAMMvLfGoc7KglM4u9D47Di4YAUHm1q0XDqyclSMZBlczvBl46fnxZAEogJ3I7l34aznrFkP4xp2S3vOsgfyVveOZAIpapO7snmryZBogsxwJ8FdhIdwzhZBFGSGKtyD1BQlgGyz9ZA3C4VXN5RJqayNes5ixWUCwpyPbyNwajydvGAF7xe4uIZD'
url="https://graph.facebook.com/v3.3/me?access_token="+token
m1=requests.get(url)
m2=m1.json()
print(m2)
url="https://graph.facebook.com/v3.3/me/friends?access_token="+token
m1=requests.get(url)
m2=m1.json()
print(m2)



