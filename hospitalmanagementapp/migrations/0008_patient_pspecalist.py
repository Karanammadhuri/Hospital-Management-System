

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0007_remove_patient_pspecalist'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pspecalist',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
