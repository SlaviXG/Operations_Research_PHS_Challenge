# Operational Research Challenge

### The Structure that we will implement for this report: The Problem - The Methodoly we used to solve it - Details of the solution with the diagrams to support the theory Diagrams
(This is to get the reader interested from the start)

## Problem Formulation 
### Part One: The central problem we aim to solve is optimizing the allocation and utilization of Accident & Emergency (A&E) services between departments provided. This includes minimizing unnecessary use of A&E services, improving patient flow efficiency, and ensuring that patients receive timely and appropriate care.

# Key Questions to Address
 - How can we reduce unnecessary A&E attendances through reallocation and pre-arrival guidance?
 - What are the optimal resource allocation strategies to minimize waiting times at A&E?
 - Where should additional resources (e.g., MIUs, GP capacity) be allocated geographically to ease pressure on A&E?
 - How do different attendance types (e.g., planned, unplanned, frequent re-attenders) impact A&E demand and resource needs?
 - How can we improve patient understanding of the best facility to visit based on their condition?

## The Correlation Matrix
### What is a Correlation Matrix -- A correlation matrix is a table that shows the correlation coefficients between variables. These coefficients measure the strength and direction of relationships: 

 - Values range between -1 (perfect negative correlation) and 1 (perfect positive correlation).
 - Positive correlation: As one variable increases, so does the other.
 - Negative correlation: As one variable increases, the other decreases.
 - Values near 0: Little to no linear relationship between the variables.

<h3>Purpose and Usage of the Correlation Matrix</h3>

<p>At the outset of this study, a correlation matrix was utilized to statistically analyze how the various variables provided in the dataset interact and influence one another. The correlation matrix highlights the relationships between key attributes such as Site Code, Patient Coordinates (Pat_X, Pat_Y), Number of Attendances, and Resource Availability (e.g., Site_Loc_GPs). By doing so, it serves as a foundational tool to identify patterns, dependencies, and areas of focus for decision-making. The matrix was crucial in understanding which variables are strongly intertwined and could provide actionable insights. Examples of its application include:</p>

 1. <b>Determining Key Relationships:<br></b> <u>Site_Loc_GPs and Site_Loc_GP_List (Correlation -> 0.93):</u> Indicates that areas with more GPs tend to have a higher number of patients registered with those GPs. This insight was used to assess how site resources and surrounding population densities interact.<br> <u>Pat_X and Site_X (Correlatio -> 0.72):</u> Shows a strong relationship between patient and site locations on the X-coordinate, which reinforces geographic proximity as a significant factor in patient distribution.
 2. <b>Identifying Variables with Weak or No Correlation:<br></b> <u>Site_Pop_20miles and Pat_Y (Correlation -> -0.06):</u> A negligible relationship suggests that the total population within 20 miles of a site does not directly correlate with patient Y-coordinates, indicating other factors (e.g., specific site types or referral pathways) may play a larger role in patient inflow.
 3. <b>Validating Assumptions for Resource Allocation:<br></b> <u>Number_Of_Attendances and Site_Loc_GPs (Correlation -> 0.12):</u> A weak positive relationship shows that the number of local GPs has a minimal direct impact on A&E attendances. This insight supports the focus on patient-centric factors like travel time, site capacity, and wait times, rather than relying solely on GP availability.

<h3>Why the Correlation Matrix Matters</h3>
<p>The correlation matrix is not just a statistical tool but a decision-making guide that was instrumental in:</p>

 - Prioritizing Variables for Analysis: Understanding which factors (e.g., patient location, site capacity, GP coverage) are most influential in patient flow and resource utilization.
 - Shaping Strategies: Using the identified relationships to design interventions like patient redistribution, optimal site selection and dynamic resource allocation.
 - Validating Methodology: Ensuring that the chosen methods align with the statistical realities of the dataset.

![Correlation Matrix](./dat_vis_assets/output.png)

<p>By incorporating the correlation matrix at the start of the analysis, we ensured that all subsequent decisions and models were grounded in data-driven insights, making the solutions more targeted, efficient, and impactful.</p>

<hr>

## Solving the Problem for the Worst-Case Scenario
### By using the worst-case scenario as the foundation for planning, this solution is designed to remain robust and efficient even during periods of peak demand. It optimizes patient flow and resource allocation in A&E departments under the assumption that all patients are unplanned and require immediate attention.

## Mathematical Modelling for Managing Patient Flow Using: 
###  - Queuing Theory 
###  - Loading Function 

### Queuing Theory for Grouped Patients

<h4>Objective: Minimize delays for critical patients while balancing fairness for all.</h4>

To simplify the complexity of patient management, categories are grouped and modeled to address their specific needs:
 - MIU/Other:
    - Treated as First Come First Serve (FCFS) for low-acuity cases.
    - Simplified queue for predicting wait times and optimizing resource allocation (eg. triage nurses, rooms)
    - Goal: Minimize the wait times for minor injuries, avoiding bottlenecks
 - ED (Emergency Department):
    - Modeled as Priority Queuing System for high-acuity cases.
    - Cases with priority:
       - High-priority cases bypass queues for immediate attention.
       - Low-priority cases wait until resources are free.
      
### Loading function for System-Wide Balance

<h4>The Statistical Approach</h4>

 - To effectively manage patient flow and optimize resource allocation across multiple A&E sites, we have developed a Loading Function to dynamically assess the busyness of the specific departments (e.g., Emergency Department [ED], Minor Injuries Unit [MIU], etc.) of an A&E site instead of calculating the load on the entire site. This ensures that patient redirection decisions are made based on a granular understanding of department-specific loads, as overall site load may not fully capture the operational strain on individual departments.
    - Load Score Formula = { (Beds Occupied / Department Capacity) * 100 } + { (Wait Time(mins) / Critical Wait Time(mins)) * 100 } 
       1. [ Beds Occupied / Site Capacity ] : This component calculates the percentage of patients in a specific department (e.g., ED, MIU), providing a department-specific indicator of capacity strain.
         - Example: If the ED has 30 out of 50 beds occupied, this contributes 60% to the Load Score for that department.
       2. [ Wait Time / Critical Wait Time ] :
          - Wait Time - Captures the time patients are currently waiting within a department. The upper bound of the wait time range is used to account for worst-case scenarios.
          - Critical Wait Time - Normalizes the wait time against a threshold, such as 240 minutes (4 hours), to express the severity of delays in proportion to what is deemed acceptable.
    - Interpretation: 
      - If the Load Score is ->
        - 100% or more then site is overloaded.
        - Scores under 65% indicate a manageable load suggesting the site can still handle additional patients.
   
   <h4>Granular Analysis for Patient Redirection</h4>
   <p>Instead of evaluating the load at the site level, we compare department-specific Load Scores across all nearby sites. This allows the system to recommend the optimal department within the most suitable site for patient redirection. For example, an overloaded ED at Site A may not preclude sending patients to its MIU if that department has a manageable Load Score.</p>
    
    - Sample Scenraio:
        - Scenario 1: Manageable Department Load
           - Department Type: ED
           - Beds Occupied: 25
           - Department Capacity: 50
           - Wait Time: 30 mins
           - Critical Wait Time: 240 minutes
           - Load Score: { (25 / 50) * 100 } + { (30 / 240) * 100 } = 50 + 12.5 = 62.5%
           - Interpretation: The site is operating well within the Load Score.
             
        - Scenario 2: Overloaded ED but Manageable MIU
         - Site A
           - Department Type: ED
            - Beds Occupied: 48
            - Site Capacity: 50
            - Patient Wait Time: 180 mins (3 hours)
            - Critical Wait Time: 240 minutes
            - Load Score (ED): { (48 / 50) * 100 } + { (180 / 240) * 100 }  = 96 + 75 = 171%
            - Interpretation: The ED is critically overloaded.

           - Department Type: MIU
            - Beds Occupied: 10
            - Capacity: 30
            - Wait Time: 20 mins
            - Load Score (MIU): { (10 / 30) * 100 } + { (20 / 240) * 100 } = 33.3 + 8.3 = 41.6%
            - Interpretation: The MIU is underutilized and can handle additional patients.
      
      - System Recommendation: Redirect patients with minor injuries or non-emergency conditions to the MIU of Site A to reduce ED strain.

        - Scenario 3: Site-Level Overload but Departmental Opportunities
         - Site B:
          - Department Type: ED
          - Beds Occupied: 40
          - Capacity: 50
          - Wait Time: 150 mins
          - Load Score (ED): { (40 / 50) * 100 } + { (150 / 240) * 100 } = 80 + 62.5 = 142.5%
          - Interpretation: The ED is severely strained.
         - MIU:
          - Beds Occupied: 5
          - Capacity: 20
          - Wait Time: 15 mins
          - Load Score (MIU): { (5 / 20) * 100 } + { (15 / 240) * 100 } = 25 + 6.25 = 31.25%
          - Interpretation: The MIU is lightly loaded.

      - System Recommendation: Route patients requiring minor care to Site B's MIU instead of Site A's ED to balance load between the departments.
         
   <p>By incorporating department-specific Load Scores, this approach ensures optimal use of available resources, minimizes patient wait times, and balances workload across both sites and individual departments.</p>

   <h3>Making Emergency Department (ED) Load Scores Accessible to the Public</h3>
   <p>While the ED Load Score is primarily designed for internal use by hospitals for efficient staff allocation and ambulance routing, it is equally critical to make this information available to the general public in emergency situations. By integrating real-time ED Load Scores into the PHS web app, individuals can make informed decisions about where to take a critically ill person in life-threatening scenarios, ensuring faster access to emergency care.</p>

