from app.domain.trade_plan import TradePlan


plan = TradePlan(
    symbol="BTCUSD",
    side="BUY",
    entry_price=100000,
    stop_loss=98000,
    take_profit=106000,
    risk_percent=1.0,
    position_size=0.5,
)

print(plan)
