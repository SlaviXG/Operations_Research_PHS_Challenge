# Operational Research Challenge

## Problem Formulation 
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

## Objective:
### Optimize patient flow and resource allocation in A&E departments under the worst-case scenario: all patients are unplanned, requiring immediate attention.

## Mathematical Modelling - Hybrid Queuing + Loading Function for Dynamic Flow. 
### Queuing Theory for Grouped Patients
To simplify the complexity, patient categories are grouped and modeled.
 - MIU/Other:
    - Treated as First Come First Serve (FCFS) for low-acuity cases.
    - Simplified queue for predicting wait times and optimizing resource allocation (eg. triage nurses, rooms)
    - Goal: Minimize the wait times for minor injuries, avoiding bottlenecks
 - ED (Emergency Department):
    - Modeled as Priority Queuing System for high-acuity cases.
    - Cases with priority:
       - High-priority cases bypass queues.
       - Low-priority cases wait until resources are free.
    - Goal: Minimize delays for critical patients while balancing fairness.
      
### Loading function for System-Wide Balance
 - Incorporate real-time data  to compute site load scores:
    - Load Score = (Beds Occupied / Site Capacity) + Travel Time + Patient Wait Time
       1. Current Patients: The number of patients currently being treated or waiting at the site.
       2. Site Capacity: The maximum number of patients the site can handle effectively at a given time.(based on available staff, rooms, and resources)
       3. Travel Time: Time it takes for a patient to reach the site (based on location).
       4. Patient Wait Time: Current average wait time for patients at the site.
    - Adjust routing to ditribute patients evenly across sites.
    - Goal: Prevent site oberload by re-routing non-urgent cases to less crowded sites.  
      
### Performance Measures - Efficiency and Fairness
Wait Times
 - Use queuing metrics (eg. average wait time Wq) to measure performance:
    - MIU/Other: Evaluate average wait time for all patients.
    - ED: Measure critical patient delay and overall system throughput
 - Effective re-allocation
    - Track patient distribution to avoid overburdening any single facility.
    - Optimize allocation dynamically by minimizing the standard deviation of load scores across sites:
       - Metric = Minimize Load Variability.
         
## Alternative Courses of Action: Leverage an Airport + Casino Hybrid to streamline patient flow
### An Airport-Inspired Attendance Managemnet System
 - Segementation and Pre-Sorting
     - Similar to how passengers are assigned to terminals and gates, patients are sorted pre-arrival based on:
        - Symptom severity
        - Wait times and Site capacity
        - Location and travel distance
     - Re-Routing:
        - Just as Airports manage over-crowding by re-directing passengers, patients are guided to nearby MIUs or GP to reduce A&E congestion.

### casino Psychology for Behavioural Guidance
 - Use visual cues and choice framing to direct patient flow to optimal options:
    - Subtly encourage non-critical patients to select MIU/Other with prompts such as:
       - "Receive care faster at our MIU, specialized for cases like yours"
    - Real-time updates provide transparency, building trust in the system.

### Event-Driven Process Chains (EPC) and State Tables
 - Document the flow of patients through the system using EPCs or state tables to:
    - Identify ineffeciencies and decision points.
    - Clearly define transitions, eg:
       - Patient Arrival -> Triage -> Department Assignment -> Treatment -> Exit.
 - Incorporate automation triggers, eg: re-routing based on load scores.
<hr>

## Focus on Worst Case Scenario
### By using the worst-case scenario as the foundation for planning, the solution is designed to remain robust and efficient even during peak demand periods. 
<hr>

## The Airport Analogy
### Airports are able to manage high volumes of people and effeciently direct to their gates while minimizing confusion and maximizing compliance with the system demands. We can take inspiration from this in the following ways: 
 - Segmentation and Pre-Sorting
    - At airports: Pssangers are sorted into different terminals, gates, or check-in lines based on their destination, ticket class, or security needs, minimizing bottlenecks and confusion. The new self-service kiosk system that passengers use to check-in, select seats and print boarding passes.
    - Applying it to the A&E: We can use a pre-arrival triage which can based on severity, age and attendance type. This can be acheived with mobile/web apps or kiosks present at the hospital sites that take the patients details and give a ticket and path to direct patients to:
       - Full A&E - The Emergency Department (for high-acuity cases)
       - Minor Injuries Units (for low-acuity cases)
       - GPs (for non-urgent cases)
    - Patients can self-report symptoms via apps before arriving. The app can also dynamically re-route them to the correct site on real-time factors like distance, wait time and availability.
         
