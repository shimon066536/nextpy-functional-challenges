"""
datetime_generator.py

Generates full datetime strings (DD/MM/YYYY HH:MM:SS) using generator functions for years, months, days, hours, minutes and seconds.
"""

def gen_secs():
    return (s for s in range(60))

def gen_minutes():
    return (m for m in range(60))

def gen_hours():
    return (h for h in range(24))

def gen_time():
    return ("%02d:%02d:%02d" % (h, m, s) for h in gen_hours() for m in gen_minutes() for s in gen_secs())

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def gen_years(start=2019):
    while True:
        yield start
        start += 1

def gen_months():
    for m in range(1, 13):
        yield m

def gen_days(month, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and is_leap_year(year):
        return (d for d in range(1, 30))
    else:
        return (d for d in range(1, month_days[month] + 1))

def main():
    count = 0
    for y in gen_years():
        for m in gen_months():
            for d in gen_days(m, y):
                for t in gen_time():
                    print("%02d/%02d/%04d %s" % (d, m, y, t))
                    count += 1
                    if count > 1_000_000:
                        return

if __name__ == "__main__":
    main()
