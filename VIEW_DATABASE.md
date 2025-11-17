# 📊 How to View Your SQLite Database

## Method 1: Browser-Based Tool (Recommended for Beginners)

### DB Browser for SQLite (SQLiteStudio alternative)

#### Download & Install:

1. **Visit**: https://sqlitebrowser.org/
2. **Download**: DB Browser for SQLite (Free, open-source)
3. **Install** with default settings

#### Usage:

1. Open **DB Browser for SQLite**
2. Click **"Open Database"**
3. Navigate to your project folder:
   ```
   D:\college\Sem 7\INT253 Django\Sports management\db.sqlite3
   ```
4. Click **"Open"**
5. You'll see all your tables!

#### Features:

- ✅ Browse tables visually
- ✅ View/edit data
- ✅ Run SQL queries
- ✅ Export data to CSV/JSON
- ✅ Search across all tables
- ✅ Free and user-friendly

---

## Method 2: VS Code Extension

### Install SQLite Extension in VS Code:

#### Steps:

1. Open VS Code
2. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac)
3. Search for: **"SQLite"**
4. Install: **"SQLite Viewer"** by qwtel or **"SQLite"** by alexcvzz
5. Open your `db.sqlite3` file in VS Code
6. View your data in the sidebar!

#### Features:

- ✅ View within VS Code
- ✅ Run queries
- ✅ Edit data
- ✅ No separate app needed

---

## Method 3: Online SQLite Viewer

### Options:

