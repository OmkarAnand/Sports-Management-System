#!/usr/bin/env python
"""
Simple script to view database contents
Run: python view_data.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import User
from facilities.models import Facility
from equipment.models import Equipment
from tournaments.models import Tournament
from bookings.models import Booking

def display_data():
    print("=" * 70)
    print(" " * 20 + "DATABASE OVERVIEW")
    print("=" * 70)
    
    # Users
    print("\n👥 USERS:")
    print("-" * 70)
    for user in User.objects.all():
        print(f"  • {user.username:15} | {user.role:8} | {user.email}")
    
    # Facilities
    print("\n🏟️  FACILITIES:")
    print("-" * 70)
    for f in Facility.objects.all():
        print(f"  • {f.name:30} | ${f.hourly_rate:6.2f}/hr | {f.get_facility_type_display():15}")
    
    # Equipment
    print("\n🏸 EQUIPMENT:")
    print("-" * 70)
    for e in Equipment.objects.all():
        print(f"  • {e.name:30} | ${e.rental_price_per_hour:6.2f}/hr | {e.quantity_available:3} available")
    
    # Tournaments
    print("\n🏆 TOURNAMENTS:")
    print("-" * 70)
    for t in Tournament.objects.all():
        print(f"  • {t.name:30} | {t.get_tournament_type_display():15} | {t.get_status_display()}")
    
    # Bookings
    print("\n📅 BOOKINGS:")
    print("-" * 70)
    if Booking.objects.exists():
        for b in Booking.objects.all():
            print(f"  • {b.user.username:15} | {b.facility.name:25} | {b.booking_date}")
    else:
        print("  (No bookings yet)")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY:")
    print("-" * 70)
    print(f"  Total Users:         {User.objects.count():3}")
    print(f"  Total Facilities:    {Facility.objects.count():3}")
    print(f"  Total Equipment:     {Equipment.objects.count():3}")
    print(f"  Total Tournaments:   {Tournament.objects.count():3}")
    print(f"  Total Bookings:      {Booking.objects.count():3}")
    print("=" * 70)

if __name__ == "__main__":
    try:
        display_data()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure Django is properly configured!")
        print("Run this from your project directory where manage.py is located.")

