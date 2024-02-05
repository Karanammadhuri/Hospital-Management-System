

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospiapp', '0003_auto_20200216_0223'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patientdetail',
        ),
    ]
