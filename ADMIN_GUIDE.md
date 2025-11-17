# 🔐 Admin vs Member Roles Guide

## Role Differences

### 🔹 Member (Default Role)
- **Access Level**: Standard user
- **Capabilities**:
  - ✅ Browse facilities
  - ✅ View equipment
  - ✅ Check tournaments
  - ✅ Book facilities
  - ✅ Rent equipment
  - ✅ View own bookings
  - ✅ Manage profile
  - ❌ No access to Admin Dashboard
  - ❌ No access to Django Admin
  - ❌ Cannot manage other users
  - ❌ Cannot create facilities/equipment/tournaments

### 🔹 Admin Role
- **Access Level**: Full administrative access
- **Capabilities**:
  - ✅ All Member capabilities, PLUS:
  - ✅ **Admin Dashboard** - View analytics, statistics, revenue
  - ✅ **Django Admin Panel** - Full CRUD operations
  - ✅ Manage all users
  - ✅ Create/edit/delete facilities
  - ✅ Create/edit/delete equipment
  - ✅ Create/edit/delete tournaments
  - ✅ View all bookings across the platform
  - ✅ Generate reports
  - ✅ Manage system settings

### 🔹 Coach Role
- **Access Level**: Special privileges (similar to Member for now)
- **Future Enhancements**:
  - Manage teams
  - Schedule training sessions
  - View team statistics
  - Coordinate tournaments

## How to Create an Admin User

### Method 1: Via Django Admin Panel
1. Start the server: `python manage.py runserver`
2. Visit: http://127.0.0.1:8000/admin/
3. Login with your superuser credentials
4. Go to **Users** → Click on the user
5. Check **Role** = "Admin"
6. Make sure **Staff status** is checked (for Django Admin access)
7. Save

### Method 2: Via Shell
```bash
python manage.py shell
```

```python
from users.models import User

# Create admin user
admin = User.objects.create_user(
    username='admin_user',
    email='admin@example.com',
    password='your_password',
    role='admin'
)
admin.is_staff = True
admin.is_superuser = True  # Optional: for Django admin access
admin.save()

print(f"Admin user created: {admin.username}")
```

### Method 3: Change Existing User to Admin
```bash
python manage.py shell
```

```python
from users.models import User

# Find user
user = User.objects.get(username='existing_user')

# Make them admin
user.role = 'admin'
user.is_staff = True  # Enables Django Admin access
user.save()

print(f"User {user.username} is now an admin")
```

## Accessing Admin Features

### Admin Dashboard
- **URL**: http://127.0.0.1:8000/dashboard/
- **What you'll see**:
  - Total users count
  - Total bookings
  - Tournament count
  - Revenue statistics
  - Recent bookings list

### Django Admin Panel
- **URL**: http://127.0.0.1:8000/admin/
- **What you can do**:
  - Manage all models (Users, Facilities, Bookings, etc.)
  - Add/edit/delete records
  - Filter and search data
  - View history of changes

## Testing Role Differences

### Test Member Role:
1. Register a new user (default role is 'member')
2. Login
3. Notice: No "Admin Dashboard" in menu
4. Can book facilities, rent equipment

### Test Admin Role:
1. Login as admin user
2. Notice: "Admin Dashboard" appears in dropdown menu
3. Click "Admin Dashboard" to see statistics
4. Click on profile name → "Admin Dashboard" (if you have is_staff=True)
5. Access Django Admin panel at /admin/

## Current Permissions Matrix

| Feature | Member | Admin | Coach |
|---------|--------|-------|-------|
| View Facilities | ✅ | ✅ | ✅ |
| Book Facilities | ✅ | ✅ | ✅ |
| Rent Equipment | ✅ | ✅ | ✅ |
| View Tournaments | ✅ | ✅ | ✅ |
| Manage Profile | ✅ | ✅ | ✅ |
| Admin Dashboard | ❌ | ✅ | ❌ |
| Django Admin | ❌ | ✅ (if staff) | ❌ |
| Create Facilities | ❌ | ✅ | ❌ |
| Manage Users | ❌ | ✅ | ❌ |
| View All Bookings | ❌ | ✅ | ❌ |
| System Reports | ❌ | ✅ | ❌ |

## Important Notes

1. **is_staff vs role='admin'**:
   - `is_staff` = Django Admin panel access
   - `role='admin'` = Admin Dashboard access + admin features
   - For full admin powers, set BOTH to True

2. **Security**:
   - Admin users should have strong passwords
   - Change default admin password in production
   - Regularly review admin user list

3. **Best Practice**:
   - Create separate admin accounts
   - Don't use your personal account as admin
   - Use the default 'admin' user for initial setup only

## Troubleshooting

### "I can't see Admin Dashboard"
**Solution**: Make sure your user has `role='admin'` or `is_staff=True`

### "I can login but can't access Django Admin"
**Solution**: Set `is_staff=True` on your user account

### "How do I check my current role?"
**Solution**: 
1. Login to your account
2. Go to Profile page
3. Check the role field

Or via shell:
```python
from users.models import User
user = User.objects.get(username='your_username')
print(f"Role: {user.role}, is_staff: {user.is_staff}")
```

---

**Need more help?** Check the main README.md for general setup instructions!

