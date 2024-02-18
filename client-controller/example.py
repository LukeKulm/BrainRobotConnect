import requests
import time
URL = "https://spot-rest-api.vercel.app/api/spot"
r = requests.post(URL, json={"data":"rest"})
time.sleep(3)
r = requests.post(URL, json={"data":"left"})
time.sleep(3)
r = requests.post(URL, json={"data":"right"})
time.sleep(3)
r = requests.post(URL, json={"data":"forward"})
time.sleep(3)
r = requests.post(URL, json={"data":"rest"})
time.sleep(3)
