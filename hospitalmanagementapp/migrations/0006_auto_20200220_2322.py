

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospiapp', '0005_patient_pspecialist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='pspecialist',
            new_name='pspecalist',
        ),
    ]
