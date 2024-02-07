

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0004_delete_patientdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pspecialist',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
