#!/usr/bin/env python3
"""
Solana Passive Yield Monitor
Fetches live prices and shows estimated yields for staking and JLP.
"""

import argparse
import requests
import json
from datetime import datetime

# Public endpoints
JUPITER_PRICE_URL = "https://api.jup.ag/price/v2"
SOL_MINT = "So11111111111111111111111111111111111111112"
JLP_MINT = "27G8MtK7VtTcCHkpASjSDdkWWYfoqT6ggEuKidVJidD4"
PUBLIC_RPC = "https://api.mainnet-beta.solana.com"

# Approximate APYs (update periodically; not live)
SOL_STAKING_APY = 5.5  # %
JLP_FEE_APY = 8.3     # % from recent Jupiter data

def fetch_prices():
    ids = f"{SOL_MINT},{JLP_MINT}"
    try:
        resp = requests.get(f"{JUPITER_PRICE_URL}?ids={ids}", timeout=10)
        resp.raise_for_status()
        data = resp.json().get("data", {})
        sol_price = data.get(SOL_MINT, {}).get("price", 0)
        jlp_price = data.get(JLP_MINT, {}).get("price", 0)
        return float(sol_price), float(jlp_price)
    except Exception as e:
        print(f"Price fetch error: {e}")
        return 0.0, 0.0

def get_sol_balance(wallet: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet]
    }
    try:
        resp = requests.post(PUBLIC_RPC, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json().get("result", {})
        lamports = result.get("value", 0)
        return lamports / 1_000_000_000
    except Exception as e:
        print(f"Balance fetch error: {e}")
        return 0.0

def main():
    parser = argparse.ArgumentParser(description="Solana Passive Yield Monitor")
    parser.add_argument("--wallet", type=str, help="Solana wallet address to check balance")
    args = parser.parse_args()

    print(f"=== Solana Passive Yield Monitor ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ===\n")

    sol_price, jlp_price = fetch_prices()
    print(f"SOL Price: ${sol_price:.2f}")
    print(f"JLP Price: ${jlp_price:.4f}")
    print(f"Estimated SOL Staking APY: {SOL_STAKING_APY}%")
    print(f"Estimated JLP Fee APY: {JLP_FEE_APY}%")

    if args.wallet:
        balance = get_sol_balance(args.wallet)
        print(f"Wallet SOL Balance: {balance:.4f} SOL (~${balance * sol_price:.2f})")

    print("\nNote: APYs are approximate and for educational purposes only. Not financial advice.")

if __name__ == "__main__":
    main()
