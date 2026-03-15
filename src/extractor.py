import requests

models = ["MODEL Y", "MODEL 3", "MODEL S", "MODEL X"]
years = ["2020", "2021", "2022", "2023", "2024", "2025"]

def extract():
    complaints = []
    for model in models:
        for year in years:
            try:
                base_url = f"https://api.nhtsa.gov/complaints/complaintsByVehicle?make={"TESLA"}&model={model}&modelYear={year}"
                r = requests.get(base_url)
                r.raise_for_status()
                data = r.json()
                results = data['results']
                complaints.extend(results)
                
            except requests.RequestException as e:
                print(f"Connection Error: {e}")
    return complaints

if __name__ == "__main__":
    result = extract()
    print(len(result))        