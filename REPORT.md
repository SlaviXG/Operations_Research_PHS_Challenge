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

## Event Driven Process Chain to Demonstrate the analogy in action. Two scenarios patient is at the site already. Patient is not at the site yet - Care Routing System (CRS)  
## Choosing Resolving Method <br>
### Analyze the Alternatives to understand outcomes of each (consequences) <br>
### Comparison of the consequences and selection of the right alternative <br>

## Resolving Problem
### Results and Conclusions

## Implementation of Solution
### Implementation of the result and evaluation of the degree/percentage of success.



