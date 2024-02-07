
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0006_auto_20200220_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='pspecalist',
        ),
    ]
