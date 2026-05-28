#!/usr/bin/env python3
import json, urllib.request, statistics
coins=["bitcoin","ethereum","solana"]
for c in coins:
    url=f"https://api.coingecko.com/api/v3/coins/{c}/market_chart?vs_currency=usd&days=7"
    try:
        data=json.load(urllib.request.urlopen(url, timeout=20))
        prices=[p[1] for p in data.get("prices", [])]
        rets=[(prices[i]/prices[i-1]-1)*100 for i in range(1,len(prices)) if prices[i-1]]
        print(c, "price", round(prices[-1],2), "vol_7d_pct", round(statistics.pstdev(rets),3), "move_7d_pct", round((prices[-1]/prices[0]-1)*100,2))
    except Exception as e:
        print(c, "error", e)
