import pandas as pd
import requests
import re
from io import StringIO
from pathlib import Path
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath

# Helper functions
def is_int_like(x: str) -> bool:
    try:
        int(x)
        return True
    except (ValueError, TypeError):
        return False
    
def parent_segment(url: str) -> str:
    path = urlparse(url).path.rstrip("/")      # drop trailing slash if present
    p = PurePosixPath(path)
    if len(p.parts) < 2:
        return ""
    return unquote(p.parts[-2])

def download_data(output_path):

    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    urls = ["https://www.bikeraceinfo.com/giro/giroindx.html",
            "https://www.bikeraceinfo.com/tdf/tdfindex.html",
            "https://www.bikeraceinfo.com/vuelta/vuelta.html",
            "https://www.bikeraceinfo.com/classics/Amstel%20Gold%20Race/amstelindex.html",
            "https://www.bikeraceinfo.com/classics/Fleche%20Wallonne/flecheindex.html",
            "https://www.bikeraceinfo.com/classics/Ghent-Wevelgem/ghentindex.html",
            "https://www.bikeraceinfo.com/classics/Liege-Bastogne-Liege/liege-index.html",
            "https://www.bikeraceinfo.com/classics/Milan-San%20Remo/milan-san-remo-index.html",
            "https://www.bikeraceinfo.com/classics/paris-roubaix/paris-roubaix-index.html",
            "https://www.bikeraceinfo.com/classics/Tour%20of%20Flanders/flandndx.html",
            "https://www.bikeraceinfo.com/classics/Tour%20of%20Lombardy/lombindx.html",
            "https://www.bikeraceinfo.com/worlds/world-championships-index.html"
        ]


    for url in urls:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        html = resp.text

        raw_tables = pd.read_html(StringIO(html), flavor="lxml")

        relevant_tables = []
        captured_header = None

        for i, t in enumerate(raw_tables):
            if t.iat[0,0] == "Year":
                print("Found the header table")
                relevant_tables.append(t)

            if is_int_like(t.iat[0,0]) and int(t.iat[0,0]) > 1800:
                print("Found a second table")
                relevant_tables.append(t)

            # specific for page
            if url == "https://www.bikeraceinfo.com/classics/Fleche%20Wallonne/flecheindex.html":
                if t.iat[0,0] == "Bastogne and other cities - Huy":
                    print("Found a second table")
                    relevant_tables.append(t)
            
            if url == "https://www.bikeraceinfo.com/classics/paris-roubaix/paris-roubaix-index.html":
                if t.iat[0,0] == "1940-1942":
                    print("Found a second table")
                    relevant_tables.append(t)

            if url == "https://www.bikeraceinfo.com/tdf/tdfindex.html":
                if t.iat[0,0] == "1940-1946 World War II, no Tours held":
                    print("Found a second table")
                    relevant_tables.append(t)

            if url == "https://www.bikeraceinfo.com/vuelta/vuelta.html":
                if t.iat[0,0] == "2000  Aug 26-  Sept 17" or t.iat[0,0] == "2015  Aug 22-  Sept 13":
                    print("Found a second table")
                    relevant_tables.append(t)

            if url == "https://www.bikeraceinfo.com/worlds/world-championships-index.html":
                if t.iat[0,0] == "Aug 14  1960" or t.iat[0,0] == "Oct 15  2000":
                    print("Found a second table")
                    relevant_tables.append(t)
            
        header_table = relevant_tables[0]
        cols = header_table.iloc[0]
        final_table = pd.DataFrame(columns=cols)

        rows = header_table[1:]
        rows_aligned = rows.set_axis(final_table.columns, axis=1)

        final_table = pd.concat([final_table, rows_aligned], ignore_index=True)

        for i, t in enumerate(relevant_tables):
            if i == 0:
                continue

            rows = t[0:]
            rows_aligned = rows.set_axis(final_table.columns, axis=1)

            final_table = pd.concat([final_table, rows_aligned], ignore_index=True)

        dest = parent_segment(url)
        csv_path = output_path / dest
        final_table.to_csv(csv_path, index=False, encoding="utf-8")
        print(f"Wrote {csv_path}")