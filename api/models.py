# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class OdkclientFarmeridhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    old_farmer_id = models.CharField(max_length=254, blank=True, null=True)
    new_farmer_id = models.CharField(max_length=254)
    verified_date = models.DateField(blank=True, null=True)
    replacement_reason = models.CharField(max_length=254, blank=True, null=True)
    staff_id = models.CharField(max_length=254, blank=True, null=True)
    staff_name = models.CharField(max_length=254, blank=True, null=True)
    date_saved = models.DateTimeField(blank=True, null=True)
    previous_state = models.JSONField()
    current_state = models.JSONField()
    odkclient_id_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'odkclient_farmeridhistory'

class ZwardyFarmers(models.Model):
    id = models.IntegerField(primary_key=True)
    farmer_id = models.CharField(max_length=254, blank=True, null=True)
    date_created = models.DateTimeField()
    is_active = models.BooleanField()
    form_id = models.CharField(max_length=254, blank=True, null=True)
    first_name = models.CharField(max_length=254, blank=True, null=True)
    surname = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zwardy_farmers'
