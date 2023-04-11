from models import Airport

Airport.objects.create(city='Krakow', code='EPKK', popularity=95, longtitude=20, latitude=50).save()
Airport.objects.create(city='Warsaw', code='EPWA', popularity=90, longtitude=21, latitude=52.2).save()
Airport.objects.create(city='Gdansk', code='EPGD', popularity=80, longtitude=18.6, latitude=54.4).save()
Airport.objects.create(city='Wroclaw', code='EPWR', popularity=85, longtitude=17, latitude=51.1).save()
Airport.objects.create(city='Dublin', code='EIDW', popularity=75, latitude=53.3, longtitude=6).save()
Airport.objects.create(city='Barcelona', code='LEBL', popularity=95, latitude=41.3, longtitude=9).save()
Airport.objects.create(city='Berlin', code='EDDB', popularity=82, latitude=52, longtitude=13).save()
Airport.objects.create(city='Brussels', code='EBBR', popularity=79, latitude=50.8, longtitude=4.3).save()
Airport.objects.create(city='Budapest', code='LHBP', popularity=55, latitude=47.5, longtitude=19).save()
Airport.objects.create(city='Cairo', code='HECA', popularity=79, latitude=30, longtitude=31).save()
Airport.objects.create(city='Caracas', code='SVMI', popularity=50, latitude=10.3, longtitude=-67).save()
Airport.objects.create(city='Frankfurt', code='EDDF', popularity=90, latitude=50.7, longtitude=8).save()
Airport.objects.create(city='Sydney', code='YSSY', popularity=93, latitude=-34, longtitude=151).save()