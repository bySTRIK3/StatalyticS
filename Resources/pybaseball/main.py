from pybaseball import batting_stats

print("Getting 2023 batting stats...")
df = batting_stats(2023)
print(df.head())
