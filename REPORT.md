Operational Research Report

Introduction - Problem Statement
The solution must balance current patient needs with future planning for increased demand. Graphics are included as links in this document to provide visual aids. Please click on them to view the corresponding images for reference. This report explores methodologies to:
Reallocate demand for A&E services across departments by classifying patients based on their specific conditions.
Virtual Capacity expansion and creating New Departments.
How the solution evolves.


Part One: Optimising A&E Operations by Re-allocating demand

Methodology Used & Explained
Loading Function: To effectively manage patient flow and re-allocate demand for A&E services between departments provided, we have developed a Loading Function to assess the busyness of the specific departments of an A&E site in real-time.
Department-specific Load Scores ensure granular insights.

(Beds Occupied / Department Capacity) * 100: This component calculates the percentage of patients currently being treated and those waiting for care in a specific department (e.g., ED, MIU, GP), providing a department-specific indicator of capacity (available space) strain.
( Wait Time / Critical Wait Time ) * 100:
Wait Time - Captures the wait time of patients that are currently waiting within a department. The current wait time for each department is used to account for worst-case scenarios.
Critical Wait Time (maximum acceptable wait time) - Normalises the wait time against a threshold, 240 minutes (4 hours), to express the severity of delays in proportion to what is deemed acceptable.



The Load Score is a key metric for analysing and comparing the capacity of each department within an A&E site. By calculating the average of the Load Scores from all departments, we can derive an overall Load Score for the site. This metric serves as a critical tool for both backend management systems and patient-facing applications, ensuring demand is allocated efficiently and services remain accessible.

For Management Systems: The Load Score provides administrators with real-time insights into the workload distribution across departments, enabling better resource allocation, staffing decisions, pre-empting and planning for surges in demand.
Load Score between 0% - 70%: Department is operating efficiently.
Load Score between 71% - 85%: Department is approaching capacity; initiate patient redirection to other departments or A&E sites with lower load scores.
Load Score above 85%: Department is overloaded; immediate action required to manage patient flow and alleviate congestion.

For Patients: Through patient-facing applications, the Load Score helps direct individuals to less crowded sites or departments, reducing wait times and ensuring an even patient distribution across all departments and A&E sites.

This dual-purpose approach ensures that A&E sites operate optimally, balancing demand by dividing it across provided departments at A&E Sites.


Implementation of the Loading Function

One-Stop Web Application: A simple, easy-to-use, and navigate web application designed to assist patients in selecting the most optimal A&E site and booking appointments seamlessly through the platform. The application caters to both categories: Registered Patients (with a Medical Profile) and Unregistered Patients (without a medical profile).

Accounting for the Age Demographics of Older People Accessing A&E Services:
To ensure accessibility and ease of use for older patients, the system will provide two additional options tailored to their needs -
Call to Book an On-Site Appointment - Older patients can call a dedicated helpline to book an appointment directly at the A&E site. The staff will assist them in choosing a suitable time and department based on their ailments and proximity to the site. A confirmation will be sent via phone or SMS for their convenience.
Call for At-Home Video Consultation Setup - Older patients can request an at-home service by calling the helpline. The A&E site will dispatch nursing staff equipped with necessary diagnostic tools (e.g., portable blood pressure monitors, pulse oximeters). The nursing staff will assist the patient in setting up a video consultation with a doctor. During the consultation, the nursing staff will relay any required physical observations or conduct minor diagnostic tests under the doctor’s guidance.


Patient not at A&E site

Registering patients on the web app: Patients must register and create a Medical Profile on the web app first by providing their name, date of birth, contact information (such as email or phone number), NHS number, and create a medical profile that includes their past medical history, ongoing medications/allergies, family medical history, and social history (e.g., ex-smoker, etc.). Based on the details entered, each patient will be classified into a profile type. The profile type ranges from "Normal" (healthy) to "Under Periodic Review" (for moderate conditions), "High Risk" (for chronic or recurring illnesses), and "Under Constant Observation" (for severe illnesses). To make sure that the patient's profile remains relevant and up to date on the patient's health an AI bot will be deployed to manage the medical profile, ensuring that with every appointment and visit to the A&E progress is logged and accounted for.
After successful registration, patients will have a medical profile with a unique link (similar to a LinkedIn profile link) and a QR code (similar to a WhatsApp profile QR code) for easy and hassle-free access anytime, anywhere. This profile will be updated after every appointment and prescription. All personal medical data will be available to download for the patient in PDF format.

