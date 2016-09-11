from django.db import models


class Cardb(models.Model):
	car_id = models.AutoField(primary_key=True)
	brand_name = models.CharField(max_length=200, default="", editable=True)
	model_name = models.CharField(max_length=200, default="", editable=True)
	variants = models.CommaSeparatedIntegerField(max_length=350, editable=True)
	min_price = models.IntegerField(default=0)
	max_price = models.IntegerField(default=0)
	min_mileage = models.IntegerField(default=0)
	max_mileage = models.IntegerField(default=0)
	seating_capacity = models.IntegerField(default=0)
	power = models.IntegerField(default=0)
	torque = models.IntegerField(default=0)
	cylinder_capacity = models.IntegerField(default=0)
	fuel_types = models.CommaSeparatedIntegerField(max_length=100, editable=True)
	geartype_manual = models.BooleanField(default=True)
	geartype_auto = models.BooleanField(default=False)
	no_of_gears = models.IntegerField(default=0)
	vehicle_class = models.CharField(max_length=200, default="", editable=True)
	dimensions = models.CommaSeparatedIntegerField(max_length=400, editable=True)
	tank_capacity = models.IntegerField(default=0)
	trunk_capacity = models.IntegerField(default=0)

	def __str__(self):
		return ''.join([self.brand_name,self.model_name])