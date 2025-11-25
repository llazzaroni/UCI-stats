# UCI-stats

A Python utility for exploring statistics of the podiums of the most important cycling races throughout history.

> **Status:** Work-in-progress. Average speed are to be included, as well as statistics linking different competitions.

---

## Features

- Download raw data from the website https://www.bikeraceinfo.com
- Process the raw data to get a clean csv file listing years and podiums for each race
- Find who collected more podiums/wins over different groups of races (e.g. monuments, gts, monuments and wc...)  
---

## Project structure

```
UCI-stats/
├─ main.py           # Main CLI script to run analyses
├─ utils/            # Utility modules: parsing, cleaning, plotting
├─ .gitignore
```

---

## Quickstart

Download raw data from https://www.bikeraceinfo.com:

```bash
python main.py --download-data True --output RAW_DATA_DIR
```

Process raw data:

```bash
python main,py --process-data True --data RAW_DATA_DIR --output DATA_DIR
```

Obtain the statistics. They will be printed in a txt file in the output directory. You can choose the number of cyclists to consider by adding the flag --number-cyclists (the default is 8), and the statistics to print by adding the flag --include (the default is all of them):

```bash
python main.py --statistics True --data DATA_DIR --output OUTPUT_DIR
```

