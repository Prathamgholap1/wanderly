from pydantic import BaseModel, Field
from typing import Optional


class TripRequest(BaseModel):
    destination: Optional[str] = Field(
        default=None,
        description="Travel destination"
    )

    duration_days: Optional[int] = Field(
        default=None,
        description="Number of days for the trip"
    )

    budget: Optional[float] = Field(
        default=None,
        description="Maximum trip budget in Indian rupees as a plain number"
    )

    number_of_people: Optional[int] = Field(
        default=None,
        description="Number of travelers"
    )

    starting_location: Optional[str] = Field(
        default=None,
        description="Location where the trip starts"
    )

    interests: list[str] = Field(
        default_factory=list,
        description="User's travel interests"
    )

    transport: Optional[str] = Field(
        default=None,
        description="Preferred mode of transportation"
    )