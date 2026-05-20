# IBKR Paper Trading App

A Python starter project for experimenting with Interactive Brokers paper-trading workflows. The app is designed for learning order placement, market data access, and automated trading logic without using real capital.

## Features

- Connects to Interactive Brokers TWS or IB Gateway.
- Supports paper-trading workflows for strategy testing.
- Provides a small Python entry point for extending trading logic.
- Keeps dependencies minimal through `requirements.txt`.

## Tech Stack

- Python
- Interactive Brokers API
- `ib_insync` / `ibapi`

## Prerequisites

- Interactive Brokers account with paper trading enabled.
- TWS or IB Gateway installed and running.
- Python 3.10 or newer.

## Run Locally

```bash
git clone https://github.com/mudassirabbasi1/ibkr-paper-trading-app.git
cd ibkr-paper-trading-app
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Disclaimer

This project is for education and paper-trading experiments only. It is not financial advice and should not be used for live trading without proper testing, risk controls, and review.
