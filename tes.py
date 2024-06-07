import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Define the column names
column_names = ['', 'capital-gains', 'capital-loss', 'incident_hour_of_the_day', 'number_of_vehicles_involved', 'witnesses', 'total_claim_amount', 'fraud_reported', 'insured_sex_FEMALE', 'insured_sex_MALE', 'insured_occupation_adm-clerical', 'insured_occupation_armed-forces', 'insured_occupation_craft-repair', 'insured_occupation_exec-managerial', 'insured_occupation_farming-fishing', 'insured_occupation_handlers-cleaners', 'insured_occupation_machine-op-inspct', 'insured_occupation_other-service', 'insured_occupation_priv-house-serv', 'insured_occupation_prof-specialty', 'insured_occupation_protective-serv', 'insured_occupation_sales', 'insured_occupation_tech-support', 'insured_occupation_transport-moving', 'insured_hobbies_chess', 'insured_hobbies_cross-fit', 'insured_hobbies_other', 'incident_type_Multi-vehicle Collision', 'incident_type_Parked Car', 'incident_type_Single Vehicle Collision', 'incident_type_Vehicle Theft', 'collision_type_?', 'collision_type_Front Collision', 'collision_type_Rear Collision', 'collision_type_Side Collision', 'incident_severity_Major Damage', 'incident_severity_Minor Damage', 'incident_severity_Total Loss', 'incident_severity_Trivial Damage', 'authorities_contacted_Ambulance', 'authorities_contacted_Fire', 'authorities_contacted_None', 'authorities_contacted_Other', 'authorities_contacted_Police', 'age_group_15-20', 'age_group_21-25', 'age_group_26-30', 'age_group_31-35', 'age_group_36-40', 'age_group_41-45', 'age_group_46-50', 'age_group_51-55', 'age_group_56-60', 'age_group_61-65', 'months_as_customer_groups_0-50', 'months_as_customer_groups_101-150', 'months_as_customer_groups_151-200', 'months_as_customer_groups_201-250', 'months_as_customer_groups_251-300', 'months_as_customer_groups_301-350', 'months_as_customer_groups_351-400', 'months_as_customer_groups_401-450', 'months_as_customer_groups_451-500', 'months_as_customer_groups_51-100', 'policy_annual_premium_groups_high', 'policy_annual_premium_groups_low', 'policy_annual_premium_groups_medium', 'policy_annual_premium_groups_very high', 'policy_annual_premium_groups_very low']

# Step 2: Read the CSV file into a DataFrame
df = pd.read_csv('Asuransi.csv', names=column_names, skiprows=1)  # Skip the first row if it contains header

# Step 3: Display the first few rows
print(df.head())

# Additional exploration (optional)
print(df.describe())
print(df.info())

# Step 4: Visualize the Data
# Example: Bar Plot of total_claim_amount by fraud_reported
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='fraud_reported', y='total_claim_amount')
plt.title('Total Claim Amount by Fraud Reported')
plt.show()

# Example: Histogram of incident_hour_of_the_day
plt.figure(figsize=(10, 6))
sns.histplot(df['incident_hour_of_the_day'], bins=24, kde=True)
plt.title('Distribution of Incident Hour of the Day')
plt.show()

# Example: Scatter Plot using Plotly
fig = px.scatter(df, x='number_of_vehicles_involved', y='total_claim_amount', color='fraud_reported', title='Total Claim Amount vs Number of Vehicles Involved')
fig.show()
