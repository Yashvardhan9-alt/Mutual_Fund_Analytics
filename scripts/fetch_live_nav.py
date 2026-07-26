import requests
import pandas as pd
from pathlib import Path

# Folder to save CSV files
save_path = Path("dataset/raw")

# AMFI Scheme Codes
schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("\n" + "=" * 60)
        print("Scheme :", data["meta"]["scheme_name"])
        print("Fund House :", data["meta"]["fund_house"])

        nav_df = pd.DataFrame(data["data"])

        file_name = save_path / f"{scheme_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"✅ Saved -> {file_name}")

    else:

        print(f"❌ Failed for {scheme_name}")
        