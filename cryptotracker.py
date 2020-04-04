import utils.parser.parse_json as parser
import utils.analyze.tickerplot as ticker
import os


def main():
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    data = parser.parse(f"{SCRIPT_DIR}/data")

    ticker.crypto_plot(data)


if __name__ == "__main__":
    main()

