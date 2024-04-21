from pydantic import BaseModel


class userProfileAdditionalDataSchema(BaseModel):
    salary: int
    no_of_dependents: int
    medical_insurance_cover: int
    term_insurance_cover: int
    disabilities: bool
    liabilities_amount: int
    stocks_mutual_funds_investment: int
    fixed_deposit: int
