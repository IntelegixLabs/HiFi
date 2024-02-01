from beanie import Document


class Stocks(Document):
    name: str

    class Settings:
        name = "stocks"