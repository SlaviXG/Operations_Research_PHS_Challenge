import pandas as pd

# File path to the Excel file
filename = "../OR_AE2_Project_Adjusted.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(filename, engine='openpyxl')

# List of columns to analyze
columns_to_analyze = [
    'Site_Code', 'Site_Type', 'Site_Loc_GPs', 'Site_Loc_GP_List', 
    'Pat_Loc_GPs', 'Pat_Loc_GP_List', 'Drive_Distance_Miles', 
    'Driving_Time_mins', 'Attendance_Type', 'Age_Group', 
    'Wait_Time', 'Year', 'Month', 'Number_Of_Attendances'
]

# Open a file to save the output
with open("summary.txt", "w") as summary_file:
    # Loop over Site_Code from 1 to 11
    for site_code in range(1, 12):
        summary_file.write(f"\nAnalyzing data for Site {site_code}:\n\n")

        # Filter data where Site_Code matches the current site_code
        site_df = df[df['Site_Code'] == site_code]

        for column in columns_to_analyze:
            if column in site_df.columns:
                summary_file.write(f"Analysis of '{column}' for Site {site_code}:\n")

                # Perform value counts to summarize the data in the column
                column_counts = site_df[column].value_counts()

                # Write the results to the file
                for value, count in column_counts.items():
                    summary_file.write(f"{value}: {count}\n")
                
                summary_file.write("\n")  # Add a blank line for readability
            else:
                summary_file.write(f"Column '{column}' not found in the dataset.\n\n")

print("Analysis completed. Data has been saved to 'summary.txt'.")
