import pandas as pd

# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

# Return the result table in any order.

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients.loc[patients['conditions'].str.contains(r'\bDIAB1'), ['patient_id', 'patient_name', 'conditions']]
