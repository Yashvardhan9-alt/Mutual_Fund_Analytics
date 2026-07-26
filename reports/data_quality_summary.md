# Data Quality Summary (Day 1)

1. All 10 CSV datasets were successfully loaded without any file read errors.

2. The `fund_master` and `nav_history` datasets were explored and AMFI scheme codes were validated.

3. Live NAV data was successfully fetched from the MFAPI and saved as CSV files in the `dataset/raw` folder.

4. During API validation, some AMFI codes provided in the project document returned different scheme names from the current MFAPI response. This indicates that the API mapping may have changed over time or the project document contains older scheme references.

5. No issues were found in loading the datasets. The observed discrepancy was related only to the current API mapping.