
# PEPLUM HOME SERVICES

unexpected car breakdown? unfortunate pipe leakage? don't know who to call? we got you covered!

A full stack home services booking platform that connects customers with trusted service providers for home-based services.

Customers can browse services, schedule appointments, and pay after successful completion of work, while service providers can register, manage availability, and receive appointments.

---

## Project Overview

PEPLUM Home Services is designed to simplify booking and managing household services through a modern web platform.

The platform supports two user roles:

* Customer
* Service Provider

The system includes appointment booking, provider approval, availability management, and post-service payment workflow.

---

## Features

| Module                 | Functionality                       |
| ---------------------- | ----------------------------------- |
| Authentication         | Customer and Provider registrations  |
| Service Booking        | Customers can schedule appointments |
| Provider Registration  | Service providers can apply         |
| Availability           | Providers manage availability       |
| Appointment Management | Track booking status                |
| Payment Workflow       | Payment after service completion    |
| Admin Panel            | Approve providers and manage data   |
| Database Storage       | Persistent data using Django        |

---

## Services Available

| Category    | Description                      |
| ----------- | -------------------------------- |
| Mechanic    | Home vehicle assistance          |
| Plumbing    | Plumbing repair and installation |
| Electrician | Electrical maintenance           |
| Cleaning    | Residential cleaning services    |
| Cooking     | Home cooking services            |

---

## Technology Stack

| Layer           | Technology   |
| --------------- | ------------ |
| Frontend        | HTML5        |
| Styling         | CSS3         |
| Client Logic    | JavaScript   |
| Backend         | Python       |
| Framework       | Django       |
| Database        | SQLite       |
| Media Handling  | Pillow       |
| Version Control | Git + GitHub |

---

## Project Structure

```plaintext
peplum-home-services/

core/
users/
services/
bookings/

templates/
static/
media/

manage.py
requirements.txt
README.md
```

---

## User Flow

```plaintext
Customer
↓

Register / Login
↓

Browse Services
↓

Choose Provider
↓

Book Appointment
↓

Provider Accepts
↓

Service Completed
↓

Customer Pays
```

---

## Installation

### 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Move Into Project

```bash
cd peplum-home-services
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

### 6. Start Server

```bash
python manage.py runserver
```

Open:

```plaintext
http://127.0.0.1:8000
```

---

## Admin Panel

Open:

```plaintext
http://127.0.0.1:8000/admin
```

Admin capabilities:

* Approve providers
* Manage bookings
* Monitor services
* Update appointment status

---

## Database Design

### Users

| Field    |
| -------- |
| Username |
| Email    |
| Phone    |
| Role     |

### Providers

| Field        |
| ------------ |
| Name         |
| Service      |
| Experience   |
| Availability |
| Approval     |

### Bookings

| Field          |
| -------------- |
| Customer       |
| Provider       |
| Date           |
| Time           |
| Payment Status |

---

## Future Improvements

* Online payment gateway
* Live availability tracking
* Provider ratings
* Customer reviews
* Notifications
* Service analytics
* Mobile application

---

## Author

Developed as a full stack web application project using Django and modern web technologies.

---

## License

This project is available for educational and development purposes.
