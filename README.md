# MultiCall Examples

We make multiple calls via a single API call to our infura node. 

## Prerequisites

1. Please go through the [brownie install documenation](https://eth-brownie.readthedocs.io/en/stable/install.html)
2. Please have an environment varibale called `WEB3_INFURA_PROJECT_ID` set to your [infura project id](https://infura.io/). You can add it to a `.env` file and add `dotenv: .env` to the `brownie-config.yaml` file. 

## Quickstart

```
git clone https://github.com/PatrickAlphaC/multicall
cd multicall
```

# Simple Example

```bash
brownie run scripts/multicall.py
```

# Plotting Example

If you installed brownie with pipx, inject `matplotlib` into the environment. Otherwise, just run `pip install matplotlib`.

```
pipx inject eth-brownie matplotlib
```

*restart terminal*

```bash
brownie run scripts/multicall_plot.py
```
