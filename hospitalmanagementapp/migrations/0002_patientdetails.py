
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patientdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=100)),
                ('mdisease', models.CharField(max_length=500)),
                ('mreports', models.CharField(max_length=1500)),
            ],
            options={
                'db_table': 'patientdetails',
            },
        ),
    ]
