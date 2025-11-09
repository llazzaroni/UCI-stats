import pandas as pd

def to_long(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in ["1st place", "2nd place", "3rd place"] if c in df.columns]
    m = df.melt(id_vars="Year", value_vars=cols, var_name="position", value_name="rider")

    m = m.dropna(subset=["rider"])

    m["rider"] = m["rider"].astype(str).str.strip()

    m["rider"] = m["rider"].str.split(";")
    m = m.explode("rider")
    m["rider"] = m["rider"].str.strip()
    m = m[m["rider"].ne("")]

    m = m.dropna(subset=["rider"])
    m["rider"] = m["rider"].str.lower()

    return m[["Year", "position", "rider"]]

def to_long_1(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["1st place"]
    m = df.melt(id_vars="Year", value_vars=cols, var_name="position", value_name="rider")

    m = m.dropna(subset=["rider"])

    m["rider"] = m["rider"].astype(str).str.strip()

    m["rider"] = m["rider"].str.split(";")
    m = m.explode("rider")
    m["rider"] = m["rider"].str.strip()
    m = m[m["rider"].ne("")]

    m = m.dropna(subset=["rider"])
    m["rider"] = m["rider"].str.lower()

    return m[["Year", "position", "rider"]]