Patients who are unregistered: Unregistered patients will still be able to use the web app to find the most appropriate A&E sites. For booking appointments, they can simply use a one-time PIN login sent to their email or phone number.

The Web App will have following features -  
Live Load on Sites: This feature displays the total load score of all A&E sites for patients. It helps patients make better decisions when booking appointments online or choosing an A&E site while en route. Additionally, for patients en route it provides a contact number of A&E allowing patients to call ahead in case of emergency situations.
Optimal Site Allocation for Registered Patients Booking Online Appointments: Patients who are successfully registered on the web app can book an appointment slot by simply logging in to their account, select book appointment and start entering their current ailments (e.g., cold and cough, fever, chest pain, etc). Based on the ailments entered, patients Profile Type, the Loading Function, and proximity to the A&E site(s) nearby, they will be allocated to the appropriate department (e.g., GP, MIU) and the most optimal A&E site. After successfully booking the slot, patients will receive a confirmation with details such as the assigned department, A&E site address, appointment time, and token number via email or SMS registered.     
Optimal Site Suggestions for Unregistered Patients: Unregistered patients can use the one-time PIN login via email or phone number. They will need to enter their name, date of birth, and current ailments, and based on those ailments, the Loading Function, and their proximity to the A&E site, patients will be allocated to the most appropriate department and and the most optimal A&E site. The only exception is that the profile type will not be included. After successfully booking the slot, patients will receive a confirmation with details such as the assigned department, A&E site address, appointment time, and token number via email or SMS entered.
Patient Medical Profile: Once the patient arrives at the A&E site, they will be asked to proceed to the specific department assigned to them by the reception. Upon reaching the department, patients must wait for their token number to be displayed on the digital board or called out by the nursing staff. Before entering the doctor's booth, patients must present a valid photo ID or use their NHS number to confirm their identity to the nursing staff.
Once the identity is verified, patients allow the nursing staff to scan their medical profile QR code, which will load it onto the screen for quick analysis and immediate treatment by the doctor. After treatment ends, patients will receive prescriptions and follow-up instructions via registered mail or SMS. A printed version can be provided instantly upon request.
For unregistered patients, a valid photo ID or NHS number will be required as well to verify their identity. Since they are not registered and do not have a medical profile, they will need to provide information about their medical history, ongoing medications/allergies, family history, and social history verbally as usual.
Emergency Alert: This feature is available for both registered and unregistered patients to use in emergency situations, allowing them to immediately contact an A&E site. The web app will use a loading function to display nearby A&E sites and their contact phone numbers, based on the load score and proximity to the patient, without requiring the patient to log in or enter any details. In the event of no response, the patient will be automatically redirected to emergency services, such as 999.




Patient at A&E site (without appointment booking)

Patient Information Display Screens: The Patient Information Display Screens will provide essential details to guide patients, including the next patient call time and token number, department type, and department name. They can also indicate the building level for easy navigation and offer real-time status updates, such as delays or high patient volume using the Loading Function. Additionally, the screens can display the availability status of nearby A&E sites, alerting new walk-in patients if the current site is nearing capacity and suggesting alternative options. 
To enable patients to navigate through the A&E site independently, we can use Wayfinding Tapes running along the walls of the facility. Each tape will be color-coded and clearly labeled, leading directly to the respective departments within the A&E site. These tapes can also include universally recognized symbols for better understanding, making navigation intuitive for all patients, including those who may face language barriers or literacy challenges.
This approach is easy to implement, highly cost-effective, and reduces the need for staff to provide directions, allowing them to focus on other critical tasks.
Patients Registered (with a Medical Profile): Patients who already have a medical profile can still use the web app to book appointments in the same way, by clicking the "Already on-site" button and selecting the A&E site they are at. The only difference is that, after logging in and entering their current ailments, the loading function will calculate the load score for the departments at the site the patient is and assign them to the appropriate department along with a token number, appointment time, and token number via email or SMS registered.

