import pandas as pd

df = pd.read_csv("./Resources/pybaseball/data/raw/batting_2023.csv")

league_totals = df.sum(numeric_only=True)
league_totals_df = pd.DataFrame(league_totals).transpose()

league_totals_df.to_csv("./Resources/pybaseball/data/processed/league_totals_2023.csv", index=False)
print("✅ League totals saved to data/processed/league_totals_2023.csv")


