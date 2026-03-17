import polars as pl
from validator import Complaint
from extractor import extract, models, years
def transform(complaints: list[Complaint]):
    complaints = [complaint.model_dump() for complaint in complaints]
    complaints_df = pl.DataFrame(complaints)
    complaints_df = complaints_df.with_columns(pl.col("date_of_incident").str.to_date(format="%m/%d/%Y"),
                                               pl.col("date_complaint_filed").str.to_date(format="%m/%d/%Y"))
    complaints_df = complaints_df.with_columns(pl.col("components").fill_null("Unknown"),
                                               pl.col("summary").fill_null("Unknown"),
                                               pl.col("number_of_injuries").fill_null(0),
                                               pl.col("number_of_deaths").fill_null(0))
    return complaints_df
    
if __name__ == "__main__":
    extract_df = extract(models, years)
    print(transform(extract_df))