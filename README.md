# Tesla Complaints Pipeline

An end-to-end ETL data engineering pipeline that extracts, validates, transforms, and loads Tesla vehicle complaint data from the NHTSA (National Highway Traffic Safety Administration) public API into a PostgreSQL database for analysis.

## Project Goal

As Tesla's software and hardware have matured over the years, have complaint volumes and types changed? This project investigates how Tesla vehicle complaints have evolved across models and time — identifying which components fail most frequently, whether safety incidents have increased or decreased, and how complaint patterns differ between Tesla's established models (Model S, X) and newer ones (Model 3, Y, Cybertruck).

The core hypothesis: as Tesla's technology has advanced — particularly with Autopilot, FSD, and over-the-air software updates — complaint patterns should reflect those changes, with older hardware issues giving way to newer software and sensor-related complaints.

## Dataset

- **Source:** [NHTSA Complaints API](https://api.nhtsa.gov/complaints/complaintsByVehicle)
- **Models:** Model Y, Model 3, Model S, Model X, Cybertruck
- **Years:** 2020–2025
- **Records:** ~4,700+ complaint records

## Tech Stack

| Tool | Purpose |
|---|---|
| `Python` | Core pipeline language |
| `requests` | HTTP client for NHTSA API calls |
| `Pydantic` | Data validation and schema enforcement |
| `Polars` | High-performance DataFrame transformations |
| `psycopg2` | PostgreSQL database driver |
| `python-dotenv` | Secure environment variable management |
| `PostgreSQL 15` | Data warehouse |
| `Docker` | Containerized PostgreSQL environment |

## Architecture

```
NHTSA API (raw JSON)
      ↓
  extractor.py      ← fetch complaints across all models & years
      ↓
  validator.py      ← Pydantic validation & schema enforcement
      ↓
  transformer.py    ← Polars cleaning, date parsing, null handling
      ↓
  loader.py         ← psycopg2 bulk insert into PostgreSQL
      ↓
  PostgreSQL DB     ← complaints table ready for analysis
```

## Project Structure

```
tesla-complaints-pipeline/
├── src/
│   ├── db.py           # Database connection module
│   ├── schema.py       # PostgreSQL table definition
│   ├── extractor.py    # NHTSA API data extraction
│   ├── validator.py    # Pydantic complaint model
│   ├── transformer.py  # Polars data cleaning
│   └── loader.py       # PostgreSQL data loading
├── main.py             # Single pipeline entry point
├── docker-compose.yml  # PostgreSQL container config
├── requirements.txt    # Python dependencies
└── .env                # Local credentials (not committed)
```

## Getting Started

### Prerequisites

- Python 3.12+
- Docker Desktop

### Setup

1. Clone the repository:
```bash
git clone https://github.com/mateor02/tesla-complaints-pipeline.git
cd tesla-complaints-pipeline
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=tesla_complaints
DB_USER=your_username
DB_PASSWORD=your_password
```

5. Start the PostgreSQL container:
```bash
docker compose up -d
```

6. Create the database schema:
```bash
python src/schema.py
```

7. Run the full pipeline:
```bash
python main.py
```

## What's Next

- **dbt** — SQL-based analytics transformations on top of raw complaint data (complaint counts by model/year, top failing components, crash rate analysis)
- **NLP Analysis** — spaCy or HuggingFace topic modeling and keyword extraction on complaint narratives to surface recurring themes per model
- **Data Visualization** — Matplotlib/Seaborn charts and a Streamlit dashboard to visualize findings