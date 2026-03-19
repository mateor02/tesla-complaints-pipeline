from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
from datetime import date

class Complaint(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    odi_number: int
    model: str 
    date_of_incident: str
    date_complaint_filed: str
    components: str | None = None
    summary: str | None = None
    crash: bool
    fire: bool
    number_of_injuries: int | None = None
    number_of_deaths: int | None = None