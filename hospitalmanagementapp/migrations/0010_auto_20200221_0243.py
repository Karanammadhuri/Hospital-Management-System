
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0009_auto_20200221_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='page',
            field=models.CharField(max_length=10),
        ),
    ]
