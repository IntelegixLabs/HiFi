# tests/factories.py
from factory import Factory

from stocks.models import Stocks


class StockFactory(Factory):
    class Meta:
        model = Stocks

    name = "test"
