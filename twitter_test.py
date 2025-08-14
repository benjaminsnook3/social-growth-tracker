import requests

# ---- USER SETTINGS ----
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAI5S3gEAAAAAW0LX29ArezUSVBnySms5SiPzGOA%3DBAaqzKmuYb6OEOJXfyvsufCPD9SkR80bs78W632y3gjOQLKpNZ"  # paste from Twitter Dev Portal
USERNAME = "BuniMunki"  # without @

# ---- API CALL ----
url = f"https://api.twitter.com/2/users/by/username/{USERNAME}?user.fields=public_metrics"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    followers = data["data"]["public_metrics"]["followers_count"]
    print(f"{USERNAME} has {followers} followers.")
else:
    print(f"Error {response.status_code}: {response.text}")
