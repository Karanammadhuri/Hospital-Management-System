
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=100)),
                ('pdisease', models.CharField(max_length=500)),
                ('pcontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
