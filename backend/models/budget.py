from pydantic import BaseModel


class BudgetBreakdown(BaseModel):
    fuel: float
    food: float
    accommodation: float
    total: float
    budget: float
    remaining: float
    within_budget: bool