# 🏆 Sports Facility Booking & Tournament Management Platform

A full-stack web platform for **sports facility bookings**, **equipment rentals**, **membership management**, and **league/tournament organization**.  
Built entirely with **Django** (backend + frontend), the platform simplifies booking, scheduling, and managing sports events for clubs, gyms, or universities.

## 📋 Features

### ✅ Core Features Implemented

- **🏟️ Facility & Court Management** - Create and manage sports facilities with real-time availability
- **📅 Booking System** - Members can book courts with conflict prevention
- **🏸 Equipment Rental** - Manage and rent sports equipment
- **💳 Membership Management** - Subscription-based membership plans
- **🏆 League & Tournament Organization** - Create tournaments with teams and matches
- **💰 Payments & Billing** - Payment system integration ready
- **🔔 Notifications** - Email and in-app notification system
- **🧑‍💼 Admin Dashboard** - Comprehensive admin panel with analytics

## 🧱 Technology Stack

| Category | Technology |
|----------|------------|
| **Backend & Frontend** | Django (with Template System) |
| **Database** | SQLite (default) / PostgreSQL |
| **Authentication** | Django's built-in auth system |
| **Styling** | Tailwind CSS (CDN) |
| **Icons** | Font Awesome |

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Steps

1. **Clone or navigate to the project directory**
```bash
cd "D:\college\Sem 7\INT253 Django\Sports management"
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Visit the application**
Open your browser and go to: **http://127.0.0.1:8000/**

## 🗂️ Project Structure

```
Sports management/
│
├── manage.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
├── facilities/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── bookings/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── equipment/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── memberships/
│   ├── models.py
│   └── admin.py
├── tournaments/
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── payments/
│   ├── models.py
│   └── admin.py
├── notifications/
│   ├── models.py
│   └── admin.py
├── dashboard/
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── users/
│   ├── facilities/
│   ├── bookings/
│   ├── equipment/
│   ├── tournaments/
│   └── dashboard/
├── static/
├── requirements.txt
├── README.md
└── README_Django_HTML.md
```

## 🔐 Default Credentials

After creating a superuser, you can login to the admin panel at:
- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin (or whatever you created)
- **Password**: admin123 (or whatever you set)

## 📡 Key URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/login/` | Login page |
| `/users/register/` | User registration |
| `/facilities/` | List all facilities |
| `/bookings/my-bookings/` | View user bookings |
| `/equipment/` | List equipment |
| `/tournaments/` | List tournaments |
| `/dashboard/` | Admin dashboard |
| `/admin/` | Django admin panel |

## 🎨 UI Features

- **Modern & Responsive Design** - Tailwind CSS for beautiful UI
- **User-Friendly Navigation** - Clean and intuitive interface
- **Color-Coded Status** - Visual indicators for bookings, tournaments, etc.
- **Mobile-Friendly** - Responsive grid layouts
- **Interactive Elements** - Hover effects and transitions

## 🚀 Quick Start Guide

1. **Setup the project** (follow installation steps above)
2. **Create admin account** to manage the platform
3. **Add facilities** via admin panel or shell
4. **Create sample data** for testing
5. **Register users** to test booking functionality

### Sample Data Creation

You can add sample data via the admin panel or Django shell:

```bash
python manage.py shell
```

```python
from facilities.models import Facility
from users.models import User

# Create a facility
facility = Facility.objects.create(
    name="Basketball Court 1",
    facility_type="basketball",
    description="Indoor basketball court with AC",
    hourly_rate=50.00,
    capacity=10
)

print("Sample facility created!")
```

## 🔒 Security Features

- Django's built-in authentication (hashed passwords)
- CSRF protection enabled by default
- Role-based access control
- Secure password validation

## 📝 Admin Features

The admin panel provides:
- User management
- Facility & availability management
- Booking oversight
- Equipment inventory management
- Tournament organization
- Payment tracking
- Analytics dashboard

## 🎯 Testing the Application

1. **Login** as admin: http://127.0.0.1:8000/admin/
2. **Add facilities** - Create courts, fields, gyms
3. **Register a regular user** - http://127.0.1:8000/users/register/
4. **Book a facility** - Navigate to facilities and create booking
5. **Check bookings** - View and manage reservations
6. **Explore tournaments** - Check tournament listings

## 🔮 Future Enhancements

- Razorpay/Stripe payment integration
- Email notifications via SendGrid
- SMS notifications via Twilio
- Mobile app (React Native)
- AI-based booking recommendations
- Live score tracking
- Multi-language support

## 🐛 Troubleshooting

### Issue: "No module named 'venv'"
**Solution**: Make sure you've activated the virtual environment properly.

### Issue: "ModuleNotFoundError: No module named 'Pillow'"
**Solution**: Run `pip install Pillow` or `pip install -r requirements.txt`

### Issue: Database locked
**Solution**: Make sure no other process is using the SQLite database file.

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` if using production mode.

## 📞 Contact

**Kumar Ankesh**  
*Full Stack Developer (Django + MERN)*  
📧 kumarankesh1894@gmail.com

## 📄 License

This project is licensed under the **MIT License**.

---

> _"Play smarter, not harder — manage your sports world efficiently!"_

## 🎉 Getting Started

The platform is ready to use! Start the server and begin managing your sports facilities today.

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** to explore!

