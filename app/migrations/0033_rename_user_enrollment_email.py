# Generated by Django 4.1.4 on 2024-05-03 18:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0032_student_dob_student_emailid_student_full_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="enrollment",
            old_name="user",
            new_name="email",
        ),
    ]