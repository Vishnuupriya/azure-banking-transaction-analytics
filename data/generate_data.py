import random
from pathlib import Path
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent
fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# 1. Generate Branches
# -----------------------------
branches = []

cities = [
    ("Chennai", "Tamil Nadu"),
    ("Bangalore", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Kochi", "Kerala"),
    ("Coimbatore", "Tamil Nadu"),
]

for i in range(1, 21):
    city, state = random.choice(cities)

    branches.append({
        "branch_id": f"B{i:03d}",
        "branch_name": f"{city} Branch {i}",
        "city": city,
        "state": state
    })

branches_df = pd.DataFrame(branches)


# -----------------------------
# 2. Generate Customers
# -----------------------------
customers = []

for i in range(1, 1001):
    city, state = random.choice(cities)

    registration_date = fake.date_between(
        start_date="-3y",
        end_date="-30d"
    )

    customers.append({
        "customer_id": f"C{i:04d}",
        "name": fake.name(),
        "city": city,
        "state": state,
        "registration_date": registration_date
    })

customers_df = pd.DataFrame(customers)


# -----------------------------
# 3. Generate Accounts
# -----------------------------
accounts = []

for i in range(1, 1201):
    customer = random.choice(customers)

    opening_date = fake.date_between(
        start_date="-3y",
        end_date="-15d"
    )

    accounts.append({
        "account_id": f"A{i:05d}",
        "customer_id": customer["customer_id"],
        "account_type": random.choice(["Savings", "Current"]),
        "opening_date": opening_date,
        "balance": round(random.uniform(5000, 500000), 2)
    })

accounts_df = pd.DataFrame(accounts)


# -----------------------------
# 4. Generate Transactions
# -----------------------------
transactions = []

transaction_types = ["Credit", "Debit"]
channels = ["UPI", "ATM", "NEFT", "IMPS", "Online", "Branch"]

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 9, 30)

date_range = (end_date - start_date).days

for i in range(1, 10001):

    account = random.choice(accounts)

    transaction_date = (
        start_date + timedelta(days=random.randint(0, date_range))
    ).date()

    transaction_type = random.choice(transaction_types)

    # Mostly normal transactions
    amount = round(random.uniform(500, 50000), 2)

    # Create some large transactions for anomaly detection later
    if random.random() < 0.01:
        amount = round(random.uniform(100000, 500000), 2)

    transactions.append({
        "transaction_id": f"T{i:06d}",
        "account_id": account["account_id"],
        "transaction_date": transaction_date,
        "transaction_type": transaction_type,
        "amount": amount,
        "channel": random.choice(channels)
    })

transactions_df = pd.DataFrame(transactions)


# -----------------------------
# 5. Save CSV files
# -----------------------------

branches_df.to_csv(OUTPUT_DIR / "branches.csv", index=False)
customers_df.to_csv(OUTPUT_DIR / "customers.csv", index=False)
accounts_df.to_csv(OUTPUT_DIR / "accounts.csv", index=False)
transactions_df.to_csv(OUTPUT_DIR / "transactions.csv", index=False)

print("Synthetic banking data generated successfully!")
print()
print(f"Branches      : {len(branches_df)}")
print(f"Customers     : {len(customers_df)}")
print(f"Accounts      : {len(accounts_df)}")
print(f"Transactions  : {len(transactions_df)}")