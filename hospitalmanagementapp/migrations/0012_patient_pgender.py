

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospiapp', '0011_remove_patient_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pgender',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
