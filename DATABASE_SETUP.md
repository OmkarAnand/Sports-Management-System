# 🗄️ Database Setup Guide

## Current Database: SQLite

**Default Configuration**: `db.sqlite3` (already set up and working!)

### SQLite Characteristics:

- ✅ **No installation needed** - Comes with Python
- ✅ **Perfect for development** - Fast and simple
- ✅ **Single file** - Easy to backup
- ✅ **Zero configuration** - Works out of the box
- ⚠️ **Not recommended for production** - Limited concurrency
- 📍 **Location**: `D:\college\Sem 7\INT253 Django\Sports management\db.sqlite3`

## Switching to PostgreSQL (Production-Ready)

### Step 1: Install PostgreSQL

1. Download from: https://www.postgresql.org/download/
2. Install with default settings
3. Remember your postgres password

### Step 2: Create Database

Open PostgreSQL command line (psql) and run:

```sql
CREATE DATABASE sports_management;
CREATE USER sports_user WITH PASSWORD 'your_secure_password';
ALTER ROLE sports_user SET client_encoding TO 'utf8';
ALTER ROLE sports_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sports_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sports_management TO sports_user;
```

### Step 3: Install psycopg2

```bash
pip install psycopg2-binary
```

_(Already in requirements.txt!)_

### Step 4: Configure Django Settings

Create a `.env` file from `env.example`:

```bash
# Copy the example
copy env.example .env  # Windows
# or
cp env.example .env     # Linux/Mac
```

Edit `.env` file:

```env
DATABASE_NAME=sports_management
DATABASE_USER=sports_user
DATABASE_PASSWORD=your_secure_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### Step 5: Update Django Settings

Modify `core/settings.py`:

```python
import os
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='5432'),
    }
}
```

**Don't forget to**:

1. Install python-decouple: `pip install python-decouple`
2. Add to settings.py:
   ```python
   from decouple import config
   ```

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Load Sample Data

```bash
python create_sample_data.py  # (if you recreated this)
```

## Switching to MySQL

### Step 1: Install MySQL

```bash
# Ubuntu/Debian
sudo apt-get install mysql-server

# Windows
# Download from: https://dev.mysql.com/downloads/installer/

# macOS
brew install mysql
```

### Step 2: Create Database

```sql
CREATE DATABASE sports_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'sports_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON sports_management.* TO 'sports_user'@'localhost';
FLUSH PRIVILEGES;
```

### Step 3: Install MySQL Client

```bash
pip install mysqlclient
```

Or add to `requirements.txt`:

```
mysqlclient==2.1.1
```

### Step 4: Configure Django Settings

Update `.env`:

```env
DATABASE_NAME=sports_management
DATABASE_USER=sports_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

Update `core/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='3306'),
    }
}
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Database Comparison

| Feature              | SQLite              | PostgreSQL    | MySQL         |
| -------------------- | ------------------- | ------------- | ------------- |
| **Setup Complexity** | ⭐ Easiest          | ⭐⭐ Moderate | ⭐⭐ Moderate |
| **Production Ready** | ❌ No               | ✅ Yes        | ✅ Yes        |
| **Concurrent Users** | Low                 | High          | High          |
| **Performance**      | Good (small DB)     | Excellent     | Excellent     |
| **Full-text Search** | Basic               | Advanced      | Advanced      |
| **JSON Support**     | ✅ Yes              | ✅ Yes        | ✅ Yes        |
| **Cost**             | Free                | Free          | Free          |
| **Best For**         | Development/Testing | Production    | Production    |

## Current Database Info

**Database Type**: SQLite  
**File Location**: `db.sqlite3`  
**Size**: Check with: `dir db.sqlite3` (Windows)  
**Tables Created**:

- users_user
- facilities_facility
- facilities_facilityavailability
- bookings_booking
- bookings_bookinghistory
- equipment_equipment
- equipment_rental
- memberships_membershipplan
- memberships_membershipsubscription
- tournaments_tournament
- tournaments_team
- tournaments_match
- payments_payment
- payments_paymenthistory
- notifications_notification
- notifications_emaillog

## Backing Up Your Database

### SQLite Backup:

```bash
# Simple copy
copy db.sqlite3 backup.db  # Windows
cp db.sqlite3 backup.db     # Linux/Mac

# Or use Django's dumpdata
python manage.py dumpdata > data.json
```

### PostgreSQL Backup:

```bash
pg_dump sports_management > backup.sql

# Restore
psql sports_management < backup.sql
```

### MySQL Backup:

```bash
mysqldump -u sports_user -p sports_management > backup.sql

# Restore
mysql -u sports_user -p sports_management < backup.sql
```

## Resetting the Database

### SQLite:

```bash
# Delete the database
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/Mac

# Recreate
python manage.py migrate
python manage.py createsuperuser
```

### PostgreSQL:

```bash
# Drop and recreate
psql -U sports_user -d postgres
DROP DATABASE sports_management;
CREATE DATABASE sports_management;
\q

# In Django project
python manage.py migrate
python manage.py createsuperuser
```

## Recommended Setup

### For Development:

✅ **SQLite** - Perfect choice!

- Fast setup
- No configuration
- Already working

### For Production:

✅ **PostgreSQL** - Industry standard

- Open source
- Excellent performance
- Great Django support
- Most popular choice for Django apps

### For Enterprise:

✅ **PostgreSQL or MySQL**

- Both work excellently with Django
- PostgreSQL preferred by Django community
- MySQL has better Windows GUI tools (MySQL Workbench)

## Current Configuration

**You're using SQLite**, which is perfect for:

- ✅ Learning Django
- ✅ Development
- ✅ Small projects
- ✅ Testing
- ✅ Academic projects

**No action needed** unless you're deploying to production!

## Troubleshooting

### Issue: `psycopg2` won't install

**Solution**:

```bash
# Windows
pip install psycopg2-binary

# Or use pre-compiled wheel from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg2
```

### Issue: MySQL client won't install

**Solution**:

```bash
# Install MySQL development libraries first
# Ubuntu: sudo apt-get install libmysqlclient-dev
# Windows: Download MySQL Connector C
```

### Issue: Database locked (SQLite)

**Solution**: Close all connections (stop Django server, close DB browser apps)

---

**Current Status**: ✅ Using SQLite - Perfect for development!

Need to switch databases? Follow the steps above! 🚀
