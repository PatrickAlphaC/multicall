import brownie
from brownie import Contract, interface


# Only works for mainnet at the moment
def main():
    price_feed = Contract.from_abi(
        "feed",
        "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
        interface.AggregatorV3Interface.abi,
    )
    rounds = []
    latest_round = price_feed.latestRoundData()[0]
    brownie.multicall(address="0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696")
    with brownie.multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            rounds.append(round_data)
    print(rounds)
