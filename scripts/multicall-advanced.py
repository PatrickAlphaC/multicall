import brownie
from brownie import Contract, interface, config, network
import matplotlib.pyplot as plt
from datetime import datetime

# pipx inject eth-brownie matplotlib


def main():
    price_feed = Contract.from_abi(
        "feed",
        config["networks"][network.show_active()]["eth_usd"],
        interface.AggregatorV3Interface.abi,
    )
    latest_round = price_feed.latestRoundData()[0]
    decimals = price_feed.decimals()

    round_ids = []
    answers = []
    time_stamps = []
    brownie.multicall(address=config["networks"][network.show_active()]["multicall2"])
    with brownie.multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            round_ids.append(round_data[0])
            answers.append(round_data[1] / 10 ** decimals)
            time_stamps.append(datetime.fromtimestamp(round_data[3]))
    plt.plot(time_stamps, answers)
    plt.show()
