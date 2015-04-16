from django.db import models

# Create your models here.

class Join(models.Model):
  email = models.EmailField(unique=True)
  ref_id = models.CharField(max_length=120, default='ABC', unique=True)
  ip_address = models.CharField(max_length=120, default='ABC')
  timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
  updated = models.DateTimeField(auto_now_add = False, auto_now = True)

  def __unicode__(self):
    return "%s" %(self.email)

  class Meta:
    unique_together = ("email","ref_id",)

# 1. Install south: pip install south, add south to settings.py under Installed_APPS
# 2. Ensure Model is in sync with Database - python manage.py syncdb
# 3. Convert the model to south : python manage.py convert_to_south appname
# 4. Make changes to the model - eg add new fields ( ip_address = models.CharField(max_length=120, default='ABC') )
# 5. Run schemamigration: python manage.py schemamigration app --auto
# 6. Run migration: python manage.py migrate