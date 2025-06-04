from pybaseball import batting_stats

print("Getting 2023 batting stats...")
df = batting_stats(2023)
print(df.head())

from pybaseball import batting_stats
import pandas as pd

print("Fetching 2023 league-wide batting stats...")

# Get league batting stats
batting = batting_stats(2023)
print(batting.head())

# Save to CSV
batting.to_csv("batting_2023.csv", index=False)
print("✅ Batting stats saved to batting_2023.csv")


