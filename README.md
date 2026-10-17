# Solana Passive Yield Monitor

Open-source CLI tool to track Solana staking yields, JLP (Jupiter Perps LP) value, and basic wallet balances for passive income monitoring.

Built for users with Phantom, Jupiter, and other Solana wallets who want to keep an eye on yields without constant manual checks.

## Features
- Fetch live SOL and JLP prices via Jupiter price API
- Display approximate current APYs for SOL staking (~5-6%) and JLP fee yield (~8%)
- Optional wallet balance check via public Solana RPC
- Simple, no API keys required for basic use
- Easy to extend with more protocols

## Disclaimer
This is not financial advice. Yields are estimates, markets are volatile, and DeFi involves smart contract and price risks. Always DYOR. Rates change. Only risk what you can afford to lose.

## Installation
```bash
git clone https://github.com/Mirmobe/solana-passive-yield-monitor.git
cd solana-passive-yield-monitor
pip install -r requirements.txt
```

## Usage
```bash
python monitor.py --wallet YOUR_SOLANA_ADDRESS
```

Example output:
```
SOL Price: $105.42
JLP Price: $4.56
Estimated SOL Staking APY: 5.5%
Estimated JLP Fee APY: 8.3%
Wallet SOL Balance: 12.45
```

## Monetization & Support
- GitHub Sponsors: Support ongoing development
- Paid support / premium features (private Discord, custom alerts, more protocols)
- Content: Tutorials and analysis threads on X (disclose promotions)
- Bounties: Contributions welcome via issues/PRs

## Contributing
PRs welcome! Ideas: more protocols (Kamino, Marinade), Telegram alerts, historical charts.

## License
MIT
