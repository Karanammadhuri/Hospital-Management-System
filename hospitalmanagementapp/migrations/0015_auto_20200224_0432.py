
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospiapp', '0014_patient_pbook_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ptimings',
            field=models.TimeField(default=datetime.datetime(2020, 2, 24, 9, 32, 5, 330661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pbook_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 24, 9, 32, 5, 330661, tzinfo=utc)),
        ),
    ]