1. **SQLite Viewer** (https://sqliteviewer.app/)

   - Upload `db.sqlite3`
   - View tables and run queries
   - No installation needed

2. **DBFSQLite.com** (https://dbfsqlite.com/)
   - Simple and free
   - Upload and browse

---

## Method 4: Command Line (Advanced)

### Using Python:

```bash
# Activate virtual environment first
venv\Scripts\activate

# Enter Python shell
python

# Import and use
>>> import sqlite3
>>> conn = sqlite3.connect('db.sqlite3')
>>> cursor = conn.cursor()
>>> cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
>>> print(cursor.fetchall())
```

### Using sqlite3 Command:

```bash
# Open database
sqlite3 db.sqlite3

# View all tables
.tables

# View data from a table
SELECT * FROM users_user;

# Exit
.exit
```

---

## Method 5: Django Shell (Python-based)

### Quick Query:

```bash
python manage.py shell
```

Then in Python:

```python
# View all users
from users.models import User
for user in User.objects.all():
    print(f"{user.username} - {user.role}")

# View facilities
from facilities.models import Facility
for facility in Facility.objects.all():
    print(f"{facility.name}: ${facility.hourly_rate}/hr")

# Count records
print(f"Total users: {User.objects.count()}")
```

### Exit shell:

```
exit()
```

---

## Method 6: Django Admin Panel (Easiest!)

### Steps:

1. **Start the server**:

   ```bash
   python manage.py runserver
   ```

2. **Visit**:

   ```
   http://127.0.0.1:8000/admin/
   ```

3. **Login** with your admin credentials:

   - Username: `admin`
   - Password: `admin123`

4. **Browse all models**:
   - Users
   - Facilities
   - Bookings
   - Equipment
   - Tournaments
   - etc.

#### Features:

- ✅ No extra software needed
- ✅ User-friendly interface
- ✅ Add/edit/delete records
- ✅ Filter and search
- ✅ See related objects

---

## Quick Comparison

| Method                | Difficulty    | Best For        | Installation      |
| --------------------- | ------------- | --------------- | ----------------- |
| **Django Admin**      | ⭐ Easiest    | Regular use     | None (built-in)   |
| **DB Browser**        | ⭐⭐ Easy     | Visual browsing | Download app      |
| **VS Code Extension** | ⭐⭐ Easy     | Developers      | VS Code extension |
| **Online Viewer**     | ⭐ Easy       | Quick check     | None              |
| **Command Line**      | ⭐⭐⭐⭐ Hard | Advanced users  | SQLite built-in   |

---

## Recommended Workflow

### Daily Use:

✅ **Use Django Admin Panel** (http://127.0.0.1:8000/admin/)

- Best for managing data
- Most intuitive
- Already integrated

### Database Inspection:

✅ **Use DB Browser for SQLite**

- Perfect for exploring structure
- Run custom queries
- Export data

### Quick Checks:

✅ **Use VS Code Extension** (if using VS Code)

- Fast and convenient
- Right in your editor

---

## Viewing Your Current Data

### Quick Check with Django:

```bash
python manage.py runserver
```

Then visit:

- **Admin Panel**: http://127.0.0.1:8000/admin/

You'll see:

- Users (including admin user)
- 5 Facilities
- 5 Equipment items
- 1 Tournament

### Check via Python Shell:

```bash
python manage.py shell
```

Then run:

```python
from users.models import User
from facilities.models import Facility
from equipment.models import Equipment

# Count records
print(f"Users: {User.objects.count()}")
print(f"Facilities: {Facility.objects.count()}")
print(f"Equipment: {Equipment.objects.count()}")

# View specific data
print("\nFacilities:")
for f in Facility.objects.all():
    print(f"  - {f.name}: ${f.hourly_rate}/hr")

print("\nEquipment:")
for e in Equipment.objects.all():
    print(f"  - {e.name}: {e.quantity_available} available")
```

---

## SQLite Table Structure

Your database contains these main tables:

### Users & Auth:

- `users_user` - All users (members, admins, coaches)
- `auth_user_groups` - User groups
- `auth_user_user_permissions` - Permissions

### Facilities:

- `facilities_facility` - Sports facilities
- `facilities_facilityavailability` - Availability schedules

### Bookings:

- `bookings_booking` - Facility bookings
- `bookings_bookinghistory` - Booking changes

### Equipment:

- `equipment_equipment` - Equipment items
- `equipment_rental` - Equipment rentals

### Memberships:

- `memberships_membershipplan` - Membership plans
- `memberships_membershipsubscription` - User subscriptions

### Tournaments:

- `tournaments_tournament` - Tournaments
- `tournaments_team` - Teams
- `tournaments_match` - Matches

### Payments:

- `payments_payment` - Payment transactions
- `payments_paymenthistory` - Payment history

### Notifications:

- `notifications_notification` - User notifications
- `notifications_emaillog` - Email logs

---

## Sample Queries

### Using Django Shell:

```python
python manage.py shell

# View all facilities
from facilities.models import Facility
for f in Facility.objects.all():
    print(f"{f.name}: ${f.hourly_rate}/hr")

# Count bookings
from bookings.models import Booking
print(f"Total bookings: {Booking.objects.count()}")

# Find admin users
from users.models import User
admins = User.objects.filter(role='admin')
for admin in admins:
    print(f"Admin: {admin.username}")
```

### Using SQL:

```sql
-- View all users
SELECT username, email, role FROM users_user;

-- Count facilities by type
SELECT facility_type, COUNT(*) as count
FROM facilities_facility
GROUP BY facility_type;

-- View bookings with facility names
SELECT
    b.id,
    u.username,
    f.name as facility,
    b.booking_date,
    b.total_cost
FROM bookings_booking b
JOIN users_user u ON b.user_id = u.id
JOIN facilities_facility f ON b.facility_id = f.id;
```

---

## Troubleshooting

### "Database is locked"

**Solution**: Close Django server and reopen DB Browser

### "Cannot open database"

**Solution**:

1. Check file path
2. Make sure file exists
3. Check file permissions

### "Permission denied"

**Solution**:

1. Stop Django server
2. Close any other apps using the database
3. Try again

---

## Quick Start Guide

**For immediate viewing:**

1. **Easiest**: Use Django Admin

   ```
   python manage.py runserver
   # Visit: http://127.0.0.1:8000/admin/
   ```

2. **Best for browsing**: Use DB Browser for SQLite

   ```
   Download from: https://sqlitebrowser.org/
   Open: db.sqlite3
   ```

3. **Fast check**: Use Python shell
   ```bash
   python manage.py shell
   >>> from facilities.models import Facility
   >>> Facility.objects.all()
   ```

---

**Recommended**: Start with Django Admin Panel - it's the easiest and most user-friendly! 🎯
