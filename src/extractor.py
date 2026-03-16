import requests
from validator import Complaint

models = ["MODEL Y", "MODEL 3", "MODEL S", "MODEL X", "CYBERTRUCK", ]
years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
MAKE = "TESLA"

def extract(models: list[str], years: list[str]) -> list[Complaint]:
    complaints = []
    for model in models:
        for year in years:
            try:
                base_url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={MAKE}&model={model}&modelYear={year}"
                r = requests.get(base_url)
                r.raise_for_status()
                data = r.json()
                results = data['results']
                for complaint in results:
                    complaint["model"] = model
                    validated = Complaint.model_validate(complaint)
                    complaints.append(validated)
                
            except requests.RequestException as e:
                print(f"Connection Error: {e}")
    return complaints

if __name__ == "__main__":
    result = extract(models, years)
    print(len(result))        