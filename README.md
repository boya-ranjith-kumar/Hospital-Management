# **Hospital Patient Management System**

A simple console-based application built using Python and MySQL to manage hospital patient records efficiently. The system provides separate functionalities for Admin and Patient (User).
Features

## 👨‍⚕️ **Admin Panel**  
Add new patient  
Check berth availability  
View patient details  
Update berth number  
Delete patient record  
Check fee details  

## 👤 **Patient Panel**
Get admission number  
Check berth number  
View pending fee  
Make payment  

## **Technologies Used**
- Python
- MySQL
- mysql-connector

## **Project Structure**
project_folder/  
│── main.py  
│── admin.py  
│── admin_features.py  
│── patient.py  
│── patient_features.py  
│── db_connection.py  
└── database (MySQL Tables)

## **Database Details**
**Database Name:** pdbc  
**Tables:**  
patients – stores patient details  
berths – stores berth availability  

## **OBJECTIVES**
• To automate patient admission process.  
• To manage berth allocation effectively.  
• To maintain patient records in a structured database.  
• To track total, paid, and pending fees.  
• To provide user-friendly admin and patient panels.

## **Sample Output**
### **Berth Status**  
Berth 1: Occupied  
Berth 2: Available  
Berth 3: Available

### **Fee Details**
Total Fee - 5000  
Amount Paid - 3000  
Pending Fee - 2000  

## **Conclusion :**
This project demonstrates how Python integrates with MySQL to build a basic patient management system and helps in understanding backend development and database operations.
