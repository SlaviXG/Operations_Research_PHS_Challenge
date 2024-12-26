"""
This Python script processes and condenses data from an Excel file named 'OR_AE2_Project_Adjusted.xlsx'.
The script performs a series of analyses on different segments of data for each site (from Site_Code 1 to 11), 
extracting insights about patient attendance, resource availability, and geographic/demographic factors. 

It achieves the following:
1. **Patient Demand Analysis:**
   - Number of patients in each attendance category.
   - Distribution of wait times in 30-minute groups.
   - Types of attendance for each site.

2. **Resource Availability:**
   - Number of GPs in the postcode area of the site.
   - Number of patients listed for GPs in the postcode area of the site.
   - Type of the site.

3. **Geographic and Demographic Factors:**
   - Driving time (in minutes) to the site.
   - Population within 20 miles of the site.

The script prints the results for each site, providing a condensed overview of key data points for better decision-making and analysis.

"""
import pandas as pd

filename = "./OR_AE2_Project_Adjusted.xlsx"
# Read the Excel file into a DataFrame
df = pd.read_excel(filename, engine='openpyxl')

# Loop over Site_Code from 1 to 11
for site_code in range(1, 12):
    # Filter data where Site_Code matches the current site_code
    site_df = df[df['Site_Code'] == site_code]
    
    print("Load Function First Segment: Demand on the A&E Site")
    # Number of Attendances for each category
    number_of_attendance_counts = site_df['Number_Of_Attendances'].value_counts()
    print("Number of patients in each category")
    print(f"Site {site_code}:")

    for number_of_attendance, count in number_of_attendance_counts.items():
        print(f"{number_of_attendance} ")
    
    print()
    
    # wait_time
    wait_time_count = site_df['Wait_Time'].value_counts()
    print("The group of wait time in 30 minutes groups")
    print(f"Site {site_code}:")

    for wait_time, count in wait_time_count.items():
        print(f"{wait_time} ")

    print() 
    
    # Attendance Type
    attendance_type_count = site_df['Attendance_Type'].value_counts()
    print("Type of Attendance")
    print(f"Site {site_code}")

    for attendance_type, count in attendance_type_count.items():
        print(f"{attendance_type}")

    print()
############################################################################
    print("Load function Second Segment: Resource Availability")
    # Site_loc_Gps
    site_loc_gp_count = site_df['Site_Loc_GPs'].value_counts()
    print("No of GPs within the postcode area of the site")
    print(f"Site {site_code}:")

    for site_loc_gp, count in site_loc_gp_count.items():
        print(f"{site_loc_gp} ")

    print()
    

    # Pat_loc_GPs
    site_loc_gp_list_count = site_df['Site_Loc_GP_List'].value_counts()
    print("No of patients listed for the GPs in the postcode area of the site")
    print(f"Site {site_code}:")

    for site_loc_gp_list, count in site_loc_gp_list_count.items():
        print(f"{site_loc_gp_list} ")

    print()

    # site_type
    site_type_count = site_df['Site_Type'].value_counts()
    print("Site Type")
    print(f"Site {site_code}:")

    for site_type, count in site_type_count.items():
        print(f"{site_type} ")

    print()
############################################################################
    print("Load Function Third Segment: Geographic and Demographic Factors")
    # Drive_time
    drive_time_count = site_df['Driving_Time_mins'].value_counts()
    print("Driving Time in mins")
    print(f"Site {site_code}:")

    for drive_time, count in drive_time_count.items():
        print(f"{drive_time} ")

    print() 

    # Site_Pop_20miles
    site_pop_twenty_miles_count = site_df['Site_Pop_20miles'].value_counts()
    print("Population within 20 miles of the site")
    print(f"Site {site_code}:")

    for site_pop_twenty_miles, count in site_pop_twenty_miles_count.items():
        print(f"{site_pop_twenty_miles} ")

    print() 



    
    