Patients Unregistered (without a Medical Profile): Patients who do not have a medical profile will be able to use the web app to book appointments as well, clicking the "Already on-site" button and selecting the A&E site they are at. They will use one-time PIN login and enter their current ailments, the loading function will calculate the load score for the departments at the site they are at and assign them to the appropriate department along with a token number, appointment time, and token number via email or SMS entered.

Paper-form Option: Patients will be provided with an option to use a paper based form to enter their details name, date of birth and current ailments. To integrate paper forms with the digital system, patients will submit their forms to the reception desk. The forms will be processed through a stamping machine, which assigns the next available token number and determines the appropriate department for the patient, replicating the functionality of the web app in a manual format. Once stamped, the form will be returned to the patient, allowing them to proceed to their assigned department.  

Instant ID: Physical keychains or Cards with QR codes can be issued to patients and can be scanned to access their complete Medical Profile. These tags can be scanned in cases where someone is unable to log in to their medical profile due to technical issues, does not have a mobile device (such as a young child), or during emergencies when the patient is not at an A&E site. For example, ambulances can scan the QR code to retrieve critical medical information, enabling faster and more focused care and eliminating the need for guesswork.


Making Waiting Comfortable: 
To improve the patient experience during long waits, accounting for demographics, strategies like creating comfortable environments with soothing colors and engaging activities can be used. Pleasant lighting that reduces harsh contrasts can help reduce mental stress, creating a calming atmosphere. A&E sites can provide refreshments such as food and drinks, ensuring patients stay hydrated and nourished during their wait without losing a place in the queue. To make longer waits more comfortable, A&E sites can provide board games in waiting areas. These games encourage social interaction, create a positive and engaging environment, and enhance emotional well-being. By reducing the perceived length of waiting times, they can help transform a stressful situation into a more uplifting experience, offering patients a space to relax.
One concern with hosting board games in A&E waiting areas is that patients might become so engrossed in the activity that they miss their turn for treatment. To mitigate this we can introduce shorter, time-limited games (e.g. 10–15 minutes) to minimize the risk of prolonged distractions. Large digital displays and regular announcements can help ensure that players remain aware of the current token number.


Part Two: Creating New Departments & Expanding Capacity 
Methodology Used & Explained

K-Means Clustering: K-means clustering is a method used to group similar data points together. It works by dividing data into a set number of groups (called clusters) based on their similarities. The algorithm identifies the center of each group and assigns data points to the group whose center they are closest to. It keeps adjusting the centers until the groups are as accurate as possible.
Using K-Means Clustering, we can group patients based on their medical profiles—such as their symptoms, medical history, and current conditions. This allows us to:
Categorize patients: Automatically separate patients into groups for video consultations or on-site visits, based on factors like the severity of their condition and medical history.
Prioritize care: Identify which patients need immediate in-person attention and which can be seen virtually, improving the efficiency of resource allocation.
Optimize resources: Ensure that patients who need physical exams are directed to the appropriate department, while those who can be treated remotely are guided to virtual consultations.
It repeats this process until the centers no longer change. In short, K-means clustering helps us assign patients to the right type of consultation, streamlining the process and enhancing overall care delivery.
Formula: K-Means Clustering Example Implementation


Implementation of the Methodologies - Part Two

Acknowledging the importance of ensuring that any available space is not already being utilised for other purposes, a thorough assessment will be conducted to identify areas that can be converted into fully functioning medical sites quickly and efficiently.The physical A&E site can commence construction simultaneously with efforts to increase virtual capacity.

Expanding Virtual Capacity - 

