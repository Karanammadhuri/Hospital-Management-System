
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0008_patient_pspecalist'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='page',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='pcontact',
            field=models.CharField(max_length=10),
        ),
    ]