## Course of Action:
### - E-Ticket System 
### - Casino Psychology

### Integration of the Loading Function in the Framework

 1. <b>Backend System for Efficient Site Management:</b> The backend system utilizes the Loading Function to continuously monitor the operational status of all A&E sites. This information ensures that resources are allocated dynamically to maintain balance across the network:
     - Real-Time Monitoring -- The backend calculates the Load Score periodically (e.g., every 15 minutes). Each site’s score is visualized on a central dashboard, color-coded to indicate site status:
        - Green (Load Score < 50%): Manageable load.
        - Yellow (Load Score between 50%–90%): Approaching capacity.
        - Red (Load Score from 90%-100% or higher): Overloaded and requires immediate attention.
     - Resource Allocation: Sites with high Load Scores trigger alerts to reallocate staff or resources to handle surges.
     - Patient Redirection: The system identifies alternative sites with lower Load Scores and redirects non-critical patients to those locations to alleviate pressure off of sites with a high Load Score.
 2. [Web Application](#data-utilization) for Patient Guidance -- The Loading Function also plays a vital role in patient-facing systems, ensuring that patients are directed to the most appropriate site for their needs:
    - Pre-Sorting Patients: When patients input their symptoms into the web application (mentioned below) the system determines the appropriate care type (e.g., ED, MIU, or GP).
    - Directing Patients to the Optimal Site:
       - The Loading Function identifies the best site based on the calculated Load Score, balancing proximity, resource availability, and wait times.
       - Example Messages:
          - “MIU at Site B has shorter wait times. Distance: 5 miles | Travel Time: 10 minutes.”
          - “Emergency care available at A&E, Site A. Estimated Wait Time: 1 hour.”
       - Real-Time Updates for Patients: Patients are informed of current site statuses using intuitive visuals, such as:
          - “Site is free.”
          - “Site is moderately busy.”
          - “Site is at capacity.”
 - Example Use Case -- A patient opens the [web application](#data-utilization) to report symptoms of mild chest pain. The system:
    1. Identifies the patient’s location and care type (Emergency Department required).
    2. Calculates the Load Scores for nearby A&E sites and recommends the least burdened site.
    3. Displays a recommendation:
       - “Site A: Emergency care available. Distance: 7 miles | Travel Time: 22 minutes | Wait Time: 45 minutes.”
    4. Generates an e-ticket with the site information, which the patient uses upon arrival for seamless check-in. 

<p>This integration of the Loading Function ensures that it is not just a theoretical concept but a practical tool driving better patient care and resource management in line with the Airport Management framework.</p>    



### Data Collection & Structuring   
### PHS Web App: Streamlined Patient Registration and Appointment Management 

<h3>Data Collection</h3>

<p>To streamline patient care and optimize resource allocation, we can register patient profiles through their existing
<b>Scottish Community Health Index (CHI) numbers</b>. This system allows individuals to register, add and update critical medical information,
including:</p>

 - Patient Name, Date Of Birth (age), Address.
 - Contact Information: For emergency updates and communication.
 - Medical History & Blood Group: Records of past illnesses, surgeries, treatments and their blood type.
 - Allergies: Allergies that the patient has and any medication they might be taking for it.
 - Current Prescriptions: Active medications that the patient is taking.
 - Viewing upcoming appointments, scheduling new ones, and canceling existing appointments.

<p>The patient will be given a specific tage according to all the details entered for eg. someone who is old and is dealing with medical condition will be given a higher priority profile when booking appointment, or someone with a life threatening condition will be given specific class or priority.</p>

<p>Integrating these profiles into the healthcare system ensures that patient details are readily available during emergencies or regular visits, 
allowing for faster and more efficient treatment. Patients profile is created with a QR code that can be scanned to view their details and access their treatment history and updates through a 
<b>Public Health Scotland (PHS)</b> web application, enabling a seamless flow of information between patients and healthcare providers.</p>

<p>
Utilizing this data to our advantage: we can streamline the reallocation of patients. By employing the loading function to assign the most 
suitable A&E site to each patient, we address a major bottleneck: the inefficiency of patients needing to reallocate themselves. This approach also 
ensures that patients arriving at the hospital are informed about exactly where they need to go, improving overall efficiency and reducing confusion.
</p>

<hr>

### Data Utilization

<h3>The Web App: Registration and E-Ticket Generation</h3>

<p>Using a Web App: Patients access the PHS web app where they register themselves using the Scotland CHI number and book an appointment. The web app processes this information to:</p>

1. Determine the Type of Care Needed:
 - Patients input symptoms they are facing at the moment via the app.
 - The system analyzes the data to decide if they require:
   - Emergency Department (ED) for high-acuity cases.
   - Minor Injuries Unit (MIU) for non-critical injuries.
   - General Practitioner (GP) for consultations or non-urgent care.
   
2. Identify the Optimal Site:
 - Using the Loading Function, the system evaluates nearby healthcare sites to determine the one with the most manageable load, balancing efficiency and reducing patient wait times.

3. Generate a Patient Ticket:
 - After processing the patient’s details and care requirements, the app generates an e-ticket containing:
  - QR Code: This can be scanned to directly load all the patient details previously entered into the system.
  - Site Code: The identifier for the recommended site.
  - Department Type: Specifies the type of department (e.g., ED, MIU).
  - Site Location: Address of the Site.
  - Ticket Number: A unique identifier for the patient.
  - Status of the Site: The current level of congestion or occupancy at the site.
    
4. Streamlined On-Site Process:
 - Upon arrival at the A&E site, the patient shows their ticket and a valid ID, which can be referred to by staff before going for the treatment.
 - The patient’s details, already entered through the web app, are automatically loaded into the hospital’s system by simply scanning the QR code on the ticket.
 - This allows for seamless registration and ensures the patient receives timely and appropriate care.       

<b><p>We use a QR Code for its simplicity and reliability. QR codes are easy to generate and scan, making them a practical solution for 
streamlining patient check-ins. A key feature of QR codes is their error correction capability, which allows them to remain scannable even if they 
are partially damaged by scratches, smudges, or other external factors. Additionally, this feature enhances readability, ensuring that QR codes 
can still be scanned accurately even if partially obscured, such as by stickers or minor physical defects.</b></p>

<b><p>This is a sample ticket that will be generated on the website for the patient. The ticket includes a QR Code that can be scanned upon arrival 
at the site. Once scanned, the patient’s details—such as patient name, age, medical history, allergies, and current symptoms—are automatically 
loaded into the system, allowing staff to provide appropriate treatment promptly. The patient’s identity can be verified by asking them to present 
a valid ID, which can then be matched with their name and date of birth.</b></p>

<b><i>This system ensures a seamless and efficient patient registration process, minimizing delays and enabling faster access to care.</i></b><br>
<b>The colored box next to the QR code represents the current load at the site assigned to the patient, while the color blocks at the bottom correspond to the all types of load levels for a site.</b>
<br>

![Sample Ticket with QR Code from web app](./dat_vis_assets/webapp.png) 

<br>

<h3>Public Accessibility through the PHS Web App</h3>

   - Real-Time Load Visibility: The PHS web app will display real-time ED load information for all A&E sites nearby. Users can view a color-coded or percentage-based load status to identify which ED is the least strained and most capable of handling emergencies.
   - Designed for Emergencies: Unlike standard appointment booking or check-in processes, this feature bypasses all detailed patient registration requirements. It is specifically tailored for time-sensitive situations where there is no time to enter symptoms or other details.
   - Enhanced Communication: Users can also directly contact the identified ED through the app, notifying them of the incoming critical case, which allows the hospital to prepare accordingly.

   <b>Example Scenario: Responding to a Life-Threatening Emergency</b>

   1. The Emergency:
      - A person suffers a heart attack at home or in the office. A family member or colleague realizes that immediate action is required to save the individual's life.

   2. Accessing the PHS Web App:
      - The family member or colleague uses the PHS web app on their smartphone or computer to quickly check the real-time ED load of A&E sites in their vicinity.
   
   3. Identifying the Optimal ED:
      - The app displays three nearby A&E sites with their respective ED load status:
         - Site A: 120% Load (Severely Overloaded)
         - Site B: 85% Load (Manageable)
         - Site C: 65% Load (Lightly Loaded)
         - Example Message: "Please proceed to Site C if you or someone nearby is experiencing life-threatening symptoms."

   4. Direct Contact:
      - Through the app, they call the ED at Site C to inform the staff about the critical nature of the situation and the patient’s expected arrival. They can also call and request an ambulance if transportation is not available at the moment. 

   5. Transport and Arrival:
      - The patient is taken directly to the ED at Site C, avoiding delays caused by overcrowded facilities and ensuring they receive timely care.   

<h3>Benefits of Public Access to ED Load Scores</h3>

   - Improved Decision-Making: Empower individuals to make quick, informed decisions during emergencies by showing real-time ED availability near them.
   - Reduced Delays: Help prevent patients from being taken to overburdened EDs, where wait times could be critical, by identifying the most optimal site for immediate care.
   - Enhanced Coordination: Allow ED staff to anticipate critical cases and prepare ahead, reducing response time upon the patient's arrival.

<p>By making this information publicly accessible in a simple, user-friendly format, the PHS web app can play a vital role in saving lives during emergencies. It bridges the gap between internal hospital systems and public usability, ensuring that critical care reaches those who need it most—when they need it the most.</p>

### Achieving Pre-Sorting through Kiosks on Site: Health Check-In Kiosk 

<p>The kiosk system is designed to streamline the entry of patient data, addressing the potential time constraints of entering details on-site.</p>

   - For patients with a pre-existing profile, the process is expedited through a profile scan.
   - For those without an account, the kiosk offers quick-select options to generate a ticket efficiently.
   - For patients unable to use the digital system, a paper-based form is available to ensure inclusivity and accessibility.
      - The paper form will collect essential details such as the patient’s name, age, symptoms, allergies, and medical history.
      - To integrate the paper form with the digital system, it will be submitted to the reception desk.
      - At the reception, the form will be processed through a stamping machine, which assigns the next available token number and determines the appropriate department for the patient, mirroring the functionality of the web app in the digital system.
      - The form, now stamped with a token number, will be returned to the patient, enabling them to proceed seamlessly to the assigned department.    

<p>Using Kiosks at the Site: Patients who arrive directly at the A&E site can use user-friendly kiosks to streamline the registration and sorting process. Unlike the web app, kiosks do not need to calculate the Loading Function as the patient is already at the site. The kiosk generates a ticket based on the department the patient needs to visit.</p>

<p>Process for Kiosk Usage</p>

 1. Inputting Patient Information:
  - The kiosk can just scan the QR code of the profile and then the patient can proceed and enter Symptoms they are facing
      
 2. Determining the Required Department:
  - Based on the symptoms provided, the kiosk directs the patient to the appropriate department:
    - Emergency Department (ED)
    - Minor Injuries Unit (MIU)
    - GP or other relevant services available at the site
      
 3. Generating a Patient Ticket:
  - The kiosk provides the patient with a printed or digital ticket containing:
    - QR Code: This can be scanned to directly load all the patient details previously entered into the system.
    - Priority Level: Displays the acuity level based on the patient’s symptoms, indicating whether the case is high acuity (urgent) or low acuity (non-urgent). 
    - Waiting Room Number: The number assigned to the waiting room where the patient must wait.
    - Ticket Number: A unique number to maintain queue order.
      
  4. E-Ticket Delivery via Email:
   - If the patient provides an email address, the kiosk can automatically send an e-ticket to their email.
   - The e-ticket includes the same details as the printed ticket, ensuring patients have a backup and can easily retrieve their information if needed.

<p>If a patient misses the appointment time:</p>

1. When the patient's token number is called, if the patient does not show up, we will move on to the next token number in line.
2. If the patient returns after missing their initial appointment time, they can proceed immediately, before the next scheduled token, to avoid having their ticket remain pending.
3. The same applies if the patient arrives within 15 minutes of their appointment time.
4. If the patient arrives 15 minutes or more after their appointment time, their ticket will be invalidated, and they will need to book another appointment and generate a new e-ticket.
5. In extreme cases, such as an emergency, a patient arriving later than 15 minutes may be given a pardon and allowed to proceed.

<p>Streamlined On-Site Process</p>

 - Patients proceed directly to the indicated department and present their ticket.
 - Staff use the ticket information to quickly access the patient’s details, ensuring a smooth check-in and registration process.
 - Patients with e-tickets can display them on their smartphones for scanning, further reducing paper usage and improving efficiency.

<p>Why the Health Check-In Kiosks are Effective</p>

 - Reduced Queues at Reception: Kiosks automate the initial registration process, minimizing the need for staff intervention and reducing bottlenecks at the reception desk.
 - Enhanced Patient Experience: Clear and concise ticketing eliminates confusion, helping patients navigate the site and reach the correct department efficiently.
 - Seamless Integration: Tickets generated at the kiosk integrate with the hospital's system, ensuring staff have access to the patient’s information without delays.
 - Digital Accessibility: Sending e-tickets via email provides an additional layer of convenience, ensuring patients have access to their ticket details even if they lose the printed version.

<h3> Adding Visual Indicators: Color Coded E-Tickets</h3>

<p>The color of the e-ticket issued to patients will reflect site status, helping manage expectations and guide behavior. Instead of showing raw numbers (e.g., patients at the site or site capacity), color-coded tickets provide a simple, visual indicator of site load:</p>

 - Red: Site is highly crowded (above 90% capacity)
 - Yellow: Site is moderately busy (65%–89% capacity)
 - Green: Site has manageable load (30%–64% capacity)
 - Purple: Site is very free (below 30% capacity)

 <p>The colors, determined by the formula (Beds Occupied / Department Capacity) * 100</p>

<p>This system complements the web app by providing similar functionality for walk-in patients, ensuring that pre-sorting and registration remain efficient regardless of how patients arrive at the site.</p>

<b><p>This is a sample ticket generated by the kiosk for patients already on-site. The ticket includes a QR Code that can be scanned at the department. Once scanned, the patient’s details—such as patient name, age, medical history, allergies, and current symptoms—are automatically loaded into the system, allowing staff to provide appropriate treatment promptly. The patient’s identity can be verified by asking them to present a valid ID, which can then be matched with their name and date of birth.</b></p>
<b><i>This system ensures a seamless and efficient patient registration process, reducing waiting times and allowing quicker access to care.</i></b><br>
<b>The colored box next to the QR code represents the current load at the site assigned to the patient, while the color blocks at the bottom correspond to the all types of load levels for a site.</b>

![Sample Ticket with QR Code from Kiosk](/dat_vis_assets/Kiosk.png) 

### Instant ID

<h3>ID Tags/Keychains with QR Codes:</h3>
<p>ID tags or keychains with QR codes, which can be scanned to access the patient's complete profile at the A&E Site, can be issued to elderly individuals and children for easy carrying in emergency situations. These tags can be ordered for anyone, and they will feature the patient's unique token number and a QR code linked to their profile on the PHS web app. The QR code can be scanned at on-site kiosks to quickly generate the patient's e-ticket. In emergency cases, ambulances can scan the QR code to instantly load the patient's data, ensuring that they are treated swiftly and accurately without delay.
</p>

![QR Code Key Chain](dat_vis_assets/PHS.png)


### Implementing Airport-Style Information Displays for Patient Guidance

<p>For improved patient navigation at A&E sites, we can implement information display screens similar to the Flight Information Display Systems (FIDS) used in airports. These systems provide clear and concise information to guide travelers to their respective gates, terminals, or platforms.</p>

<h3>Inspiration from Airport Displays:</h3>

 - Displayed Information:
   <p>Airport FIDS typically show details such as Boarding Time, Destination, Flight Number, Gate Number, and Status (e.g., Boarding, On-Time, Delayed).</p>

 - Signage and Directions:
   <p>Clear directional signage is placed above or near the screens, pointing travelers towards specific gates or areas (e.g., "Gates A1-A21 →").</p>

<h3>Proposed Application for A&E Sites:</p>

 - Patient Information Display Screens (PIDS):
   <p>These screens will guide patients to the appropriate department or waiting area with the following details:</p>

      - Next Patient Call Time: Displays the estimated time the next patient will be attended, replacing traditional “Waiting Time” metrics for better clarity.
      - Department Type: Identifies the nature of the department, such as Emergency Department (ED), Minor Injuries Unit (MIU), or General Practice (GP).
      - Department Name: Specifies the department’s focus, such as Cardiology, Orthopedics, or Dermatology.
      - Building Level: Indicates the floor or level where the department is located for easy navigation.
      - Status: Provides real-time updates, such as “No Delays,” “Slight Delays,” or “High Volume.”

 - Enhanced Navigation:
   <p>Clear and visible directional signage will complement these displays, pointing patients toward elevators, stairs, or pathways to reach their assigned department (e.g., “Level 2: Departments A1-A5 →”).</p>

<h3>Benefits of PIDS:</h3>

 - Improved Clarity: Patients can easily locate their assigned department without confusion or the need for repeated inquiries.
 - Transparency: Real-time updates on status and patient flow build trust and reduce anxiety.
 - Streamlined Navigation: Reduces bottlenecks and misdirection, ensuring smoother patient movement throughout the facility.

<p>This approach leverages proven airport systems to optimize patient guidance, aligning with the goal of creating a seamless and efficient A&E experience.</p>

<hr>
       
## Casino Psychology

<p> Casinos excel at altering people's perception of time to keep them engaged. Casinos also use specific colors, special lighting and even music to keep the people as relaxed as possible. Applying this concept for managing the patients' experience while they wait for their treatment will help reduce the mental stress and affect it has.  
Get people to host Board games and invite the other people waiting in queue or just waiting around to spend time with the people around them, time flies when you play games. But what would happen if someone is in too deep playing the game rather hearing their number being called out.</p>

 - Environmental Variables
     - Casinos use environmental stimuli (lighting, layout, background music) to distract patrons and create a seamless flow.
     - Applying it to the A&E sites:
        - Introducing Pleasant lighting, soothing colors.
        - Using music or audio cues in waiting rooms to reduce stress and create a sense of progress. Examle. Notification - "You're number is next!".
 
 - Perception of Progress
      - People feel a sense of progress even when they are staionary, for example spinning wheels and flashy animations.
      - Applying it to the A&E sites:
         - Provide small "wins" like quicker assessments or initial consultations, without compromising the quality of the consultation, even if full treatment isn't immediate.

  - Controlled Choices
      - In casinos people are given apparent choices that feel empowering but lead them where the system wants.
      - Applying it to the A&E sites:
         - Creating a flow that directs people to the correct Site and departemnt type, offering them guided choices on the PHS web app. Example:
            - "MIU team at Site A is readily available to assist you."
            - "Would you like to skip the wait? Specialists at Site B are available immediately."
            - "We’ve reserved a spot for you at the MIU Department. Proceed to Site B for quick care."              

 ### Hosting Board Games to Enrich the Waiting Experience
 <p>To make long waits more enjoyable, A&E sites can host board games in waiting areas. Patients can join games to pass the time, fostering human interaction and creating a positive, engaging environment. Why do this:</p>

  - Increases social interaction and emotional well-being.
  - Reduces the perceived length of the wait.
  - Gives patients a safe, uplifting space to smile and relax during stressful situations.

![Board Games Room](dat_vis_assets/boardgames.jpeg)

<b>Image Source: Wikipedia</b>

  <br>
  <b><u>Addressing the Problem of Missing Calls</u></b>
   <p>One concern with hosting board games in A&E waiting areas is that patients might become so engrossed in the activity that they miss their turn for treatment. To mitigate this, we propose the following strategies:</p>
  
  1. Digital Alerts:
    
   - Send the patient notification/alerts on their device to let them know that their turn is coming up soon or is up next.

  2. Visual and Audio Cues:
     
   - Use large digital displays and frequent announcements to call out patient numbers.
   - Large digital displays and regular announcements (e.g., “Patient 45, please proceed to Triage Room 2”) help ensure that players remain aware of their position in the queue.
     
  3. Dedicated Staff:
    
   - Assign a staff member to oversee game sessions, ensuring players are reminded when their turn is near and can leave promptly without confusion.
     
  4. Game Selection:

   - Introduce shorter, time-limited games (e.g., 10–15 minutes) to minimize the risk of prolonged distractions.<br>
   - Host only short-form games or games that allow players to step away without disrupting others. Examples:
     - Carrom: A quick, interactive game that lets players leave mid-round without halting the game.
     - Uno or Card Games: Simple, fast-paced games where players can step out and others can continue seamlessly.
     - Puzzle Tables: Collaborative jigsaw puzzles that don’t require a fixed number of participants and can be completed over time.
       
<p>Selecting activities that encourage participation while accommodating the dynamic nature of waiting times, these measures ensure patients can enjoy a positive, engaging experience without risking missed calls or delays in treatment.</p>

<p><b>Incorporating casino-inspired strategies, such as visual indicators, engaging activities, and perception management, transforms the waiting experience. The combination of colored e-tickets and board games not only enhances patient satisfaction but also aligns with the overarching goal of improving patient flow while maintaining an emotionally positive environment. Clear, tech-driven solutions address potential issues, ensuring that no one misses their turn while enjoying these innovative features.</b></p>

<hr>

## Event Driven Process Chain to Demonstrate the analogy in action. <br>Following Two scenarios:<br>  

 <b>Event-Driven Process Chains (EPC) and State Tables</b>
 - Document the flow of patients through the system using EPCs or state tables to:
    - Identify ineffeciencies and decision points.
    - Clearly define transitions.
 - Incorporate automation triggers, eg: re-routing based on load scores.

### 1. Patient is at the site already. (On-Site Flow)

<p>This diagram outlines the patient’s flow when they are physically present at the healthcare site:</p>

 1. Patient Arrival at Site: Upon arrival, the patient begins the process at a self-service kiosk.
 2. Triage and Ticket Generation: The kiosk collects the patient’s name, date of birth (age), symptoms, allergies, or current medications, and generates a ticket with a unique identifier.
 3. Symptom-Based Decision: The system analyzes the symptoms and assigns the patient to the appropriate department or waiting room.
 4. Patient Directed to Department: The patient is directed to their designated department based on symptom severity and department availability.
 5. Arrival at Assigned Department: The patient arrives at the assigned department where further assessment begins.
 6. Department-Specific Process:
      - For Minor Injuries Unit (MIU) or other non-urgent care: Patients are treated on a first-come, first-served basis.
      - For Emergency Department (ED): Patients are prioritized based on acuity levels determined by their symptoms.
 7. Treatment and Completion: Once treatment is completed, the patient either exits the care flow or is admitted for further care based on their condition.

<p>This structured flow ensures that patients already on-site are efficiently triaged, directed to the correct department, and treated based on urgency.</p>

### UPDATE CHANGE FCFS TO TOKEN NUMBER BASED

![Patient at Site](./dat_vis_assets/arrived.jpg)

<hr>

### 2. Patient is not at the site (patient at home/office/etc.) - Care Routing System (CRS)

<p>This diagram explains the process for patients accessing care remotely using a web application:</p>

 1. Patient Seeks Care: The patient initiates the care process from home, office, or another location.
 2. Access Web App: The patient logs into the web application and enters relevant medical details such as symptoms, allergies, and current medications.
 3. System Analysis and Ticket Generation: The system analyzes the input to determine the optimal A&E site, calculates the best time to visit, and generates a digital ticket with a QR Code and unique identifier.
 4. Symptom-Based Decision: The system determines the appropriate department based on symptom severity and site availability.
 5. Patient Arrival at Site: Upon arrival, the patient’s ticket is scanned at the site, and all pre-entered medical details are automatically retrieved into the system.
 6. Patient Directed to Department: Based on the retrieved details, the patient is directed to the appropriate department for care.
 7. Department-Specific Process:
      - For Minor Injuries Unit (MIU) or other non-urgent care: Patients are treated on a first-come, first-served basis.
      - For Emergency Department (ED): Patients are prioritized based on acuity levels determined by their symptoms.
 8. Treatment and Completion: Treatment begins promptly, and once completed, the patient either exits the care process or is admitted for further care as needed.

<p>This remote care process enables patients to pre-register for care, reducing delays upon arrival and ensuring they are efficiently directed and treated based on symptom urgency.</p>

![Patient Not at Site](./dat_vis_assets/home.jpg)

<hr>

### Part Two: Expanding the Capacity in departments/creating new departments and see how the solution would change.

### Creating New Department: Type - Minor Injuries Unit 

<h3>Space Readiness for Expansion:</h3>

<p>Acknowledging the importance of ensuring that any available space is not already being utilized for other purposes, a thorough assessment will 
be conducted to identify areas that can be converted quickly and efficiently. These spaces will be maintained in a ready-to-use condition, 
ensuring minimal downtime when creating the new department.</p>

### Express Treatment Centre | ETC - Concept Overview

<p>
The Express Treatment Centre | ETC is a specialized department designed to deliver swift, high-quality care to patients with minor injuries.
This initiative focuses on optimizing processes, eliminating bottlenecks, and leveraging innovative tools to ensure a seamless patient experience.
Initially launched on a small scale, the ETC will serve as a pilot model to refine and evaluate its efficacy before potential scaling.
</p>

<h3>Key Features of the Express Treatment Centre</h3>

1. Target Operating Hours:
   - 8:00 AM to 6:00 PM, covering peak demand times aligned with office hours, school schedules, and other daily activities.

2. Efficient Staffing:
   - Two teams will work 2.5-hour shifts ensuring staff remain alert and energized, minimizing burnout.
      - Team A: 8 AM - 10:30 AM
      - Team B: 10:30 AM - 1 PM (Team A on break)
      - Team A: 1 PM - 3:30 PM (Team B on break)
      - Team B: 3:30 PM - 6 PM (Team A's shift ends)
      - Team B: Shift ends at 6:00 PM
   - Staff currently treating patients during a shift change must complete their duties before transitioning out, ensuring uninterrupted care.
      - If a patient's treatment is ongoing or the patient has not been discharged yet, the staff must continue providing care until the treatment is complete, ensuring the patient is not abandoned mid-treatment or near its conclusion.    

3. Streamlined Patient Flow: Using the Leaky Token Bucket Algorithm
   - Patients are assigned an Express Treatment Centre (ETC) through a web application or on-site kiosks.
   - Upon arrival at the site, patients are allocated an e-ticket, which includes their ETC assignment (if the patient is not already at the A&E site).
   - After being assigned the ETC, patients are directed to the waiting room near the ETC.
   - The waiting room acts as the "bucket" in the Leaky Bucket Algorithm, with patients waiting for their turn. Patients are called into the department based on their e-ticket token number, which will be displayed on information screens in the waiting room.
   - As their e-ticket number is displayed, patients proceed to the ETC for treatment.
   - Treatment in the ETC is based on the information entered by the patient on the web app or kiosks, which can be accessed via a QR code on their e-ticket.
   - Finally, after receiving treatment, patients will either be discharged or re-directed for further care, based on the analysis of their data and treatment needs.

<p>
The Leaky Token Bucket Algorithm is a method used to manage the flow of data or people. Imagine a bucket with a small hole at the bottom, and each
token represents an item (like a patient or data). As tokens enter the bucket, they leak out at a steady, controlled pace. This ensures a smooth, 
manageable flow without overwhelming the system or causing congestion.</p>

4. Simplified Discharge Process:
   - Patients receive a discharge stamp on their prescription or an update on their e-ticket upon completion of treatment.
   - For follow-up care, automated notifications or referral notes are sent directly via the e-ticket system.

<h3>Bottlenecks Addressed</h3>

1. Staff Shortages:
   - Spliting shifts ensure a steady rotation of staff, preventing exhaustion and maintaining efficiency.

2. Ambiguous Triage Criteria:
   - Resolved through pre-sorting using the web app and kiosk systems. Patients are routed directly to the appropriate department.

3. High Patient Volumes:
   - Controlled using the leaky token bucket model, which ensures smooth patient flow based on e-tickets token number.

4. Communication Gaps:
   - The e-ticket system provides patients with clear instructions, including the department and waiting area they need to proceed to.

5. Discharge Delays:
   - A dedicated staff member oversees discharges, ensuring patients leave promptly.
   - The discharge stamp or e-ticket update minimizes confusion and formalizes the process.

<h3>Approach</h3>

<p>The ETC will be implemented on a small scale initially to assess its viability. This controlled rollout will:</p>

   - Allow for iterative improvements based on real-world performance.
   - Provide data-driven insights to refine processes and identify potential scaling opportunities.
   - Minimize risks associated with large-scale implementation.

<p>If the pilot proves successful, the model will be expanded to other sites. If challenges arise that cannot be mitigated, scaling will be reconsidered.</p>

<p>The Express Treatment Centre represents a proactive step toward enhancing patient care for minor injuries. By focusing on efficiency,
clarity, and quality, this initiative has the potential to redefine how MIUs operate, providing faster and more reliable care during high-demand
periods. Starting small allows for evaluation and development of the approach, ensuring that the model is robust before scaling to broader implementation.</p>

<hr>

### Creating a new Site: Type - Satellite Site
### To calculate where we must create the new Site we use the following data: Patient X, Patient Y

<h4>We will make the following Assumptions</h4>
<p>For the purposes of this analysis and planning, we make the following assumptions:</p>

 1. Available Space for Expansion:
    - We assume that the optimal site identified for new satellite locations is either empty or has sufficient space available to accommodate the new department.
 2. Regulatory Approvals:
    - It is assumed that the necessary regulatory approvals, such as zoning permissions and adherence to building codes, have been secured to allow for the construction of these new satellite sites.
 3. Infrastructure and Transport Feasibility:
    - It is assumed that space for these sites is available and suitable for installation without significant delays or obstacles.
    - The satellite sites will be situated in locations with adequate transport infrastructure to support quick and reliable patient transfers between the satellite and associated main sites. This includes the availability of ambulances, well-maintained road networks, and manageable response times.
 4. Financial Feasibility:
    - Financial resources for building, equipping, and staffing these satellite sites are assumed to be available, ensuring operational readiness.
 5. Population and Traffic Flow Considerations:
     - Patients may not always be at home when they require care; hence, high-traffic areas or densely populated zones are assumed to be better indicators for site placement.
 
<p>To further enhance placement decisions, data such as population density, traffic flow patterns, and patient registration statistics (e.g., Pat_Loc_GPs) will be integrated into the site selection process. These insights, combined with tools like weighted-mean calculations, help predict demand in real time, particularly during peak hours or seasons.</p>

<h4>New Satellite Sites Integrated with Emergency, Minor Injuries Unit, and GP Services</h4>
<p>The creation of new, smaller-scale <b>Satellite Sites</b> that integrate <b>Emergency Life-Saving Services</b>, <b>Minor Injuries Units (MIU)</b>, and <b>GP services</b>. These sites will be linked to Main Sites by Site Codes to ensure continuity of care, facilitate efficient patient transfers, and provide access to advanced facilities when needed.</p>

<p>Satellite sites will act as the first point of care, providing essential services such as life-saving treatment and telemedicine consultations until patients can be transferred to the main site for escalated care. Each satellite site will be tagged with a **Site Code**, ensuring seamless integration with the main A&E system. For example, a satellite site associated with **Site_Code: 2** could also support telemedicine, urgent care, or diagnostic services. Clear escalation protocols will be in place to guide patient transfers when necessary. For instance, a critical patient flagged at a satellite site will receive life-saving care on-site while arrangements for immediate transport to the associated Main Site are made. This ensures no interruption in the continuity of care.</p>

<h3>Use of Prefabricated Buildings:</h3>

<p>A prefabricated building, informally a prefab, is a building that is manufactured and constructed using prefabrication. It consists of factory-made components or units that are transported and assembled on-site to form the complete building. Various materials were combined to create a part of the installation process. [Definition from Wikipedia]</p>

   - The use of prefabricated buildings can significantly reduce the cost of establishing satellite A&E sites.
   - These buildings are modular, easy to customize, and can be quickly integrated, allowing for a fast setup.
   - This approach helps streamline the allocation of staffing and the procurement of equipment, ensuring the site can become operational with minimal delay.

![Pre-fabricated Medical Building](dat_vis_assets/prefab.jpeg)

<b>Image Generated from: [deepai.org](https://deepai.org/machine-learning-model/text2img)</b>

### The Beacon System: A Public Emergency Response Platform

<p>The Beacon System is designed to allow individuals in public spaces to send out emergency signals when they collapse or face a medical emergency, such as a heart attack. This system uses a web app to transmit a distress signal to nearby Satellite Sites (medical facilities or paramedic stations located in high-traffic areas such as supermarkets and busy public spaces). The goal is to ensure rapid response and assistance, even if the individual is alone and unable to call for help themselves, someone else—such as a family member, friend, or a random person on the street—can call on their behalf.</p>

<h3>Key Features of the Beacon System:</h3>

1. Emergency Alert Transmission:
   - Signal through Web App:
      - The Beacon web app allows individuals to send an emergency signal containing their GPS location, condition (e.g., heart attack, collapse), and medical profile (if set up in advance).

   - Web App Integration:
      - The web app facilitates the emergency alert system, ensuring that the signal is sent to Satellite Sites and emergency responders without the need for a mobile app.

2. Simultaneous Alert to Multiple Satellite Sites:
   - Multi-Site Notification:
      - When the emergency signal is triggered, the system sends an alert to multiple Satellite Sites near the user’s location. These sites include nearby medical facilities, paramedics, and other emergency responders located in high-traffic areas (such as supermarkets, shopping centers, or transport hubs).
   
   - First-Responder Site:
      - The first Satellite Site to respond within a 1-mile radius of the user is designated as the first responder, ensuring the closest help is dispatched immediately.
      - If no response is received from any Satellite Sites within the 1-mile radius, the call will automatically be re-routed to emergency services (e.g., 999 or local emergency numbers).

3. Response and Communication:
   - Automated Location Sharing:
      - The user’s GPS location is automatically shared with the responding Satellite Site or emergency services, ensuring that responders know exactly where to go.
   
   - Real-Time Communication:
      - Once a Satellite Site responds, they can establish direct communication with the person in distress (if conscious) or continue with the response process to ensure help is on the way.

4. Emergency Medical Information Access:
   - Integrated Medical Profiles:
      - If the user has pre-registered medical information (e.g., allergies, chronic conditions, medications), this data is included with the emergency alert to help responders prepare in advance.

<h3>System Flow:</h3>

1. Pre-Registration:
   - No pre-registration will be required for accessing The Beacon system. If the individual has a [PHS Keychain/ID](#instant-id) issued it can be used by the satellite site to access the patients details that was registered on their profile on the PHS web app. 
   
2. Triggering the Emergency Alert:
   - When a medical emergency occurs (e.g., heart attack, collapse), the user or a nearby witness triggers the alert through the web app.

3. Signal Sent to Satellite Sites:
   - The Beacon web app sends the emergency signal to multiple Satellite Sites within a defined radius of the user,  that have been located in high-traffic areas, like supermarkets or shopping malls.

4. First-Responder Site:
   - The first responder (the Satellite Site nearest to the user within a 1-mile radius) receives the alert, and help is dispatched immediately.
   - If no response is received from any nearby Satellite Site, the system automatically redirects the alert to emergency services (such as 999 or local equivalent).

5. Response from Medical Facility:
   - The responding Satellite Site can communicate with the individual (if conscious) or continue dispatching help to their location, ensuring immediate medical assistance.

6. Fallback Measures:
   - If the situation requires further assistance or no responders are available within the 1-mile radius, the emergency services are notified as the final step for quick intervention.

<h3>Example Use Case:</h3>
<p>Scenario: A person collapses in a public area, and they are alone, unable to call for help.</p>

1. The individual, upon feeling unwell or about to collapse, triggers the emergency Beacon signal through the PHS web app. 

2. This sends a signal containing the person's GPS location and contact (phone number) to the all Satellite Sites within the 1 mile radius or paramedics located near high-traffic areas such as supermarkets, shopping malls, or transit hubs.

3. The first Satellite Site to respond (within a 1-mile radius) receives the alert, and help is dispatched immediately to the individual’s location.

4. If no Satellite Site responds within the 1-mile radius, the system automatically redirects the call to emergency services (such as 999 or the local emergency number).

5. The first responder (the nearest Satellite Site) reaches the person in distress. The response team proceeds with appropriate medical intervention.

<h3>Key Benefits of the Beacon System:</h3>

   - Faster Emergency Response: By notifying multiple Satellite Sites at once, the system ensures rapid help from the nearest available responder, reducing response time.
   - Medical Service Availability: Individuals can rely on the Beacon system to alert the Satellite Sites emergency services quickly in public spaces.
   - Improved Emergency Outcomes: Immediate access to medical information and precise location sharing helps responders act more efficiently and save lives.

<p>The Beacon System is an emergency response solution that leverages a web app to simultaneously notify multiple Satellite Sites (nearby medical facilities and paramedic teams) in case of a public medical emergency. This ensures that the nearest responder is alerted quickly and can take immediate action. If no one within a 1-mile radius responds, the call is automatically redirected to emergency services. This system significantly reduces response time and increases the likelihood of timely and effective intervention.</p>

### Using Weighted Mean of Data to find the Optimal Location for Creating Satellite Sites
 
How it would work (backend of the web app): 
 - For each patient, calculate the distance to the closest department.
 - Store these distances in an array and sort them in descending order. This helps identify outliers that might disproportionately influence the mean. Consider limiting the weights for patients located far outside the target area (e.g., > 40 miles).
 - Calculate the Weighted Mean of their X and Y coordinates to determine the optimal location for the new department.

   <p> Formula- </p> <p>Weighted Mean = (Items * Weight) / Sum of all Weights</p>
   - Items: Refers to the X and Y coordinates of each patient (separately).
   - Weight: Represents the distance from each patient to the nearest department.
  <br>
  
  ![Weighted Mean Formula](./dat_vis_assets/formulas.png)
  
  <br>
  
  Meaning of the Symbols - <br>
   - Xn : is the X co-ordinate for the new department.
   - Yn : is the Y co-ordinate for the new department.
   - ∑ : is the Symbol for Summation or to declare that we must take the sum of all values present.
   - di : is the the distance for each patient to the closest department
   - X1 : is the X co-ordinate of the patient
   - Y1 : is the Y co-ordinate of the patient

  <h4>Simplifying the Calculation</h4> 
  <p>To simplify calculations we can group patients by postcode or GP cluster. Reverse-Engineering the Pat_Loc_GPs we can group patients by postcode or GP area to simplify calculations for the weighted mean. Aggregate data by groups, then using Pat_Loc_GPs as a proxy for grouping patients into clusters. For Example:</p>
   - Patients within the same postcode or within a specific radius of a GP cann be treated as a single group.
   - Assign a central point for each group, reducing the computational complexity.   

  <h4>Visualizing the Weighted Mean of the data using K-Means Clustering and Vonoroi Diagram</h4> 
  <p>To enhance the current method by we are integrating K-Means Clustering to find the optimal locations for new departments and improve demand distribution, visualizing it on a Vonoroi Diagram.</p> 

## K-Means Clustering
<p>Is a technique used in data analysis to group similar similar data points together. It's like sorting a collection of items into categories based on their characteristics, so that items in the same category (or group) are more similar to each other than to items in other categories. In K-Means, K represents the number of groups (or clusters) we want to create. The algorithm works by:</p>

  - Choosing K initial cluster centers (called centroids) at random.
  - Assigning each data point to the closest centroid.
  - Recalculating the centroids based on the new groupings of data points.
  - Repeating the process until the centroids no longer change significantly, meaning the data has been grouped in the best possible way.

### K-Means Clustering: In the context of the problem
 - In the context of our problem, we have patient locations (their coordinates) and we want to determine optimal locations for new A&E departments or services.
 - Patients are spread out over a geographic area, and some areas may have more patients than others. By using K-Means Clustering, we can group patients based on their geographic proximity and demand.
 - The centroids (center points) of these clusters can represent ideal locations for new departments, such as Minor Injury Units (MIUs), to help spread out the patient load and make care more accessible.

### K-Means Clustering: Usage
 <b>1. Collecting Patient Data:</b> Gather patient location data using coordinates (Pat_X, Pat_Y). These represent where patients are distributed geographically.<br>
 <b>2. Applying K-Means Clustering:</b> Use the K-Means algorithm to group patients into clusters based on their locations. The number of clusters (K) corresponds to the number of new departments we aim to explore.<br>
 <b>3. Identifying Optimal Sites:</b> The centroids of these clusters represent the best potential locations for new departments, positioned to serve the highest number of patients efficiently.<br>
 <b>4. Validation:</b> Evaluate whether these locations improve patient access by reducing travel times and balancing patient loads across existing and proposed sites.<br>

<p>The Images below illustrate how the K-Means Clustering works. The smaller circles are the Pat_X and Pat_Y. While the bigger circles are centroids. 
The website below can be used as a tool to demostrate how we will implement it. Illustration of K-Means Clustering Workflow: </p><br>
 - <b>Initialization:</b> Begin with all patient points (small circles) ungrouped. Randomly place a specified number of centroids (representing potential new departments). In this example, there are 3 centroids.<br>
 - <b>Assigning Points to Clusters:</b> Each patient point is assigned to the closest centroid. The points take the same color as their nearest centroid, forming temporary clusters.<br>
 - <b>Updating Centroids:</b> Calculate the mean of all points in each cluster. Move the centroid to this new, more optimal position.<br>
 - <b>Reassignment of Points:</b> Points are reassigned to the updated centroids based on proximity. Colors are adjusted to reflect the new cluster assignments.<br>
 - <b>Iteration:</b> Steps 3 and 4 are repeated until centroids stabilize, meaning their positions no longer change.<br>
 - <b>Result:</b> Once stable, the final centroid positions represent the optimal locations for new sites or departments.<br>
   
<b>From youtube channel: TheDataPost | Link to Video: https://www.youtube.com/watch?v=R2e3Ls9H_fc </b>
<b>K-Means Clustering website from youtube channel: TheDataPost https://www.naftaliharris.com/blog/visualizing-k-means-clustering</b> 
<br>

![K-Means Clustering](./dat_vis_assets/kmeans_clusters.png)

<hr>

## Vonoroi Diagram
<p>A Voronoi Diagram is a way to divide up a space into regions based on the proximity to a set of points. These points are called seeds (or centroids in our case). Imagine a map with several hospitals (seeds). A Voronoi diagram shows which parts of the map are closest to each hospital. Every point within a region belongs to the hospital closest to it. The edges of the regions represent the boundary where a patient is equidistant between two hospitals. In simple terms, a Voronoi diagram tells you which hospital serves which patients based on distance.</p><br>

### Vonoroi Diagram: In the context of the problem
 - After using K-Means Clustering to find the optimal department locations, we need a way to visualize how patients would be allocated to these new locations.
 - A Voronoi diagram will help us visualize the catchment areas of each new department, showing exactly which patients would be directed to which department based on proximity.
 - This visualization is important because it helps us understand whether the new department locations are serving the right areas and whether they can handle the patient load effectively.

### Vonoroi Diagram: Usage
 <b>1. Collecting the Centroids:</b> After applying K-Means Clustering, we obtain centroids representing potential new department locations.<br>
 <b>2. Creating the Voronoi Diagram:</b> These centroids serve as seeds in the Voronoi diagram, dividing the geographic area into regions based on proximity to each centroid.<br>
 <b>3. Visualizing Allocation:</b> The diagram highlights the catchment areas for each department, showing how patients are distributed across locations.<br>
 <b>4. Identifying Gaps or Overlaps:</b> Regions with no coverage or excessive overlap between sites become visible, helping identify underserved areas or opportunities to adjust department locations.<br>

<p>The Images below illustrate how the Vornoi Diagram is being used to visulize the location for the new sites/departemnts. Illustration of Voronoi Diagram Workflow:</p><br> 
 1. Seeds (Centroids): The centroids (points on the map) represent the locations of new sites or departments.<br>
 2. Regions (Catchment Areas): The colored regions depict the areas assigned to each site, divided by borders to clearly differentiate the coverage of neighboring sites.<br>
 3. Coverage Visualization: The diagram helps visualize how well the new departments serve the surrounding areas.<br>

 <p>Applications of the Voronoi Diagram:</p><br>
  1. Backend System Integration:<br>
   - Use the Voronoi diagram to dynamically assign patients to the nearest site.<br>
   - When a patient’s location is provided (Pat_X, Pat_Y), the Voronoi diagram determines which department serves them best, ensuring efficient redirection.<br>
  2. Road Signage and Patient Navigation:<br>
   - Place simplified Voronoi-based signs at key junctions or highways to guide patients.<br>
   - These signs show nearby sites, their coverage areas, and directions based on the patient’s current location.<br>
  3. Identifying Gaps in Coverage:<br>
   - Regions far from any centroid indicate underserved areas, helping identify where to place additional MIUs or A&E departments strategically.<br>
  4. Dynamic Resource Allocation:<br>
   - Update the Voronoi diagram in real-time to reflect changes in patient load, site capacity, or new department placements.<br>
   - Use it for backend logic in dynamic routing systems and resource distribution.<br>

<p>The Voronoi diagram is an essential tool for visualizing patient distribution, identifying underserved areas, and making informed, geography-based decisions for improving emergency care access. Key Benefits of Using Voronoi Diagrams:</p><br>
 - Dynamic Routing Systems:<br>
  - Backend logic for efficient patient redirection based on real-time proximity.<br>
 - Resource Optimization:<br>
  - Visualize coverage and site loads for better allocation of resources.<br>
 - Patient Guidance:<br>
  - Use road signs, kiosks, and apps to reduce confusion and simplify navigation.<br>
 - Strategic Planning:<br>
  - Simulate and decide on new site placements or expansions to improve overall system coverage.<br>

<b>From youtube channel: Revision Village | Link to Video: https://www.youtube.com/watch?v=LOxlRQqHjs4 </b>
<br>

![Voronoi Diagrams](./dat_vis_assets/VoronoiDiag.png)

<hr>

### Integrating K-Means Clustering and Vonoroi Diagram
 - K-Means Clustering groups patients by their geographic location and demand, helping us identify optimal department locations.
 - Voronoi Diagrams then visualize how these locations will divide the area into catchment regions, showing how patients are distributed and allocated to departments.
 - Combined, these tools ensure that we are:
     - Placing new departments in the most needed areas, reducing travel times and balancing patient demand.
     - Visualizing patient allocation, so we can tweak department locations to better serve the population.
 - By applying both K-Means Clustering and Voronoi Diagrams, we create a powerful framework for optimizing A&E department locations and improving overall patient flow.

## Expanding Capacity in Existing Departments

<p>When faced with the challenge of increasing capacity in healthcare facilities, this approach prioritizes feasibility and efficiency. Before 
considering the creation of new departments, first evaluation— whether expansion is possible within existing sites. This involves assessing 
available space and determining if additional capacity can be accommodated effectively. If expansion is viable, direct focus on increasing staffing 
levels and patient beds to enhance the facility's ability to handle surges in patient demand. However, in scenarios where physical expansion is 
constrained—either due to space limitations or logistical challenges— deploy re-purposed Mega Hauler Trucks and Shipping Containers housing the 
complete suite of technology and bedding that is able to provide full care to patients, serving as temporary extensions to existing facilities, 
providing crucial support during high-demand periods. This dual-layered strategy ensures that healthcare systems remain adaptive and scalable, 
meeting patient needs efficiently without the need for costly and time-consuming permanent infrastructure changes.</p>

### Introduction of a new System 
### HERO: Health Emergency Response Operations

<p>The HERO concept aims to address healthcare capacity challenges during times of high demand by utilizing mobile units - trucks and shipping 
containers that will be repurposed and designed to be equipped with medical facilities. These units can be quickly deployed and integrated with 
main A&E sites providing an effective solution to meet urgent needs. The units will support a range of services - from initial assessment to 
diagnostics, wound care and dressing, minor burns treatment, vaccination and so on. This ensures patients receive timely attention without 
overwhelming existing facilities. By integrating these with the Site using the SIte Code, clear communication, and digital queue management, 
HERO is designed to maintain a smooth flow of healthcare services during emergencies and peak periods.</p>

<h3>Trucks Mentioned/Referred to: Denby Eco-Link</h3>

![Big Truck](dat_vis_assets/bigTruck.jpeg)

<b>Image Source: Wikipedia</b>

<h3>Shipping Containers Mentioned/Referred to: Reefer Container carried on Articulated Lorries</h3>

![Shipping Container](dat_vis_assets/container.png)

<b>Image Source: tritoncontainer.com</b>

![Artic Lorry](dat_vis_assets/articlo.jpg)

<b>Image Source: Wikipedia</b>

1. Pre-Designed Trucks and Containers:

<p>Instead of committing significant funds to the construction of permanent expansions, which require substantial time, money, and planning, allocating these resources to pre-designed and repurposed trucks and shipping containers. These units will be fully equippedw ith beds, equipment, computers and ready to deploy during times of extreme need, ensuring a cost-effective and scalable solution to temporary capacity challenges.</p>

2. Integration with Main Sites:

<p>Integration between the trucks and containers with the main sites will be streamlined using the same software system currently employed at the main sites. By simply labeling the mobile units as extensions (e.g., "Mobile Unit - Site Code: N"), the system will maintain seamless operations, including patient record management, staff allocation, and resource tracking. Using the existing software as a main sites make this a straightforward process, minimizing the potential for disruptions or inefficiencies.</p>

3. Clear Communication and Signage:

<p>To ensure clarity for both patients and staff, large, clearly visible signage will be placed on these mobile units. The signage will explain the purpose of the trucks and containers and direct individuals to their specific locations, eliminating confusion about why they are being directed to these temporary facilities.</p>

<b>Purpose and Role of Trucks and Containers:</b> 
<p>The primary purpose of these mobile units is not to replace the existing sites but to alleviate the load on these facilities during times of high demand. These trucks and containers will act as temporary extensions, providing care for minor issues and diseases and ensuring that no patient is left standing or unattended for hours during chaotic times.
Taking into account that in extreme cases, even these mobile units may become overcrowded. However, the goal is not to eliminate all delays but to keep the flow of traffic moving smoothly. Even if the process is slower, maintaining a steady flow ensures that care is provided, and the system remains functional rather than coming to a halt due to the overwhelming demand.</p>

4. Staff Readiness Plan:

<p>While the physical infrastructure (trucks and containers) is ready for deployment, it’s equally crucial to have a standby staffing plan. This could include:</p>
 
 - A roster of on-call staff trained to work in these temporary units.
 - Partnerships with local healthcare providers or temporary staffing agencies to fill gaps quickly.

5. Modular Flexibility for Containers:

<p>Equip containers with interchangeable interiors so they can serve multiple roles (e.g., triage, diagnostics, or even administrative functions) based on the needs of the site. For example, during one surge, a container might act as a vaccination center, while in another it serves as a diagnostic lab.</p>

6. Digital Queue Management:

 - Using the same digital queue management system accessible via a web applications or kiosks at the site.
 - Patients can check estimated wait times for both the main site and mobile units.
 - This ensures transparency and helps patients understand why they are being redirected.

7. Multi-Purpose Design for Trucks and Containers:

 - Beyond healthcare services, these units can also serve other purposes during quieter periods, such as:
    - Community health education centers.
    - Vaccination campaigns or outreach initiatives.
    - Telemedicine hubs, providing remote consultations for underserved areas and over crowded areas.

   <h3>Things to Address</h3>
   <p>The following are the potential questions that come up: </p>

    - How quickly can the mobile units be prepared and deployed to the site in ready to use condition?
    - What are the limitations in handling severe cases or only low-acuity conditions will be handled here?
    - Could staffing the mobile units be a bottleneck in extreme surge conditions?

   <h3>Strategies to mitigate these hurdles</h3>

   1. <b>Deployment Speed:</b>
      - Mobile units will be deployed within 2-4 hours from their designated hangars to the target site.
      - Deployment decisions will be based on pre-emptive analysis of site overloads, identified using the [Loading Function](#loading-function-for-system-wide-balance)
      - For extreme conditions, such as when the [Load Score](#loading-function-for-system-wide-balance) exceeds 150%, the mobile units will be mobilized immediately to alleviate pressure on overwhelmed sites.
   2. <b>Case Handling Capacity:</b>
      - The mobile units will primarily handle low-acuity and medium-acuity cases, such as minor injuries, mild respiratory issues, fractures, or dehydration.
      - Each mobile unit will include a fully equipped life support module (similar to those found in ambulances) to stabilize patients with severe conditions until they can be transferred to the main A&E site if necessary.
   3. <b>Staffing Preparedness:</b>
      - A specialized team will be pre-assigned and on standby to staff the mobile units during surge conditions.
      - Staff allocation will be planned in advance, ensuring there is no delay in deployment. This includes creating a roster of healthcare professionals trained specifically for mobile unit operations.

<h3>Power Supply for the Mobile Units: electric Generator, Equipment fixed securely to the mobile units so that it doesn't move in transit.</h3>

   <h3>Question: Where will patients wait for the Mobile Units, especially in cold or harsh weather conditions</h3>

   <h3>Answer: </h3>
   <p>To ensure patient comfort while waiting for Mobile Units, Inflatable Heated Tents will be deployed alongside the units. These tents will serve as temporary waiting areas and will be equipped with:</p>

   1. <b>Heating Systems:</b> To keep the interior warm and comfortable during cold weather.
   2. <b>Seating Arrangements:</b> Foldable chairs or benches to provide adequate seating for patients and accompanying family members.
   3. <b>Lighting and Visibility:</b> Proper lighting to ensure the space is functional during night hours.
   4. <b>Durable and Weather-Resistant Materials:</b> The tents will be made from robust, weather-resistant materials to withstand adverse conditions like wind, rain, or snow.

   <p>These tents can be rapidly inflated and set up within minutes, ensuring minimal delays and providing a safe, sheltered environment for patients while they wait for their turn to receive care. This solution is cost-effective, portable, and highly efficient, catering to the unpredictable weather conditions.</p>

<h3>Tent Mentioned/Referred to: Negative Pressure Inflatable Medical Tents</h3>

![Medical Waiting Tent](dat_vis_assets/tents.jpg)

<b>Image Source: stretchstructures.com</b>

### Based on all of this how would the solution change:

   <h4>Existing Solution includes: </h4>

   - Queuing Theory: No Change required for this as it can be applied to the Mobile Units as well.
   - Loading Function: The loading function will updated here and instead of using the large scale version where we would find the optimal Site Locationfor the patient, we will use the loading function on a smaller scale to direct patients to either the Main SIte or the Mobile Units based on the Patient_Wait_Time/Age_Group/Symptom_Severity. Load Score adjusted to: Patient_Wait_Time + Age_Group + Symptom_Severity.  
   - Airport Style Management System:
      - Self-Service Kiosk: Will also be updated
      - Clear Signage: No Change, there will still be clear signage for directing the patients to in the Main Site Building or the Mobile Units.   
      - Screens Displaying the real-time data: All the screens displaying the real-time data will show a split view of the data between the Main Site Building and the Mobile Unit at the Site.    
      - Pre-Sorted Ticket: The Pre-Sorted ticket  
   - Casino Pschology: No change here either, the same 
  
## Choosing Resolving Method 
### Analyze the Alternatives to understand outcomes of each (consequences) 
### Comparison of the consequences and selection of the right alternative

## Resolving Problem
### Results and Conclusions

## Implementation of Solution
### Implementation of the result and evaluation of the degree/percentage of success.


Loading Function Backend Visual how will it look like for someone in the backend keeping eye on everything: Screen for the Management 
(an example of how the Mobile Units will be signaled during extreme loads at a or multiple site)

an example layout or image of the satellite site: pre-fabricated homes style design
A visual aid of how the very fast department will look like
Visual of how a beacon system will work.

### Detailed Explaination of the Computations that were performed including all py files.

### Limitations and caveats section at the end.