- Visual Cues and Navigation
   - We can see that airports have clear signage and real-time updates that help guide the passengers to the where they need to be. Passengers receive immediate and location-specific messages about gates, amenities and services in their devices. Displaying real-time information on way finding at central points. 
   - Applying to the A&E: Implementing a clear signage and location-specific messaging system. This can be used to indicate priority lanes for elderly and new patients all while redirecting the other patients to the right service:
      - "For minor injuries, you will be seen faster at this MIU"
      - "Severe cases will be treated here; please proceed to A&E"
        
 -  Anticipatory Resource Allocation
    - At airports the number of service counters are open are adjusted dynamically based on the passenger inflow.
    - Applying to the A&E: Using real-time monitoring similar to boarding queues to shft staff between departments or adjust priorities. We can also use the historical data to find out patterns and predict the patient inflow to adjust staff and resources.

### Defining a <i>"Loading Function"</i> for the A&E sites and then applying it to distribute patients while minimizing the standard deviation is a way we can use statistics to see how the Airport Style Management approach will help in improving the overall flow of patients. Combing this with the Segmentation, and anticipatory resource allocation startegies helps further strengthen the system's ability to optimize the patient flow dynamically. 
<h3>Here is how we can integrate the loading function into the Airport Analogy</h3>
 - What is the <i>Loading Function</i>?
   A loading function will mathematically describe how <i>"loaded"</i> an A&E site is in terms of its capacity and resources. It can consider factors like:
     - Number of patients currently being treated
     - Wait times in different departments (A&E, MIU)
     - Staff-to-patient ratio
     - Resource availability (beds)
     
<h3>The goal here is to calculate <i>a Loading Score</i> for each A&E sites dynamicaly.</h3>
 - The Statistical/ML Approach
   The <i>Loading Function</i> can be applied to each A&E site to get Ditribution of Patient Load across all sites in the network. Sites with a lower load score will take on more patients. Hospitals with higher laod scores will take on fewer patients or will redirect patients. Then we minimize the standard deviation from this distribution. By minimizing the standard deviation of the load scores, we ensure that no single site is being overwhelmed while others remian underused. This aligns with the Airport Analogy of directing passengers to less bsuy counters or terminals to balance the service demands.

### Enhanced Airport-Style Management along with the Loading Function
  - Segementation and Pre-Sorting
      - Improvement with the Loading Function: In addition to patient severity and syptoms, the Load Score becomes a key-factor in the pre-arrival triage:
      - If Site A has a high load score and Site B has a low load score, non-urgent cases are rerouted to the Site B automatically.
  - Real-Time updates adjust these scores, ensuring dynamic re-allocation
  - Patients receive messages like:
     - <i>"Site A is currently full. Please proceed to MIU Site B for faster care"</i>
     - <i>"Estimated Wait Time at Site B: 2 hours. Estimated Wait Time at Site C: 30 mins"</i><br>
  <b>Example: Apps or Kiosks can Compute the best A&E site option the following way: <br>Best A&E Site = min(Load Score + Travel Time)</b><br>
 - Visual Cues and Navigation
     - Improvement with the loading function: Real-time load distribution is reflected in central signage or web apps, displaying current load and expected wait-times across A&E sites. The digital wayfinding signboards and directions will direct patients away from overburdened facilities towards less busy ones, reducing localised congestion. Example:
        - "Site A: 90% capacity. Est. Wait Time: 2 hours."
        - "Site B: 50% capacity. Est. Wait Time: 30 minutes."    
 - Anticipatory Resource Allocation
     - Improvement with the loading function: The loading function can also predict resource needs and aid in staff alocation. Additional staff are allocated pre-emtively, or lower-priority cases are rerouted to reduce incoming demand load. Site A's load score predicts a spike in demand on specific days or during specific months using historic data combined with real-time monitoring to anticipate patterns. Example:
        - "Site B witnesses a Monday morning surge, staff are scheduled accordingly."
       
## Casino Psychology
### Casinos excel at altering people's perception of time to keep them engaged. Casinos also use specific colors, special lighting and even music to keep the people as relaxed as possible. Applying this concept for managing the patients' experience while they wait for their treatment will help reduce the mental stress and affect it has.  
 - Environmental Variables
     - Casinos use environmental stimuli (lighting, layout, background music) to distract patrons and create a seamless flow.
     - Applying it to the A&E sites:
        - Introducing Pleasant lighting, soothing colors.
        - Using music or audio cues in waiting rooms to reduce stress and create a sense of progress. Examle. Notification - "You're number is next!".
 - Perception of Progress
      - People feel a sense of progress even when they are staionary, for example spinning wheels and flashy animations.
      - Applying it to the A&E sites:
         - Provide small "wins" like quicker assessments or initial consultations, without compromising the quality of the consultation, even if full treatment isn't immediate.
         - Giving people an udpate on the queue. Example:
            - "3 patients are ahead of you."
  - Controlled Choices
      - In casinos people are given apparent choices that feel empowering but lead them where the system wants.
      - Applying it to the A&E sites:
         - Creating a flow that directs people to the correct Site type by offering them guided choices. Example:
            - "MIU team at Site A is ready to assist you now."
            - "Would you like to skip the wait? Specialists at Site B are available immediately."
            - "We’ve reserved a spot for you at the MIU Site B. Follow the path provided for quick care.

