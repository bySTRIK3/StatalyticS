import pandas as pd

df = pd.read_csv("data/raw/batting_2023.csv")

if "Position" not in df.columns:
    print("⚠️ Position data not found in CSV.")
else:
    pos_stats = df.groupby("Position").sum(numeric_only=True)
    pos_stats.to_csv("data/processed/positional_totals_2023.csv")
    print("✅ Positional stats saved.")
