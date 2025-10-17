from ib_insync import *
import pandas as pd

# --- IBKR Connection ---
ib = IB()

try:
    # Connect to Trader Workstation (TWS)
    ib.connect('127.0.0.1', 7497, clientId=1)
    print("✅ Connected to IBKR TWS")

    # --- Step 1: Define a Contract (e.g., Apple Stock) ---
    contract = Stock('AAPL', 'SMART', 'USD')

    # --- Step 2: Request Market Data ---
    ticker = ib.reqMktData(contract)
    ib.sleep(2)  # Wait a moment for data
    print(f"📊 Market Data for {contract.symbol}: Bid={ticker.bid}, Ask={ticker.ask}, Last={ticker.last}")

    # --- Step 3: Place a Paper Trade ---
    order = MarketOrder('BUY', 10)  # Buy 10 shares
    trade = ib.placeOrder(contract, order)
    print("📝 Order placed:", trade)

    # --- Step 4: Wait for order updates ---
    ib.sleep(3)
    print("📋 Trade status:", trade.orderStatus.status)

except Exception as e:
    print("❌ Error:", e)

finally:
    ib.disconnect()
    print("🔌 Disconnected from IBKR")
