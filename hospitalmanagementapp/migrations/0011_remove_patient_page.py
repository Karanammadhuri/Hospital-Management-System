

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagementapp', '0010_auto_20200221_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='page',
        ),
    ]
