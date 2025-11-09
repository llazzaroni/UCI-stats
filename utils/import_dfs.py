import pandas as pd
from pathlib import Path
from functools import reduce
import unicodedata
import re

def fix_weird(col):
    return (
        col.astype(str)
           .str.replace('""', '"', regex=False)
           .str.encode("latin1", errors="ignore")
           .str.decode("utf-8", errors="ignore")
           .str.replace(r"\s+", " ", regex=True)
           .str.strip()
    )

def import_amstel(input):
    amstel = pd.read_csv(input / "Amstel Gold Race")
    amstel = amstel[["Year", "1st place", "2nd Place", "3rd Place"]]
    amstel["Year"] = pd.to_numeric(amstel["Year"], errors="coerce")
    amstel["1st place"] = (
        amstel["1st place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    amstel["2nd Place"] = (
        amstel["2nd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    amstel = amstel.rename(columns={"2nd Place": "2nd place"})
    amstel["3rd Place"] = (
        amstel["3rd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    amstel = amstel.rename(columns={"3rd Place": "3rd place"})
    amstel.loc[amstel["Year"].eq(2020), "1st place"] = ""
    amstel.loc[amstel["Year"].eq(2020), "2nd place"] = ""
    amstel.loc[amstel["Year"].eq(2020), "3rd place"] = ""
    return amstel

def import_fleche(input):
    fleche = pd.read_csv(input / "Fleche Wallonne")
    fleche = fleche[["Year", "1st Place", "2nd Place", "3rd Place"]]
    fleche = fleche[pd.to_numeric(fleche["Year"], errors="coerce").notna()].copy()
    fleche["Year"] = pd.to_numeric(fleche["Year"], errors="coerce").astype("Int64")
    fleche["1st Place"] = (
        fleche["1st Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    fleche = fleche.rename(columns={"1st Place": "1st place"})
    fleche["2nd Place"] = (
        fleche["2nd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    fleche = fleche.rename(columns={"2nd Place": "2nd place"})
    fleche["3rd Place"] = (
        fleche["3rd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    fleche = fleche.rename(columns={"3rd Place": "3rd place"})
    fleche.loc[fleche["Year"].eq(1940), "1st place"] = ""
    fleche.loc[fleche["Year"].eq(1940), "2nd place"] = ""
    fleche.loc[fleche["Year"].eq(1940), "3rd place"] = ""
    return fleche

def import_gend(input):
    gend = pd.read_csv(input / "Ghent-Wevelgem")
    gend = gend[gend["Year"] != "1940  1944"].copy()
    gend = gend[["Year", "1st place", "2nd Place", "3rd Place"]]
    gend["Year"] = pd.to_numeric(gend["Year"], errors="coerce").astype("Int64")
    gend["1st place"] = (
        gend["1st place"].astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r'["“”]', "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    gend["2nd Place"] = (
        gend["2nd Place"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    gend = gend.rename(columns={"2nd Place": "2nd place"})
    gend["3rd Place"] = (
        gend["3rd Place"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    gend = gend.rename(columns={"3rd Place": "3rd place"})
    missing_years = [1940, 1941, 1942, 1943, 1944]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    gend = pd.concat([gend, blank_rows], ignore_index=True)
    gend = gend.sort_values("Year").reset_index(drop=True)
    return gend

def import_giro(input):
    giro = pd.read_csv(input / "giro")
    giro = giro[["Year", "Winner", "2nd Place", "3rd Place"]]
    giro["Year"] = pd.to_numeric(giro["Year"], errors="coerce").astype("Int64")
    giro = giro[(giro["Year"] < 1941) | (giro["Year"] > 1945)].copy()
    giro["Winner"] = (
        giro["Winner"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    giro["Winner"] = (
        giro["Winner"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.replace(r"\s*,\s*$", "", regex=True)
          .str.strip()
    )
    giro["Winner"] = (
        giro["Winner"]
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    giro = giro.rename(columns={"Winner": "1st place"})
    giro["2nd Place"] = (
        giro["2nd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    giro["2nd Place"] = (
        giro["2nd Place"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.replace(r"\s*,\s*$", "", regex=True)
          .str.strip()
    )
    giro["2nd Place"] = (
        giro["2nd Place"]
          .str.replace(r'"\s*[^"]+\s*"', "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    giro["2nd Place"] = (
        giro["2nd Place"]
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    giro = giro.rename(columns={"2nd Place": "2nd place"})
    giro["3rd Place"] = (
        giro["3rd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    giro["3rd Place"] = (
        giro["3rd Place"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.replace(r"\s*,\s*$", "", regex=True)
          .str.strip()
    )
    giro["3rd Place"] = (
        giro["3rd Place"]
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    giro = giro.rename(columns={"3rd Place": "3rd place"})
    missing_years = [1941, 1942, 1943, 1944, 1945, 1915, 1916, 1917, 1918]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    giro = pd.concat([giro, blank_rows], ignore_index=True)
    giro = giro.sort_values("Year").reset_index(drop=True)
    return giro

def import_liege(input):
    liege = pd.read_csv(input / "Liege-Bastogne-Liege")
    liege = liege[["Year", "1st place", "2nd Place", "3rd Place"]]
    liege["Year"] = pd.to_numeric(liege["Year"], errors="coerce")
    liege["1st place"] = (
        liege["1st place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    liege["2nd Place"] = (
        liege["2nd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    liege = liege.rename(columns={"2nd Place": "2nd place"})
    liege["3rd Place"] = (
        liege["3rd Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    liege = liege.rename(columns={"3rd Place": "3rd place"})
    missing_years = []
    for i in range(1895, 1908):
        missing_years.append(i)
    missing_years.append(1910)
    for i in range(1914, 1919):
        missing_years.append(i)
    for i in range(1940, 1943):
        missing_years.append(i)
    missing_years.append(1944)
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    liege = pd.concat([liege, blank_rows], ignore_index=True)
    liege = liege.sort_values("Year").reset_index(drop=True)
    liege.loc[liege["Year"].eq(1957), "1st place"] = "Frans Schoubben; Germain Derycke"
    liege.loc[liege["Year"].eq(1957), "2nd place"] = ""
    return liege

def import_msr(input):
    msr = pd.read_csv(input / "Milan-San Remo")
    msr = msr[["Year", "First", "Second", "Third"]]
    msr["Year"] = pd.to_numeric(msr["Year"], errors="coerce")
    msr["First"] = (
        msr["First"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    msr = msr.rename(columns={"First": "1st place"})
    msr["Second"] = (
        msr["Second"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    msr = msr.rename(columns={"Second": "2nd place"})
    msr["Third"] = (
        msr["Third"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    msr = msr.rename(columns={"Third": "3rd place"})
    missing_years = [1916, 1944, 1945]
    for year in missing_years:
        msr.loc[msr["Year"].eq(year), "1st place"] = ""
        msr.loc[msr["Year"].eq(year), "2nd place"] = ""
        msr.loc[msr["Year"].eq(year), "3rd place"] = ""
    msr.loc[msr["Year"].eq(1976), "3rd place"] = "Michel Laurent"
    msr.loc[msr["Year"].eq(1907), "3rd place"] = "Giovanni Gerbi"
    return msr

def import_roubaix(input):
    pr = pd.read_csv(input / "paris-roubaix")
    pr = pr[["Year", "First", "Second", "Third"]]
    pr["Year"] = pd.to_numeric(pr["Year"], errors="coerce")
    pr = pr[pr["Year"] >= 1896]
    pr["First"] = (
        pr["First"].astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r'["“”]', "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    pr["Second"] = (
        pr["Second"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    pr = pr.rename(columns={"First": "1st place"})
    pr["Third"] = (
        pr["Third"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    pr = pr.rename(columns={"Third": "3rd place"})
    pr["Year"] = pr["Year"].astype(int)
    pr = pr.rename(columns={"Second": "2nd place"})
    missing_years = [1915, 1916, 1917, 1918, 1940, 1941, 1942]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    pr = pd.concat([pr, blank_rows], ignore_index=True)
    pr = pr.sort_values("Year").reset_index(drop=True)
    pr.loc[pr["Year"].eq(1949), "1st place"] = 'André Mahé; Serse Coppi'
    pr.loc[pr["Year"].eq(1949), "2nd place"] = ""
    pr.loc[pr["Year"].eq(2020), "1st place"] = ''
    pr.loc[pr["Year"].eq(2020), "2nd place"] = ''
    pr.loc[pr["Year"].eq(2020), "3rd place"] = ''
    return pr

def import_tdf(input):
    tdf = pd.read_csv(input / "tdf")
    tdf = tdf[["Year", "1st Place, age and time  (1905-1912, points  determined the winner)", "2nd Place, time  behind winner.  If points,  total points", "3rd place, time  behind winner.  If points,  total points"]]
    tdf["Year"] = pd.to_numeric(tdf["Year"], errors="coerce").astype("Int64")
    tdf["1st Place, age and time  (1905-1912, points  determined the winner)"] = (
        tdf["1st Place, age and time  (1905-1912, points  determined the winner)"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tdf = tdf.rename(columns={"1st Place, age and time  (1905-1912, points  determined the winner)": "1st place"})
    tdf["1st place"] = (
        tdf["1st place"].astype(str)
          .str.replace(r",\s*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tdf["2nd Place, time  behind winner.  If points,  total points"] = (
        tdf["2nd Place, time  behind winner.  If points,  total points"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tdf = tdf.rename(columns={"2nd Place, time  behind winner.  If points,  total points": "2nd place"})
    tdf["2nd place"] = (
        tdf["2nd place"].astype(str)
          .str.replace(r",\s*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tdf["3rd place, time  behind winner.  If points,  total points"] = (
        tdf["3rd place, time  behind winner.  If points,  total points"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tdf = tdf.rename(columns={"3rd place, time  behind winner.  If points,  total points": "3rd place"})
    tdf["3rd place"] = (
        tdf["3rd place"].astype(str)
          .str.replace(r",\s*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
          .str.replace(r"^\s*([^,]+),\s*(.+)$", r"\2 \1", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tdf = tdf[~tdf["Year"].isna()].copy()
    tdf = tdf[tdf["Year"] < 2026].copy()
    missing_years = [1915, 1916, 1917, 1918, 1940, 1941, 1942, 1943, 1944, 1945, 1946]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    tdf = pd.concat([tdf, blank_rows], ignore_index=True)
    tdf = tdf.sort_values("Year").reset_index(drop=True)
    for i in range(1999, 2006):
        tdf.loc[tdf["Year"].eq(i), "1st place"] = ""
    return tdf

def import_flanders(input):
    tof = pd.read_csv(input / "Tour of Flanders")
    tof = tof[["Year", "First", "Second", "Third"]]
    tof["Year"] = pd.to_numeric(tof["Year"], errors="coerce").astype("Int64")
    tof["First"] = (
        tof["First"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tof = tof.rename(columns={"First": "1st place"})
    tof["Second"] = (
        tof["Second"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tof = tof.rename(columns={"Second": "2nd place"})
    tof["Third"] = (
        tof["Third"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    tof = tof.rename(columns={"Third": "3rd place"})
    tof = tof[~tof["Year"].isna()].copy()
    tof.loc[tof["Year"].eq(1977), "2nd place"] = ""
    missing_years = [1915, 1916, 1917, 1918]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    tof = pd.concat([tof, blank_rows], ignore_index=True)
    tof = tof.sort_values("Year").reset_index(drop=True)
    return tof

def import_lombardia(input):
    tol = pd.read_csv(input / "Tour of Lombardy")
    tol = tol[["Year", "First", "Second", "Third"]]
    tol["Year"] = pd.to_numeric(tol["Year"], errors="coerce")
    tol["First"] = (
        tol["First"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tol = tol.rename(columns={"First": "1st place"})
    tol["Second"] = (
        tol["Second"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tol = tol.rename(columns={"Second": "2nd place"})
    tol["Third"] = (
        tol["Third"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    tol = tol.rename(columns={"Third": "3rd place"})
    missing_years = [1943, 1944]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    tol = pd.concat([tol, blank_rows], ignore_index=True)
    tol = tol.sort_values("Year").reset_index(drop=True)
    return tol

def import_vuelta(input):
    vuelta = pd.read_csv(input / "vuelta")
    vuelta = vuelta[["Year", "First Place", "Second", "Third"]]
    vuelta["Year"] = (
        vuelta["Year"].astype(str).str.extract(r"(\d{4})", expand=False)
        .astype("Int64")
    )
    vuelta["Year"] = pd.to_numeric(vuelta["Year"], errors="coerce")
    vuelta["First Place"] = (
        vuelta["First Place"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    vuelta = vuelta.rename(columns={"First Place": "1st place"})
    vuelta["Second"] = (
        vuelta["Second"].astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    vuelta = vuelta.rename(columns={"Second": "2nd place"})
    vuelta["Third"] = (
        vuelta["Third"].astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    vuelta = vuelta.rename(columns={"Third": "3rd place"})
    missing_years = [1937, 1938, 1939, 1940, 1943, 1944, 1949, 1951, 1952, 1953, 1954]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    vuelta = pd.concat([vuelta, blank_rows], ignore_index=True)
    vuelta = vuelta.sort_values("Year").reset_index(drop=True)
    return vuelta

def import_worlds(input):
    worlds = pd.read_csv(input / "worlds")
    worlds = worlds[["Year", "First", "Second", "Third"]]
    worlds["Year"] = (
        worlds["Year"]
          .astype(str)
          .str.extract(r"(\d{4})", expand=False)
          .astype("Int64")
    )
    worlds["Year"] = pd.to_numeric(worlds["Year"], errors="coerce")
    worlds["First"] = (
        worlds["First"]
          .astype(str)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.strip()
    )
    worlds["First"] = (
        worlds["First"]
          .astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    worlds = worlds.rename(columns={"First": "1st place"})
    worlds["Second"] = (
        worlds["Second"].astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    worlds = worlds.rename(columns={"Second": "2nd place"})
    worlds["Third"] = (
        worlds["Third"].astype(str)
          .str.replace(r"\([^)]*\)", "", regex=True)
          .str.replace(r"\s*(?:@|s\.t\.).*$", "", regex=True)
          .str.replace(r"\s*\d.*$", "", regex=True)
          .str.replace(r"\s+", " ", regex=True)
          .str.strip()
    )
    worlds = worlds.rename(columns={"Third": "3rd place"})
    worlds = worlds[~(worlds["Year"] == 1939)].copy()
    missing_years = [1939, 1940, 1941, 1942, 1943, 1944, 1945]
    blank_rows = pd.DataFrame({
        "Year": missing_years,
        "1st place": "",
        "2nd place": "",
        "3rd place": "",
    })
    worlds = pd.concat([worlds, blank_rows], ignore_index=True)
    worlds = worlds.sort_values("Year").reset_index(drop=True)
    return worlds

def process_tables(input, output):
    input = Path(input)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    cols = ["1st place","2nd place","3rd place"]

    amstel = import_amstel(input)
    amstel[cols] = amstel[cols].apply(fix_weird)
    amstel.to_csv(output / "amstel", index=False)

    fleche = import_fleche(input)
    fleche[cols] = fleche[cols].apply(fix_weird)
    fleche.to_csv(output / "fleche", index=False)

    gend = import_gend(input)
    gend[cols] = gend[cols].apply(fix_weird)
    gend.to_csv(output / "gend", index=False)

    giro = import_giro(input)
    giro[cols] = giro[cols].apply(fix_weird)
    giro.to_csv(output / "giro", index=False)

    liege = import_liege(input)
    liege[cols] = liege[cols].apply(fix_weird)
    liege.to_csv(output / "liege", index=False)

    msr = import_msr(input)
    msr[cols] = msr[cols].apply(fix_weird)
    msr.to_csv(output / "msr", index=False)

    roubaix = import_roubaix(input)
    roubaix[cols] = roubaix[cols].apply(fix_weird)
    roubaix.to_csv(output / "roubaix", index=False)

    tdf = import_tdf(input)
    tdf[cols] = tdf[cols].apply(fix_weird)
    tdf.to_csv(output / "tdf", index=False)

    flanders = import_flanders(input)
    flanders[cols] = flanders[cols].apply(fix_weird)
    flanders.to_csv(output / "flanders", index=False)

    lombardy = import_lombardia(input)
    lombardy[cols] = lombardy[cols].apply(fix_weird)
    lombardy.to_csv(output / "lombardia", index=False)

    vuelta = import_vuelta(input)
    vuelta[cols]  = vuelta[cols].apply(fix_weird)
    vuelta.to_csv(output / "vuelta", index=False)

    worlds = import_worlds(input)
    worlds[cols]  = worlds[cols].apply(fix_weird)
    worlds.to_csv(output / "worlds", index=False)

