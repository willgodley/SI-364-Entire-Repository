import csv

from unesco.models import Site, Iso, Region, States, Category

f = open('unesco/whc-sites-2018-clean.csv')
reader = csv.reader(f)

Site.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
Category.objects.all().delete()
Iso.objects.all().delete()

i = 0
for row in reader:
    if i == 0:
        i = i + 1
        continue

    print(row)

    try:
        iso_obj = Iso.objects.get(name = row[10])
    except:
        print('inserting iso: ' + row[10])
        iso_obj = Iso(name = row[10])
        iso_obj.save()

    try:
        r = Region.objects.get(name = row[9])
    except:
        print('inserting region: ' + row[9])
        r = Region(name = row[9])
        r.save()

    try:
        s = States.objects.get(name = row[8])
    except:
        print('inserting states: ' + row[8])
        s = States(name = row[8])
        s.save()

    try:
        c = Category.objects.get(name = row[7])
    except:
        print('inserting category: ' + row[7])
        c = Category(name = row[7])
        c.save()

    try:
        site_name = Site.objects.get(name = row[0])
    except:
        print('inserting site: ' + row[0])
        site_name = row[0]

        try:
            y = int(row[3])
        except:
            y = None

        desc = row[1]

        try:
            j = row[2]
        except:
            j = None

        try:
            lng = float(row[4])
        except:
            lng = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            a = float(row[6])
        except:
            a = None

    s = Site(name=site_name, year=y, category=c, states=s, region=r, iso=iso_obj, description=desc, justification=j, longitude=lng, latitude=lat, area_hectares=a)
    s.save()

    i = i + 1
