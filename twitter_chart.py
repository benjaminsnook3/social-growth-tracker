import pandas as pd
import matplotlib.pyplot as plt

# ---- SETTINGS ----
CSV_FILE = "twitter_followers.csv"

# ---- LOAD DATA ----
df = pd.read_csv(CSV_FILE)

# ---- PLOT ----
plt.figure(figsize=(10, 6))

for column in df.columns[1:]:  # skip 'Date' column
    plt.plot(df["Date"], df[column], marker="o", label=column)

plt.title("Twitter Follower Growth")
plt.xlabel("Date")
plt.ylabel("Followers")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save & Show
plt.savefig("follower_growth_chart.png")
plt.show()
