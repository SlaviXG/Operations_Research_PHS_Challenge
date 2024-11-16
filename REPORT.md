# Operational Research Challenge

## Problem Description
### Part One: The central problem we aim to solve is optimizing the allocation and utilization of Accident & Emergency (A&E) services within a defined geographic area. This includes minimizing unnecessary use of A&E services, improving patient flow efficiency, and ensuring that patients receive timely and appropriate care.

# Key Questions to Address
 - How can we reduce unnecessary A&E attendances through reallocation and pre-arrival guidance?
 - What are the optimal resource allocation strategies to minimize waiting times at A&E?
 - Where should additional resources (e.g., MIUs, GP capacity) be allocated geographically to ease pressure on A&E?
 - How do different attendance types (e.g., planned, unplanned, frequent re-attenders) impact A&E demand and resource needs?
 - How can we improve patient understanding of the best facility to visit based on their condition?


## Data Collection
### Since all the data has already been provided already, here is a heatmap created to show the correlation between each data definition. The Correlation is being shown using the Spearman's rank Correlation. [From google - In statistics, Spearman's rank correlation coefficient or Spearman's ρ, named after Charles Spearman and often denoted by the Greek letter or as, is a nonparametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function.]

![Correlation Matrix](output.png)


## Modelling
### To create an equation for minimizing unnecessary A&E attendances through reallocation and pre-arrival guidance, we’ll define a score or index that reflects the necessity for a patient to go to a full Emergency Department (ED) versus a Minor Injury Unit (MIU) or GP. The goal is to route patients to the most appropriate care level based on their condition, distance, wait time, and site availability. This score could guide us in deciding if a patient should be advised to visit an ED or if they can be directed to an alternative healthcare provider.

<p>
Here is a minimizing equation for minimizing unnecessary A&E attendances through reallocation and pre-arrival guidance, we’ll define a score or index that reflects the necessity for a patient to go to a full Emergency Department (ED) versus a Minor Injury Unit (MIU) or GP. The goal is to route patients to the most appropriate care level based on their condition, distance, wait time, and site availability. This score could guide us in deciding if a patient should be advised to visit an ED or if they can be directed to an alternative healthcare provider.
</p>

### Variables
 1. Necessity Score (𝑁) -> Patient Suitability for A&E
 2. Key Factors ->
     a. Patient factors: Attendance_Type, Age_Group, Pat_Loc_GPs
     b. Travel factors: Drive_Distance_Miles, Driving_Time_mins
     c. Site factors: Site_Type, Site_Loc_GPs, Site_X and Site_Y
     d. Wait Time: Wait_Time
3. Objective -> Minimize unnecessary A&E attendances by reassigning non-urgent cases to alternative sites if possible.
4. Weights assigned to each factor -> w1, w2, w3, w4, w5, w6 and w7  

### Formula Structure
### 𝑁 = w1 * Attendance_Type + w2 * f(Age_Group) + w3 * Pat_Loc_GPs + w4 * Drive_Distance_Miles + w5 * Driving_Time_mins + w6 * Wait_Time + w7 Site_Type

Explanation of Each Term
1. Attendance Type (Attendance_Type): Could be binary or categorical. For instance, urgent conditions = 1, minor conditions = 0.5, non-urgent = 0.
2. Age Group f(Age_Group)): Function: f(Age_Group) could assign higher scores for older age brackets. For example:
   f(Age_Group)= if 20-39 then f = 0.5; if 40-59 then f = 1.0; if 80+ then f = 2.0
3. Patient’s Local GPs (Pat_Loc_GPs): Usage => Inverse relation — higher Pat_Loc_GPs should decrease 𝑁. This could be formulated as:
   <br>
   [1 / Pat_Loc_GPs + 1]
   <br>
   to prevent division by zero and ensure it impacts 𝑁 appropriately.
5. Drive Distance and Driving Time to Site (Drive_Distance_Miles and Drive_Time_mins): Combined Term: We could use a weighted average of both. For simplicity:
   Travel_Factor = w4 * Drive_Distance_Miles + w5 * Drive_Time_mins
6. Wait Time at A&E (Wait_Time): Usage: The higher the wait time, the lower the suitability for non-urgent cases. This could be an additive term.
7. Site Type (Site_Tpye): Values: Assign a binary value (1 for full A&E, 0.5 for MIU) to reflect the level of care.

### Final Formula
### 𝑁 = w1 * Attendance_Type + w2 * f(Age_Group) + w3 * ( 1 / Pat_Loc_GPs + 1 ) + Travel_Factor + w6 * Wait_Time + w7 Site_Type
### Where Travel_Factor = w4 * Drive_Distance_Miles + w5 * Drive_Time_mins

- Minimizing 𝑁 indicate cases that are more suitable for alternatives like MIUs or GPs, while higher values indicate a stronger need for A&E services. 
- Decision Threshold: Set a threshold value 𝑁~threshold~. If 𝑁 < 𝑁~threshold~ the patient could be directed to MIUs or GPs instead of A&E.
- Parameter Tuning: The weights can be tuned using historical data and optimization techniques to best capture the factors influencing A&E necessity.

## Potential Scenarios and Adjustments
<p> Overcrowding: If the current wait time is high, increasing w6 (weight for wait time) can amplify the effect of wait times on the model, pushing more non-urgent patients to alternative care. </p>
<p>Long-Distance Patients: For patients further from A&E, we could increase w4 and w5 to make local GP services or MIUs more attractive.</p>
<p>Age and Attendance Type: Adjusting w1 and w2 based on the criticality of certain age groups or attendance types can further refine the model’s sensitivity to patient needs.</p>

This mathematical model provides a quantitative basis for deciding whether to advise a patient to visit an A&E or suggest an alternative. It allows flexibility to adapt weights and test different scenarios, helping minimize unnecessary A&E attendances through guided reallocation. This score-based system can be embedded into a decision-support tool or pre-arrival guidance system that evaluates incoming patient data and suggests the most appropriate care pathway based on current conditions.