Video Consultation (Addressing Inappropriate Admissions): The main focus is to expand the Virtual Capacity first. To address capacity expansion hurdles, inappropriate admissions, and staffing challenges in A&E operations, a patient sorting mechanism will be implemented using K-Means Clustering. Patients entering their symptoms via a web application will be classified into video consultations or on-site appointments based on their input, medical history, and dynamically assigned profile type (e.g., Normal, High Risk). The algorithm groups patients by severity and care needs, directing minor cases to virtual consultations and urgent cases to physical appointments. Doctors retain the final authority to escalate video consultations to physical check-ups if required. This mechanism streamlines patient flow, reduces inappropriate admissions, and improves overall resource utilization while enhancing patient care and satisfaction.   

Outsourcing Video Consultations: Outsourcing video consultations to countries with large, skilled workforces is an emerging strategy to enhance healthcare accessibility. For example, a multinational hospital group based in the United States sought to offer telemedicine consultations with specialists in Europe and Asia, aiming to provide patients with access to a broader range of expertise. To mitigate the shortage of doctors and enhance patient care efficiency, outsourcing video consultations to countries with substantial, highly skilled workforces presents a viable solution. This strategy involves partnering with international telehealth providers to manage non-emergency consultations, thereby alleviating the burden on local healthcare professionals. Such collaborations can expand the pool of available medical experts, ensuring timely patient consultations and optimizing resource allocation. Implementing this model requires establishing robust communication channels, ensuring compliance with international medical regulations, and maintaining high standards of patient confidentiality and data security. By leveraging global medical expertise, healthcare facilities can improve service delivery and patient satisfaction while addressing staffing challenges.

Utilizing Augmented Reality (AR) Technology for Enhanced Virtual Assessments: To further improve patient assessments on-site, implementing AR technology can create immersive virtual consultation environments. In specialized rooms equipped with AR cameras, patients can engage in virtual consultations with doctors from outsourced locations. This enables doctors to visualize patients in a 3D space using an Augmented Reality headset, providing a comprehensive 360-degree view. Doctor will guide both the patient and the attending nursing staff as needed. This setup enhances the quality of remote assessments, ensuring thorough examinations without the immediate need for on-site specialists. By adopting these advanced technology, healthcare facilities can expand their consultation capabilities, improve patient experiences, and optimize the utilization of medical expertise across different locations.

New Department type

Express Treatment Centres: The Express Treatment Centre is a specialised GP services department focused on delivering swift, high-quality care for patients leveraging automation for efficiency. The ETC will have a Vital Signs Assessment Machine (VSAM), which automates the initial patient evaluation.
Vital Signs Assessment Machine (VSAM): This all-in-one device measures temperature (infrared scanner), heart rate, blood pressure, and oxygen saturation. It includes a hand sanitiser for patient hygiene before use. The collected data is automatically linked to the patient’s profile when the patient scans their Medical Profile QR code or Instant ID to use the VSAM.
Doctor Integration and Prescription: Before the patient enters the assessment room, the doctor’s system loads the VSAM report on a computer monitor along with scanning the QR code and accessing the patient's Medical Profile, enabling quick and informed decision-making on whether a physical examination is required. After treatment, prescriptions are sent directly to the patient’s email or a physical copy can be printed on request, streamlining the discharge process.

The ETC will initially operate on a small scale, enabling data-driven improvements and ensuring processes are refined before scaling to other sites. This department will initially only be assigned to patients registered on the web app with a Medical Profile.

