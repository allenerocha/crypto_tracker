import utils.parser.parse_json as parser
import utils.analyze.tickerplot as ticker

data = parser.parse("/home/allen/PycharmProjects/data_science/crypto_tracker/data")

ticker.crypto_plot(data)

#coins = ["BCHUSD", "DASHUSD", "USDTZUSD", "XETCZUSD", "XETHZUSD", "XXBTZUSD", "XXMRZUSD", "XXRPZUSD", "XZECZUSD"]
#plot_dict = dict()



#for time_key, result in tqdm.tqdm(data.items()):
#    plot_dict[time_key] = {}
#    for coin in coins:
#        try:
#            plot_dict[time_key][coin] = result["result"][coin]["c"][0]
#        except KeyError as e:
#            print(f"Key error {str(e)}")
#            continue

#ordered_plots = collections.OrderedDict(sorted(plot_dict.items()))

#plots = {}

#for coin in coins:
#    try:
#        plots[coin] = {}
#        for key, value in ordered_plots.items():
#            plots[coin][key] = value[coin]
#    except KeyError as e:
#        print(f"Key error {str(e)}")

#for key, value in tqdm.tqdm(plots.items()):
#    times = list(value.keys())
#    ps = list(value.values())
#    prices = [float(p) for p in ps]
#    plt.figure(figsize=(37, 21))
#    plt.scatter(times, prices, label=key, s=2)
#    plt.plot(times, prices, label=key, marker=',')
#    plt.legend()
#    plt.suptitle(f"{key} chart")
#    plt.savefig(f"{key}.png", dpi=300)
#    plt.cla()
#    plt.clf()



if __name__ == "__main__":
    pass

