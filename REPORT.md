# Operational Research Challenge

## Problem Formulation 
### Part One: The central problem we aim to solve is optimizing the allocation and utilization of Accident & Emergency (A&E) services within a defined geographic area. This includes minimizing unnecessary use of A&E services, improving patient flow efficiency, and ensuring that patients receive timely and appropriate care.

# Key Questions to Address (Objectives)
 - How can we reduce unnecessary A&E attendances through reallocation and pre-arrival guidance?
 - What are the optimal resource allocation strategies to minimize waiting times at A&E?
 - Where should additional resources (e.g., MIUs, GP capacity) be allocated geographically to ease pressure on A&E?
 - How do different attendance types (e.g., planned, unplanned, frequent re-attenders) impact A&E demand and resource needs?
 - How can we improve patient understanding of the best facility to visit based on their condition?


## Data Collection
### Since all the data has already been provided already, here is a heatmap created to show the correlation between each data definition. The Correlation is being shown using the Spearman's rank Correlation. [From google - In statistics, Spearman's rank correlation coefficient or Spearman's ρ, named after Charles Spearman and often denoted by the Greek letter or as, is a nonparametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function.]

![Correlation Matrix](output.png)


## Mathematical Modelling - Using Queuing Theory for Wait Times & Linear Optimizing website for the main re-allocation problem. 
### Performance Measures - Wait Times and Effective Re-allocation. Thinking only about the worst case scenario: everyone that comes into the department is a new - unplanned attendance. 
### Alternative Courses of Action - An Airport Style attendance management system might be useful here. Use of Event Driven Process Chains and or State Tables to demonstrate the System. 
 - Grouping MIU/Other patients as one entity and then use the Queuing theory. Where we can apply First Come First Serve instead of a Priority based queue.
 - Grouping ED patients as another entity where we can apply a priority based service.
 - Solution to the problem of re-allocation will include a hybrid approach that Airports and Casinos use to manage peopl eand sort them around.

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
     - <i>"Estimated Wait Time at Site B: 2 hours. Estimated Wait Time at Site C: 30 mins"</i>
  <b>Example: Apps or Kiosks can Compute the best A&E site option the following way: <br>Best A&E Site = min(Load Score + Travel Time)</b>


## Casino Psychology
### Casinos excel at altering people's perception of time to keep them engaged. Applying this concept for managing the patients' experience while they wait for their treatment will help reduce the mental stress and affect it has.  

## Choosing Resolving Method
### Analyze the Alternatives to understand outcomes of each (consequences)
### Comparison of the consequences and selection of the right alternative

## Resolving Problem
### Results and Conclusions

## Implementation of Solution
### Implementation of the result and evaluation of the degree/percentage of success.



