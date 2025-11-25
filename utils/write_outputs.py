from pathlib import Path
import utils.statistics as stats


def write_stats_1(df, number_cyclists):
    df_sorted = df.sort_values(by="size", ascending=False).reset_index(drop=True)
    result = ""
    for i in range(number_cyclists):
        result += (df_sorted.loc[i, "rider"] + ": " + str(df_sorted.loc[i, "size"]) + "\n")
    return result


def write_outputs(inputpath, outputpath, include, number_cyclists=8):
    inputpath = Path(inputpath)
    outputpath = Path(outputpath)

    result = ""

    if "most_podiums" in set(include):
        result += f"{number_cyclists} cyclists with most podiums in Amstel Gold Race, Tour of Flanders, La Flèche Wallonne, Gent-Wevelgem, Giro d'Italia, Liège Bastogne Liège, Giro di Lombardia, Milano Sanremo, Paris-Roubaix, Tour de France, Vuelta a España, World Championship Road Race\n"
        podiums = stats.most_podiums(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_podiums_gt" in set(include):
        result += f"{number_cyclists} cyclists with most podiums Grand Tours\n"
        podiums = stats.most_podiums_gt(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_podiums_monuments" in set(include):
        result += f"{number_cyclists} cyclists with most podiums in cycling Monuments\n"
        podiums = stats.most_podiums_monuments(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"
    
    if "most_podiums_monuments_wc" in set(include):
        result += f"{number_cyclists} cyclists with most podiums in cycling Monuments and Wolrd Championship Road Race\n"
        podiums = stats.most_podiums_monuments_wc(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_podiums_monuments_wc_gt" in set(include):
        result += f"{number_cyclists} cyclists with most podiums in cycling Monuments, Wolrd Championship Road Race and Grand Tours\n"
        podiums = stats.most_podiums_monuments_wc_gt(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_wins" in set(include):
        result += f"{number_cyclists} cyclists with most wins in Amstel Gold Race, Tour of Flanders, La Flèche Wallonne, Gent-Wevelgem, Giro d'Italia, Liège Bastogne Liège, Giro di Lombardia, Milano Sanremo, Paris-Roubaix, Tour de France, Vuelta a España, World Championship Road Race\n"
        podiums = stats.most_wins(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_wins_gt" in set(include):
        result += f"{number_cyclists} cyclists with most wins Grand Tours\n"
        podiums = stats.most_wins_gt(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_wins_monuments" in set(include):
        result += f"{number_cyclists} cyclists with most wins in cycling Monuments\n"
        podiums = stats.most_wins_monuments(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"
    
    if "most_wins_monuments_wc" in set(include):
        result += f"{number_cyclists} cyclists with most wins in cycling Monuments and Wolrd Championship Road Race\n"
        podiums = stats.most_wins_monuments_wc(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"

    if "most_wins_monuments_wc_gt" in set(include):
        result += f"{number_cyclists} cyclists with most wins in cycling Monuments, Wolrd Championship Road Race and Grand Tours\n"
        podiums = stats.most_wins_monuments_wc_gt(inputpath)
        result += write_stats_1(podiums, number_cyclists)
        result += "\n"


    with open(outputpath / "statistics.txt", "w") as f:
        f.write(result)