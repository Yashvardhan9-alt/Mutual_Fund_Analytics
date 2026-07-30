# Mutual Fund Analytics - Data Dictionary

## Project Overview

This document describes the datasets, tables, and columns used in the Mutual Fund Analytics project.

---

# 1. fact_nav

Stores daily Net Asset Value (NAV) of mutual fund schemes.

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

# 2. fact_transactions

Stores investor transaction details.

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | Integer | Unique Investor ID |
| transaction_date | Date | Date of Transaction |
| amfi_code | Integer | Mutual Fund Scheme Code |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| payment_mode | Text | Payment Method |
| kyc_status | Text | Investor KYC Status |

---

# 3. fact_performance

Stores mutual fund performance metrics.

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Scheme Code |
| return_1yr_pct | Float | One Year Return (%) |
| return_3yr_pct | Float | Three Year Return (%) |
| return_5yr_pct | Float | Five Year Return (%) |
| benchmark_3yr_pct | Float | Benchmark Return |
| alpha | Float | Alpha Ratio |
| beta | Float | Beta Ratio |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annual Standard Deviation |
| max_drawdown_pct | Float | Maximum Drawdown |
| aum_crore | Float | Assets Under Management (Crores) |
| expense_ratio_pct | Float | Expense Ratio (%) |
| anomaly_flag | Boolean | Data Validation Flag |

---

# Data Cleaning Summary

## NAV History

- Converted dates to datetime
- Sorted by AMFI Code and Date
- Forward-filled missing NAV values
- Removed duplicate records
- Validated NAV > 0

---

## Investor Transactions

- Standardized transaction types
- Converted transaction dates
- Removed duplicates
- Validated transaction amount
- Checked KYC status values

---

## Scheme Performance

- Converted return columns to numeric
- Validated expense ratio
- Flagged anomalies
- Removed duplicate records

---

# Database

SQLite Database

Tables:

- fact_nav
- fact_transactions
- fact_performance

---

Prepared for Bluestock Data Analyst Internship