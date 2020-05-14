from django.db import models

# Create your models here.


class Store(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Supplier(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Delivered', 'Delivered'),
		('Approved', 'Approved'),
		('Denied', 'Denied'),
	)
	id = models.CharField(primary_key=True, max_length=200, null=False, choices=STATUS)
	store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
	supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	# file = models.FileField()

	def __str__(self):
		return self.id


class Carrier(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
