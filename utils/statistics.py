import pandas as pd
from pathlib import Path

from utils.helpers import to_long, to_long_1

def most_podiums(input):
    input = Path(input)
    amstel = pd.read_csv(input / "amstel")
    fleche = pd.read_csv(input / "fleche")
    gend = pd.read_csv(input / "gend")
    giro = pd.read_csv(input / "giro")
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tdf = pd.read_csv(input / "tdf")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    vuelta = pd.read_csv(input / "vuelta")
    worlds = pd.read_csv(input / "worlds")

    parts = []
    dfs = [amstel, fleche, gend, giro, liege, msr, pr, tdf, tof, tol, vuelta, worlds]
    for df in dfs:
        parts += [to_long(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

def most_podiums_gt(input):
    input = Path(input)
    giro = pd.read_csv(input / "giro")
    tdf = pd.read_csv(input / "tdf")
    vuelta = pd.read_csv(input / "vuelta")

    parts = []
    dfs = [giro, tdf, vuelta]
    for df in dfs:
        parts += [to_long(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

def most_podiums_monuments(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")

    parts = []
    dfs = [liege, msr, pr, tof, tol]
    for df in dfs:
        parts += [to_long(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

def most_podiums_monuments_wc(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    worlds = pd.read_csv(input / "worlds")

    parts = []
    dfs = [liege, msr, pr, tof, tol, worlds]
    for df in dfs:
        parts += [to_long(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums


def most_podiums_monuments_wc_gt(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    worlds = pd.read_csv(input / "worlds")
    giro = pd.read_csv(input / "giro")
    vuelta = pd.read_csv(input / "vuelta")
    tdf = pd.read_csv(input / "tdf")

    parts = []
    dfs = [liege, msr, pr, tof, tol, worlds, tdf, giro, vuelta]
    for df in dfs:
        parts += [to_long(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums


def most_wins(input):
    input = Path(input)
    amstel = pd.read_csv(input / "amstel")
    fleche = pd.read_csv(input / "fleche")
    gend = pd.read_csv(input / "gend")
    giro = pd.read_csv(input / "giro")
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tdf = pd.read_csv(input / "tdf")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    vuelta = pd.read_csv(input / "vuelta")
    worlds = pd.read_csv(input / "worlds")

    parts = []
    dfs = [amstel, fleche, gend, giro, liege, msr, pr, tdf, tof, tol, vuelta, worlds]
    for df in dfs:
        parts += [to_long_1(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums


def most_wins_gt(input):
    input = Path(input)
    giro = pd.read_csv(input / "giro")
    tdf = pd.read_csv(input / "tdf")
    vuelta = pd.read_csv(input / "vuelta")

    parts = []
    dfs = [giro, tdf, vuelta]
    for df in dfs:
        parts += [to_long_1(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

def most_wins_monuments(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")

    parts = []
    dfs = [liege, msr, pr, tof, tol]
    for df in dfs:
        parts += [to_long_1(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

def most_wins_monuments_wc(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    worlds = pd.read_csv(input / "worlds")

    parts = []
    dfs = [liege, msr, pr, tof, tol, worlds]
    for df in dfs:
        parts += [to_long_1(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums


def most_wins_monuments_wc_gt(input):
    input = Path(input)
    liege = pd.read_csv(input / "liege")
    msr = pd.read_csv(input / "msr")
    pr = pd.read_csv(input / "roubaix")
    tof = pd.read_csv(input / "flanders")
    tol = pd.read_csv(input / "lombardia")
    worlds = pd.read_csv(input / "worlds")
    giro = pd.read_csv(input / "giro")
    vuelta = pd.read_csv(input / "vuelta")
    tdf = pd.read_csv(input / "tdf")

    parts = []
    dfs = [liege, msr, pr, tof, tol, worlds, giro, vuelta, tdf]
    for df in dfs:
        parts += [to_long_1(df)]

    long = pd.concat(parts, ignore_index=True)

    podiums = (long
        .groupby("rider", as_index=False)
        .size()
        .sort_values("size", ascending=False)
    )
    return podiums

            
