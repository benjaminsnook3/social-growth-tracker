import requests
import csv
import os
from datetime import datetime

# ---- USER SETTINGS ----
BEARER_TOKEN = "YOUR_BEARER_TOKEN_HERE"  # paste from Twitter Dev Portal
USERNAMES = ["username", "anotherusername"]  # list of accounts (no @)
CSV_FILE = "twitter_followers.csv"

# ---- API CALL FUNCTION ----
def get_followers(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=public_metrics"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["public_metrics"]["followers_count"]
    else:
        print(f"Error {response.status_code} for {username}: {response.text}")
        return None

# ---- LOGGING FUNCTION ----
def log_followers():
    today = datetime.now().strftime("%Y-%m-%d")
    row = [today]
    for username in USERNAMES:
        followers = get_followers(username)
        row.append(followers)
    
    # If CSV doesn't exist, create with header
    if not os.path.exists(CSV_FILE):
        header = ["Date"] + USERNAMES
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)

    # Append today's data
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    print(f"Logged follower counts for {today}: {row[1:]}")

# ---- RUN SCRIPT ----
log_followers()
