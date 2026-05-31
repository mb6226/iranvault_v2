from app.portfolio.portfolio import Portfolio


portfolio = Portfolio(
    initial_balance=100000.0,
    cash_balance=100000.0,
    equity=100000.0,
    exposure=0.0,
    open_positions=0,
)

print(portfolio)
