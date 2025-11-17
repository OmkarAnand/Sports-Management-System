# 🚀 Quick Start Guide

## View Your Database in 3 Easy Ways

### 1️⃣ EASIEST: Django Admin Panel ⭐⭐⭐⭐⭐

**No installation needed!**

```bash
# 1. Start the server
python manage.py runserver

# 2. Open browser
http://127.0.0.1:8000/admin/
```

**Login:**

- Username: `admin`
- Password: `admin123`

**What you'll see:**

- ✅ All users
- ✅ All facilities
- ✅ All bookings
- ✅ Equipment
- ✅ Tournaments
- ✅ Everything!

**Best for:** Daily use, managing data

---

### 2️⃣ VISUAL: DB Browser for SQLite ⭐⭐⭐⭐

**Free download:**

1. **Download**: https://sqlitebrowser.org/
2. **Install** (click through installer)
3. **Open** DB Browser for SQLite
4. **Click** "Open Database"
5. **Navigate** to: `D:\college\Sem 7\INT253 Django\Sports management\db.sqlite3`
6. **Click** Open

**What you'll see:**

- ✅ Visual table browser
- ✅ All your data in tables
- ✅ Can run SQL queries
- ✅ Can export data

**Best for:** Exploring database structure

---

### 3️⃣ QUICK: Python Shell ⭐⭐⭐

**No installation needed!**

```bash
python manage.py shell
```

Then paste this code:

```python
# View all users
from users.models import User
print("=" * 50)
print("USERS:")
print("=" * 50)
for user in User.objects.all():
    print(f"  • {user.username} ({user.role}) - {user.email}")

# View all facilities
from facilities.models import Facility
print("\n" + "=" * 50)
print("FACILITIES:")
print("=" * 50)
for f in Facility.objects.all():
    print(f"  • {f.name}: ${f.hourly_rate}/hr ({f.get_facility_type_display()})")

# View all equipment
from equipment.models import Equipment
print("\n" + "=" * 50)
print("EQUIPMENT:")
print("=" * 50)
for e in Equipment.objects.all():
    print(f"  • {e.name}: ${e.rental_price_per_hour}/hr ({e.quantity_available} available)")

# Summary
from tournaments.models import Tournament
from bookings.models import Booking
print("\n" + "=" * 50)
print("SUMMARY:")
print("=" * 50)
print(f"  Total Users: {User.objects.count()}")
print(f"  Total Facilities: {Facility.objects.count()}")
print(f"  Total Equipment: {Equipment.objects.count()}")
print(f"  Total Tournaments: {Tournament.objects.count()}")
print(f"  Total Bookings: {Booking.objects.count()}")
print("=" * 50)
```

**Exit:**

```
exit()
```

---

## Your Current Database

**Location:** `D:\college\Sem 7\INT253 Django\Sports management\db.sqlite3`

**Contains:**

- 3 Users (including admin)
- 5 Facilities (courts, fields, etc.)
- 5 Equipment items (rackets, balls, etc.)
- 1 Tournament
- Ready for bookings!

---

## Recommended Workflow

**For daily data management:** → Use **Django Admin** (#1)
**For database exploration:** → Use **DB Browser** (#2)  
**For quick checks:** → Use **Python Shell** (#3)

---

## Start Now!

**Just want to see your data?**

```bash
python manage.py runserver
# Then visit: http://127.0.0.1:8000/admin/
```

That's it! 🎉
