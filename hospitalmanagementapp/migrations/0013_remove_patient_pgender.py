

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0012_patient_pgender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pgender',
        ),
    ]
