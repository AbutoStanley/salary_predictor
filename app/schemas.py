from pydantic import BaseModel, Field
from typing import Literal

class SalaryRequest(BaseModel):
    work_year: int = Field(ge=2020, le=2025)
    experience_level: Literal["EN", "MI", "SE", "EX"]
    employment_type: Literal["FT", "PT", "CT", "FL"]
    remote_ratio: int = Field(ge=0, le=100)
    company_size: Literal["S", "M", "L"]
    residence_grouped: str