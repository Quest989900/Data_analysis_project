import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# 1. Base Setup for Nigeria's States
states_clean = [
    "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", 
    "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT", "Gombe", 
    "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", 
    "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", 
    "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
]

# ----------------------------------------------------
# TABLE 1: STATE DEMOGRAPHICS (Demographics.csv)
# ----------------------------------------------------
# Introduce intentional spelling anomalies to force ETL cleaning
demographic_states = states_clean.copy()
demographic_states[demographic_states.index("FCT")] = "Abuja (FCT)"
demographic_states[demographic_states.index("Cross River")] = "Cross-River"
demographic_states[demographic_states.index("Kano")] = "Kanoo"
demographic_states[demographic_states.index("Ogun")] = "Ogun " # Trailing space

populations = np.random.randint(2000000, 15000000, size=len(states_clean))
# Give Lagos and Kano realistic higher populations
for i, state in enumerate(states_clean):
    if state == "Lagos": populations[i] = 16000000
    if state == "Kano": populations[i] = 14000000

df_demographics = pd.DataFrame({
    "State Name": demographic_states,
    "Population": populations,
    "Growth Rate (%)": np.round(np.random.uniform(2.1, 3.8, size=len(states_clean)), 2),
    "GDP per Capita (USD)": np.random.randint(800, 4500, size=len(states_clean))
})

# ----------------------------------------------------
# TABLE 2: HEALTHCARE INFRASTRUCTURE (Infrastructure.csv)
# ----------------------------------------------------
# Create multiple facilities per state
facility_records = []
facility_id_counter = 1001

# Introduce variation in state naming variants again
infra_states_pool = states_clean.copy()
infra_states_pool[infra_states_pool.index("FCT")] = "FCT"
infra_states_pool[infra_states_pool.index("Cross River")] = "Cross River"

for state in infra_states_pool:
    num_facilities = np.random.randint(5, 20) # 5 to 20 facilities per state
    for _ in range(num_facilities):
        fac_type = np.random.choice(["Primary", "Secondary", "Tertiary"], p=[0.7, 0.2, 0.1])
        ownership = np.random.choice(["Public", "Private"], p=[0.6, 0.4])
        
        # Base operational beds on facility type
        if fac_type == "Primary":
            beds = np.random.randint(5, 25)
        elif fac_type == "Secondary":
            beds = np.random.randint(30, 120)
        else:
            beds = np.random.randint(150, 500)
            
        # Introduce purposeful structural missingness (Nulls) for students to handle
        if np.random.rand() < 0.12: # 12% missing data
            beds = np.nan
            
        power_reliability = np.random.randint(2, 24)
        
        facility_records.append({
            "Facility ID": f"FAC-{facility_id_counter}",
            "State": state,
            "Facility Type": fac_type,
            "Ownership": ownership.upper() if np.random.rand() > 0.5 else ownership.lower(), # Messy casing
            "Operational Beds": beds,
            "Power Supply Reliability (Hours/Day)": power_reliability
        })
        facility_id_counter += 1

df_infrastructure = pd.DataFrame(facility_records)

# ----------------------------------------------------
# TABLE 3: EPIDEMIC INCIDENCE (Disease_Incidence.csv)
# ----------------------------------------------------
# Tracking 3 major diseases across 3 years
disease_records = []
record_id_counter = 50001

disease_states_pool = states_clean.copy()
# Another slight variation pattern for mapping failures
disease_states_pool[disease_states_pool.index("FCT")] = "Abuja"

for state in disease_states_pool:
    for year in [2024, 2025, 2026]:
        for disease in ["Malaria", "Lassa Fever", "Cholera"]:
            # Differentiate baseline counts based on disease threat profile
            if disease == "Malaria":
                cases = np.random.randint(5000, 75000)
                mortality_rate = np.random.uniform(0.005, 0.02) # Low mortality, high volume
            elif disease == "Lassa Fever":
                cases = np.random.randint(10, 450)
                mortality_rate = np.random.uniform(0.12, 0.25) # High mortality, low volume
            else: # Cholera
                cases = np.random.randint(50, 3000)
                mortality_rate = np.random.uniform(0.03, 0.08)
                
            disease_records.append({
                "Record ID": record_id_counter,
                "State": state,
                "Year": year,
                "Disease Category": disease,
                "Reported Cases": cases,
                "Mortality Rate": np.round(mortality_rate, 4)
            })
            record_id_counter += 1

df_disease = pd.DataFrame(disease_records)

# ----------------------------------------------------
# EXPORT TO CSV
# ----------------------------------------------------
df_demographics.to_csv("Demographics.csv", index=False)
df_infrastructure.to_csv("Infrastructure.csv", index=False)
df_disease.to_csv("Disease_Incidence.csv", index=False)

print("Successfully generated project datasets:")
print(" -> Demographics.csv (37 rows)")
print(f" -> Infrastructure.csv ({len(df_infrastructure)} rows with intentional NaNs)")
print(f" -> Disease_Incidence.csv ({len(df_disease)} rows spanning 2024-2026)")
