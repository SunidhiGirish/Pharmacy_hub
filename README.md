# Pharmacy_hub

## Overview

Pharmacy Hub is a web-based pharmacy management system developed using Python, Flask, HTML, Tailwind CSS, and MySQL Workbench. The system allows users to browse medicines, create accounts, sign in securely, add medicines to their cart, place orders, and submit feedback through an interactive and user-friendly interface.

---

## Features

* User Registration and Login
* Browse Available Medicines
* Medicine Categorization
* Add Medicines to Cart
* Remove Medicines from Cart
* Checkout Functionality
* Order History Tracking
* Feedback Submission
* Responsive User Interface
* Session Management

---

## Technology Stack

### Frontend

* HTML5
* Tailwind CSS

### Backend

* Python
* Flask
* PyMySQL

### Database

* MySQL
* MySQL Workbench

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## Database Tables

### Users

Stores user account information.

### Categories

Stores medicine categories.

### Medicines

Stores medicine information such as:

* Name
* Description
* Price
* Stock Quantity
* Category
* Image URL

### Feedback

Stores user feedback and reviews.

---

## Project Structure

```text
Pharmacy_hub/
│
├── app.py
├── requirements.txt
├── pharmacy.sql
│
├── templates/
│   ├── index.html
│   ├── medicines.html
│   ├── signin.html
│   ├── signup.html
│   ├── cart.html
│   ├── checkout.html
│   ├── orderhistory.html
│   └── feedback.html
│
├── static/
│   └── images/
│
└── README.md
```

---

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SunidhiGirish/Pharmacy_hub.git
```

### Step 2: Navigate to Project Directory

```bash
cd Pharmacy_hub
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Install MySQL Workbench

Download and install MySQL Workbench:

https://dev.mysql.com/downloads/workbench/

### Step 5: Create Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE pharmacy_hubs;
```

### Step 6: Import Database

Import the provided `pharmacy.sql` file into MySQL Workbench.

### About pharmacy.sql

The project includes a database script file named **pharmacy.sql**.

This file contains all SQL queries required to set up the Pharmacy Hub database. It includes:

* Database creation queries
* Table creation queries
* Primary Key and Foreign Key constraints
* Sample category data
* Sample medicine data with image URLs

The script automatically creates and configures the following tables:

#### Users

Stores user registration and login information.

#### Categories

Stores medicine category information.

#### Medicines

Stores medicine details including:

* Medicine Name
* Description
* Price
* Stock Quantity
* Category ID
* Image URL

#### Feedback

Stores customer feedback submitted through the application.

After importing `pharmacy.sql`, all required tables and sample records will be created automatically, making the application ready to run without additional database setup.

The `pharmacy.sql` file is included in this repository so that anyone cloning the project can easily recreate the complete database structure and sample data.

### Step 7: Configure Database Connection

Update database credentials inside `app.py` if required:

```python
host="localhost"
user="root"
password="your_password"
database="pharmacy_hubs"
```

### Step 8: Run the Application

```bash
python app.py
```

### Step 9: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

This project helped in understanding:

* Flask Web Application Development
* Database Connectivity using PyMySQL
* CRUD Operations
* User Authentication and Session Management
* Frontend Development using HTML and Tailwind CSS
* Database Design and Management using MySQL Workbench
* Git and GitHub Version Control

---

## Future Enhancements

* Online Payment Gateway Integration
* Advanced Search and Filtering
* Admin Dashboard
* Order Tracking System
* Email Notifications
* Password Encryption
* Inventory Management Module
---

