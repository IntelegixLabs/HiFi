from tests.factories.stock_factories import StockFactory


def test_stocks(client, mock_mongodb_connection, mock_db):
    stock = StockFactory()
    assert stock.name == "test"
