

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_patientdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patientdetails',
            new_name='Patientdetail',
        ),
    ]
