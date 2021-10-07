# MultiCall Examples

We make multiple calls via a single API call to our infura node. 

## Prerequisites

1. Please go through the [brownie install documenation](https://eth-brownie.readthedocs.io/en/stable/install.html)
2. Please have an environment varibale called `WEB3_INFURA_PROJECT_ID` set to your [infura project id](https://infura.io/). You can add it to a `.env` file and add `dotenv: .env` to the `brownie-config.yaml` file. 

# Simple Example

```bash
brownie run scripts/multicall.py
```

# Advanced Example

```bash
brownie run scripts/multicall-advanced.py
```
