from pybaseball import batting_stats, pitching_stats
import os

# Make sure data/raw exists
os.makedirs("data/raw", exist_ok=True)

# Fetch batting stats for 2023
print("📊 Fetching 2023 batting stats...")
batting_df = batting_stats(2023)
batting_df.to_csv("data/raw/batting_2023.csv", index=False)
print("✅ Saved batting_2023.csv")

# Fetch pitching stats for 2023
print("📊 Fetching 2023 pitching stats...")
pitching_df = pitching_stats(2023)
pitching_df.to_csv("data/raw/pitching_2023.csv", index=False)
print("✅ Saved pitching_2023.csv")