## Event Driven Process Chain to Demonstrate the analogy in action. <br>Following Two scenarios:<br>  

### 1. Patient is at the site already.

![Correlation Matrix](arrived.jpg)

<hr>

### 2. Patient is not at the site(patient at home/office/etc.) - Care Routing System (CRS)

![Correlation Matrix](home.jpg)

<hr>

### Part Two: Expanding the Capacity in departments/creating new departments and see how the solution would change.

### Data Collection: To calculate where we must place the department we need to Collect the following data: Patient X, Patient Y, Distance to the closest department from each patient.

 - Things to consider:
    - Patients may not be at home, and dense population/traffic flow might be better indicators.
       <p>So instead of solely relying on Patients X and Y, integrate data about population density and traffic flow patterns for specific days and hours. Using the weighted-mean of high-traffic areas or population centres during peak demand times to better predict the optimal new department location. Leveraging data like: mobile phone density or traffic counters (if available) and Pat_Loc_GPs to identify regions with high patient registrations.</p>

       
### Using Weighted Mean of Data to find the Optimal Location for Creating new Departments
 
How it would work: 
 - For each patient, calculate the distance to the closest department.
 - Store the distances in an array and sort it in descending order. Sort distances to identify outliers that might disproportionately influence the mean. Consider limiting weights for patients far outside the target area (eg. > 40 miles).
 - Take the Weighted Mean of their X and Y co-ordinates: This will be the New Departments location. 

 - Formula -> Weighted Mean = (Items * Weight) / Sum of all Weights
   - Items: represents Patient X and Y (separately)
   - Weight: represents the distance for each patient to the closest department

  Insert Formula SC here.
  Xn = ∑ di X1 / ∑ di
  <br>
  Yn = ∑ di Y1 / ∑ di
  <br>
  
  Meaning of the Symbols - <br>
   - Xn: is the X co-ordinate for the new department.
   - Yn: is the Y co-ordinate for the new department.
   - ∑: is the Symbol for Summation or to declare that we must take the sum of all values present.
   - di: is the the distance for each patient to the closest department
   - X1: is the X co-ordinate of the patient
   - Y1: is the Y co-ordinate of the patient

  <h4>Associating New Sites with Main Sites</h4>   
  <p>Associate the eah new site created with the Site Code so that we can know which sub-department/new department created is associated with a bigger site and not acting as a separate entity. This ensures continuity and avoiding isolation of critical care. New departments are tagged as satellite or support units for a mian site. Eg. Main_Site_X -> Satellite_MIUs, telemedicine zones, or urgent care units. Devlop rules for transferring patients with esclating symptoms to the main site. E.g., “If symptoms are flagged critical at a satellite unit, immediate transport to Main_Site_X is initiated”.</p>

  <h4>Assumptions</h4>
  <p>We will also make the assumption that the optimal site that we have found is either empty or has an available space to incorporate the new department. While assuming available space is practical for initial calculations, it is essential to analyze real-world constraints like land availability, building costs, and zoning laws. Using cost-weighted decision-making to prioritize feasible locations. we must also consider the Main Site transport feasbility. Ensure that transport infrastructure supports quick patient transfers between satellites and main sites. Factoring in the availability of an ambulance and average response times.</p>

  <h4>An Alternative to Simplify the Calculation</h4> 
  To simplify calculations we can group patients by postcode or GP cluster. Reverse-Engineering the Pat_Loc_GPs we can group patients by postcode or GP area to simplify calculations for the weighted mean. Aggregate data by groups, then using Pat_Loc_GPs as a proxy for grouping patients into clusters. For Example:
   - Patients within the same postcode or within a specific radius of a GP cann be treated as a single group.
   - Assign a central point for each group, reducing the computational complexity.   

 

## Choosing Resolving Method 
### Analyze the Alternatives to understand outcomes of each (consequences) 
### Comparison of the consequences and selection of the right alternative

## Resolving Problem
### Results and Conclusions

## Implementation of Solution
### Implementation of the result and evaluation of the degree/percentage of success.



