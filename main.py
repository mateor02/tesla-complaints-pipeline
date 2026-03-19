import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from extractor import models, years, extract
from transformer import transform
from loader import load

# manually call create_tables() separately if not already created
def run_pipeline():
    print("Extracting data...")
    raw = extract(models, years)
    
    print("Transforming data...")
    cleaned = transform(raw)
    
    print("Loading data...")
    loaded = load(cleaned)
    
if __name__ == "__main__":
    run_pipeline()
    