from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Cardb(models.Model):
	car_id = models.AutoField(primary_key=True)
	brand_name = models.CharField(max_length=200, default="", editable=True)
	model_name = models.CharField(max_length=200, default="", editable=True)
	variants = models.CharField(max_length=500,validators=[validate_comma_separated_integer_list], editable=True)
	min_price = models.FloatField(default=0)
	max_price = models.FloatField(default=0)
	min_mileage = models.FloatField(default=0)
	max_mileage = models.FloatField(default=0)
	seating_capacity = models.IntegerField(default=0)
	power = models.FloatField(default=0)
	torque = models.FloatField(default=0)
	cylinder_capacity = models.IntegerField(default=0)
	fuel_types = models.CharField(max_length=500,validators=[validate_comma_separated_integer_list], editable=True)
	geartype_manual = models.BooleanField(default=True)
	geartype_auto = models.BooleanField(default=False)
	no_of_gears = models.IntegerField(default=0)
	VEHICLE_CLASS_CHOICES = (
        ('Van', 'Van'),
        ('Minivan', 'Minivan'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('MUV', 'MUV'),
        ('Offroad', 'Offroad'),
        ('Hybrid', 'Hybrid'),
    )
	vehicle_class = models.CharField(max_length=10,choices=VEHICLE_CLASS_CHOICES)
	dimensions = models.CharField(max_length=500,validators=[validate_comma_separated_integer_list], editable=True)
	tank_capacity = models.IntegerField(default=0)
	trunk_capacity = models.IntegerField(default=0)
	ac = models.BooleanField(default=True)
	power_window = models.BooleanField(default=True)
	cd_drive = models.BooleanField(default=True)
	mp3_player = models.BooleanField(default=True)
	usb = models.BooleanField(default=True)
	aux = models.BooleanField(default=True)
	foglamps = models.BooleanField(default=True)
	esp = models.BooleanField(default=True)
	abs_break = models.BooleanField(default=True)
	airbags = models.IntegerField(default=0)
	traction_control = models.BooleanField(default=True) 
	
	def __str__(self):
		return ''.join([self.brand_name,self.model_name])