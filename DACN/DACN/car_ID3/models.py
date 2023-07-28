from django.db import models
import django
# Create your models here.
class Car(models.Model):
    car_id = models.AutoField(primary_key = True)
    symboling = models.FloatField()
    carname = models.CharField(max_length = 50, blank = False)
    fueltype = models.CharField(max_length = 50, blank = False)
    aspiration = models.CharField(max_length = 50, blank = False)
    doornumber = models.CharField(max_length = 50, blank = False)
    carbody = models.CharField(max_length = 50, blank = False)
    drivewheel = models.CharField(max_length = 50, blank = False)
    enginelocation = models.CharField(max_length = 50, blank = False)
    wheelbase = models.FloatField()
    carlength = models.FloatField()
    carwidth = models.FloatField()
    carheight = models.FloatField()
    curbweight = models.FloatField()
    enginetype = models.CharField(max_length = 50, blank = False)
    cylindernumber = models.CharField(max_length = 50, blank = False)
    enginesize = models.FloatField()
    fuelsystem = models.CharField(max_length = 50, blank = False)
    boreratio = models.FloatField()
    stroke = models.FloatField()
    compressionratio = models.FloatField()
    horsepower = models.FloatField()
    peakrpm = models.FloatField()
    citympg = models.FloatField()
    highwaympg = models.FloatField()
    price = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def to_dict(self):
        return {
        'symboling': self.symboling,
        'CarName': self.carname,
        'fueltype': self.fueltype,
        'aspiration': self.aspiration,
        'doornumber': self.doornumber,
        'carbody': self.carbody,
        'drivewheel': self.drivewheel,
        'enginelocation': self.enginelocation,
        'wheelbase': self.wheelbase,
        'carlength': self.carlength,
        'carwidth': self.carwidth,
        'carheight': self.carheight,
        'curbweight': self.curbweight,
        'enginetype': self.enginetype,
        'cylindernumber': self.cylindernumber,
        'enginesize': self.enginesize,
        'fuelsystem': self.fuelsystem,
        'boreratio': self.boreratio,
        'stroke': self.stroke,
        'compressionratio': self.compressionratio,
        'horsepower': self.horsepower,
        'peakrpm': self.peakrpm,
        'citympg': self.citympg,
        'highwaympg': self.highwaympg,
        'price': self.price
        }

class User(models.Model):
    username = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length=50,blank=True)
    