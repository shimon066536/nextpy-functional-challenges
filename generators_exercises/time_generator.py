def gen_secs():
    secs = (s for s in range(60))
    return secs
def gen_minutes():
    minutes = (m for m in range(60))
    return minutes
def gen_hours():
    hours = (h for h in range(24))
    return hours
def gen_time():
    time = ("%02d:%02d:%02d" %(h, m, s) for h in gen_hours() for m in gen_minutes() for s in gen_secs())
    return time
t = gen_time()



def gen_years(start=2019):
    while True:
        yield start
        start += 1
y = gen_years()
def gen_months():
    for m in range(12):
        yield m+1
m = gen_months()
def gen_days(month, leap_year=False):
    number_month = {1: 31, 2: 28, 3: 31, 4: 29, 5: 31, 6: 29, 7: 31, 8: 31, 9: 29, 10: 31, 11: 29, 12: 31}
    leap_number_month = {1: 31, 2: 29, 3: 31, 4: 29, 5: 31, 6: 29, 7: 31, 8: 31, 9: 29, 10: 31, 11: 29, 12: 31}
    if y % 4 == 0:
        leap_year = True
        if y % 100 == 0:
            leap_year = False
            if y % 400 == 0:
                leap_year = True
    if leap_year: return leap_number_month[month]
    else: return number_month[month]
def gen_day():
    for d in range(gen_days(m)):
        yield d+1

count = 0
for y in gen_years():
    for m in gen_months():
        for d in gen_day():
            for t in gen_time():
                count+=1
                if count>1000000:
                    count = 0
                    print("%02d/%02d/%02d" %(d,m,y) ,t, '\n')

# date = (("%02d/%02d/%02d" %(d,m,y) ,t) for y in gen_years() for m in gen_months() for d in gen_day() for t in gen_time())
# date = ([d, m, y, t] for y in gen_years() for m in gen_months() for d in gen_days_of_month() for t in gen_time())
# dd / mm / yyyy  hh: mm:ss

