

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0013_remove_patient_pgender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pbook_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 24, 9, 30, 45, 601360, tzinfo=utc)),
        ),
    ]
