import matplotlib.pyplot as plt
import collections
import tqdm
import time
import numpy as np


def crypto_plot(data: dict):
    coins = ["BCHUSD", "DASHUSD", "USDTZUSD", "XETCZUSD", "XETHZUSD", "XXBTZUSD", "XXMRZUSD", "XXRPZUSD", "XZECZUSD"]
    plot_dict = dict()
    key_errors = 0

    for time_key, result in tqdm.tqdm(data.items()):
        plot_dict[time_key] = {}
        for coin in coins:
            try:
                plot_dict[time_key][coin] = result["result"][coin]["c"][0]
            except KeyError as e:
                key_errors += 1
                continue
    print(f"{key_errors} key errors")
    ordered_plots = collections.OrderedDict(sorted(plot_dict.items()))

    plots = {}

    key_errors = 0
    for coin in tqdm.tqdm(coins):
        try:
            plots[coin] = {}
            for key, value in ordered_plots.items():
                plots[coin][key] = value[coin]
        except KeyError as e:
            key_errors += 1
            continue
    print(f"{key_errors} key errors")

    for key, value in tqdm.tqdm(plots.items()):
        start_time = time.time()
        print(f"Generating plot for {coin}...")
        times = list(value.keys())
        ps = list(value.values())
        prices = [float(p) for p in ps]
        plt.figure(figsize=(37, 21))
        plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
        plt.scatter(times, prices, label=key, s=3)
        plt.plot(times, prices, label=key, marker=',')
        plt.legend()
        plt.suptitle(f"{key} chart")
        plt.savefig(f"{key}.png", dpi=300)
        plt.cla()
        plt.clf()
        print(f"Plot for {coin} has been successfully generated in {time.time() - start_time} seconds!")


