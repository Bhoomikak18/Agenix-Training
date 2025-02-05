# Subscriber Churn Prediction - Data Model Overview 

## Overview
This project focuses on designing a **database model for churn prediction** in a subscription-based streaming service. The model tracks **user activity, subscriptions, payments, cancellations, content interactions, and support interactions** to analyze patterns leading to churn.

The **goal** is to identify users likely to cancel their subscriptions by analyzing their interactions, payments, and support requests.

---

## 1. Conceptual Data Model  

The conceptual model represents the high-level structure of the database, showing the relationships between entities without focusing on implementation details.  

### Entities and Relationships:  
- **Users** → `Has` → **Subscriptions** (1:N)  
- **Users** → `Makes` → **Payments** (1:N)  
- **Users** → `Watches` → **Content** (N:N via ActivityLogs)  
- **Users** → `Contacts` → **SupportInteractions** (1:N)  
- **Subscriptions** → `Initiates` → **Payments** (1:N)  
- **Subscriptions** → `Is Cancellation Called` → **Cancellations** (1:0..1)  
- **ActivityLogs** → `Refers To` → **Content** (N:1)  

---

## 2. Logical Data Model  

The logical model defines the attributes for each entity and the foreign keys without implementing database-specific details.  

### Users  
- `UserID (PK)`  
- Name  
- Email  
- PhoneNo  
- Country  
- DOB  
- LastLogin_Date  
- Preferred_Lang  
- Emails_Ignored_Count  

### Subscriptions  
- `Subscription_ID (PK)`  
- `UserID (FK)`  
- Plan_Type  
- Start_Date  
- End_Date  
- Renewal_Status  
- Previous_Plan  

### Payments  
- `Payment_ID (PK)`  
- `UserID (FK)`  
- `Subscription_ID (FK)`  
- Payment_Date  
- Payment_Amount  
- Payment_Method  
- Payment_Status  

### Cancellations  
- `Cancellation_ID (PK)`  
- `Subscription_ID (FK)`  
- Cancellation_Date  
- Is_PromoUsed
- Refund_Requested
- Refund_ProcessedDate  
- Refund_Status
- Refund_Amount  

### Content  
- `Content_ID (PK)`  
- Title  
- Genre  
- Duration  
- Release_Date  
- Language  
- Content_Type  

### **ActivityLogs**  
- `LogID (PK)`  
- `UserID (FK)`  
- `Content_ID (FK)`  
- Watched_Date  
- Watch_Duration  
- Is_Completed  
- Device_Type  
- Rating  

### SupportInteractions  
- `Support_ID (PK)`  
- `UserID (FK)`  
- Interaction_Date  
- Issue_Type  
- Resolution_Status  

---

## 3. Physical Data Model  

The physical model converts the logical design into a database schema with SQL implementation.  

### SQL Table Definitions  
```sql
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    PhoneNo VARCHAR(20),
    Country VARCHAR(100),
    DOB DATE,
    LastLogin_Date DATETIME,
    Preferred_Lang VARCHAR(50),
    Emails_Ignored_Count INT
);

CREATE TABLE Subscriptions (
    Subscription_ID INT PRIMARY KEY,
    UserID INT,
    Plan_Type VARCHAR(100),
    Start_Date DATE,
    End_Date DATE,
    Renewal_Status VARCHAR(50),
    Previous_Plan VARCHAR(100),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Payments (
    Payment_ID INT PRIMARY KEY,
    UserID INT,
    Subscription_ID INT,
    Payment_Date DATE,
    Payment_Amount DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Payment_Status VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (Subscription_ID) REFERENCES Subscriptions(Subscription_ID)
);

CREATE TABLE Cancellations (
    Cancellation_ID INT PRIMARY KEY,
    Subscription_ID INT,
    Cancellation_Date DATE,
    Is_PromoUsed BOOLEAN,
    Refund_Status VARCHAR(50),
    Refund_Requested BOOLEAN,
    Refund_ProcessedDate DATE,
    Refund_Amount DECIMAL(10,2),
    FOREIGN KEY (Subscription_ID) REFERENCES Subscriptions(Subscription_ID)
);

CREATE TABLE Content (
    Content_ID INT PRIMARY KEY,
    Title VARCHAR(255),
    Genre VARCHAR(100),
    Duration INT,
    Release_Date DATE,
    Language VARCHAR(50),
    Content_Type VARCHAR(50)
);

CREATE TABLE ActivityLogs (
    LogID INT PRIMARY KEY,
    UserID INT,
    Content_ID INT,
    Watched_Date DATETIME,
    Watch_Duration INT,
    Is_Completed BOOLEAN,
    Device_Type VARCHAR(50),
    Rating INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (Content_ID) REFERENCES Content(Content_ID)
);

CREATE TABLE SupportInteractions (
    Support_ID INT PRIMARY KEY,
    UserID INT,
    Interaction_Date DATETIME,
    Issue_Type VARCHAR(255),
    Resolution_Status VARCHAR(100),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
```
## How This Model Helps in Churn Prediction  

The goal of this database is to **predict subscriber churn** by analyzing user behavior, payments, cancellations, and engagement.  

## Churn Indicators in the Model  

### 1. Subscription Status  
- Users with expired `End_Date` and no `Renewal_Status = Active` are at churn risk.  

### 2. Payment Failures  
- Users with many `Payment_Status = Failed` may churn.  

### 3. Low Engagement  
- Users with low `Watch_Duration` or few `ActivityLogs` → Potential churners  
- Users who watch less content (low `Is_Completed` rate) → Disengaged users  

### 4. Support Issues  
- Many SupportInteractions with `Resolution_Status = Unresolved` → High churn probability  

### 5. Cancellations & Refunds  
- Users who requested refunds (`Refund_Requested = TRUE`) are at high risk of not returning.  

---


## User Behavior Tracking:
- `ActivityLogs` captures what content users watch and for how long.
- `SupportInteractions` records user complaints and resolutions.
- `LastLoginDate` helps detect inactive users.

## Subscription & Payment Analysis:
- `Subscriptions` show renewal patterns.
- `Payments` track successful and failed transactions.
- `Cancellations` provide insights into refund requests and plan downgrades.

## Predicting Churn:
- High support interactions + low engagement → High churn risk.
- Frequent cancellations + refund requests → Users likely to leave.
- No recent activity + no payment renewal → Inactive users at risk.

## Conclusion  

This ER model provides a structured way to manage and analyze subscriber data for churn prediction.  

### Key Strengths:  
1. Tracks user activity, payments, and engagement metrics.  
2. Predicts churn based on payment failures, low activity, and cancellations.  
3. Can be extended to include AI-based personalization and retention strategies.  
