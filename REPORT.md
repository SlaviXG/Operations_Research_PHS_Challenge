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
    - At airports: Pssangers are sorted into different terminals, gates, or check-in lines based on their destination, ticket class, or security needs, minimizing bottlenecks and confusion
    - Applying it to the A&E: We can use a pre-arrival triage which can based on severity, age and attendance type to direct patients to
       - Full A&E - The Emergency Department (for high-acuity cases)
       - Minor Injuries Units (for low-acuity cases)
       - GPs (for non-urgent cases)
         
- Visual Cues and Navigation
   - We can see that airports have clear signage and real-time updates that help guide the passengers to the where they need to be. Passengers receive immediate and location-specific messages about gates, amenities and services in their devices. Displaying real-time information on way finding at central points. 
   - Applying to the A&E: Implementing a clear signage and location-specific messaging system. This can be used to indicate priority lanes for elderly and new patients all while redirecting the other patients to the right service:
      - "For minor injuries, you will be seen faster at this MIU"
      - "Severe cases will be treated here; please proceed to A&E"
        
 -  Anticipatory Resource Allocation
    - At airports the number of service counters are open are adjusted dynamically based on the passenger inflow.
    - Applying to the A&E: Using real-time monitoring similar to boarding queues to shft staff between departments or adjust priorities. We can also use the historical data to find out patterns and predict the patient inflow to adjust staff and resources.

## Choosing Resolving Method
### Analyze the Alternatives to understand outcomes of each (consequences)
### Comparison of the consequences and selection of the right alternative

## Resolving Problem
### Results and Conclusions

## Implementation of Solution
### Implementation of the result and evaluation of the degree/percentage of success.