Option to Opt for Preemptive Health Analysis: At the ETC, patients will have access to a comprehensive health evaluation service that combines physical assessments with dietary and lifestyle consultations. Patients can measure their BMI and meet with a dietitian to discuss their eating habits, exercise routines, and overall lifestyle. This information, alongside the patient’s medical profile—which includes their medical history, family medical history, ongoing medications, allergies, social history, and current ailments—will be used to generate a personalized health forecast.
Using AI (Machine Learning) for predictive analytics and advanced modeling techniques, the ETC will provide patients with a graphical representation of their potential health risks or concerns (if any at all) over the next 6 months to 1 year. This forecast will highlight any areas of concern, such as the likelihood of developing chronic conditions, and suggest proactive measures to mitigate risks.
This feature not only empowers patients to take control of their health but also serves as a valuable tool for preventive care. By offering insights into potential health trends, the ETC fosters early interventions, better health outcomes, and a more personalized approach to patient care.
How the solution from Part One Evolves accordingly - 
Initial Sorting of Patients: Patients are first categorized into virtual or physical consultations when booking appointments through the web app. This step ensures that patients are directed to the most appropriate form of consultation based on their needs and availability. To address potential gaps in patient preparedness for video consultations, the solution in Part One evolves by incorporating additional screening questions during the patient intake process. These questions identify whether patients have access to basic medical equipment, such as thermometers and pulse oximeters, and their comfort level using such devices. For patients lacking essential tools or unable to use them, the system adjusts by recommending on-site appointments or scheduling at-home nurse visits equipped with the necessary devices. This adaptive approach ensures that all patients receive accurate diagnoses and appropriate care while maintaining the flexibility and efficiency of the solution.
Sharing Medical Profiles for Virtual Consultations: Before entering the video consultation meeting room, patients can share their Medical Profile link with the doctor via the chatroom of the video conferencing platform. This allows the doctor to review the patient’s medical history and vital data, enabling a quick and efficient assessment during the consultation.
Integration in AR On-Site Rooms: Similarly, when patients visit the on-site AR consultation rooms, the process remains consistent. The Medical Profile link or QR code is used by the attending doctor, present physically or virtually, to instantly access the patient’s medical information, enhancing the seamless integration of advanced technology in on-site treatments.
Feedback Loop: Finally, to further enhance personalized care, it is possible to introduce the feedback loop which could comprise post-consultation feedback collection from each patient (questions on overall experience and the consultation outcome), automated feedback analysis (applied machine learning, including natural language processing, to identify common complaints and actionable insights), and, as a result, adaptive care system adjustments (patient-specific, doctor-specific, or system-specific), overall creating fundamental steps for continuous improvement. 




Presented By: Samraat Jain and Slava Horbanov

Appendix

Observations and Research Process:
To develop this report, Samraat Jain conducted direct observations at an A&E site and engaged in discussions with medical staff to understand operational challenges and patient workflows. These insights were instrumental in identifying inefficiencies and proposing solutions tailored to real-world scenarios.
Limitations: 
Technical Issues: As the system heavily relies on digital platforms, technical issues such as system outages, connectivity problems, or software glitches could disrupt patient flow or cause delays in ticket generation and navigation.
Data Quality and Accuracy: Predictive analytics and personalized health forecasts heavily depend on the accuracy and completeness of patient data. Missing or outdated information can reduce the effectiveness of predictions.
Limitations in Predictive Health Forecasts: Long-term health predictions are inherently uncertain due to unpredictable lifestyle changes, environmental factors, and genetic variances.

Computations Performed 
Source Code Repository: Github

References
Articles Consulted: 
Operational Research
How can we extend healthcare capacity?
National Library of Medicine
K-Means Clustering: 
Visualisation Source: Visualising K-Means Clustering
Explanation and Visualisation Source: K-Means Clustering Explanation and Visualisation
Images and Videos Used: 
Physical Keychain, Patient Information Display Screens created via - Canva
Wayfinding Tape - Duralabel
K-Means Clustering Image Computed in python - Github
K-Means Clustering Video - Science Buddies: K-Means Algorithm Simple Explanation
Multinational Hospital Group - Staffingly
Web App Concept and Live Load on Sites created using HTML/CSS - Github
Calming Atmosphere, Paper forms with digital system, Express Treatment Centre Concept generated via -  AI Image Generator
Board Games - Wikipedia (King of Tokyo))
Q&A sessions:
Session 1: Video Recording
Session 2: Video Recording
