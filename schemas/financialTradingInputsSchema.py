from pydantic import BaseModel


class financialTradingInputsSchema(BaseModel):
    stock_selection: str
    initial_capital: str
    risk_tolerance: str
    trading_strategy_preference: str
    news_impact_consideration: bool
