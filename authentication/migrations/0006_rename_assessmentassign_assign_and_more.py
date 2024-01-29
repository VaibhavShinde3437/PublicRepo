# Generated by Django 5.0.1 on 2024-01-29 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_submittedassessment_assess_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssessmentAssign',
            new_name='Assign',
        ),
        migrations.RenameModel(
            old_name='SubmittedAssessment',
            new_name='Submit',
        ),
        migrations.AlterModelOptions(
            name='assign',
            options={'ordering': ['user_id']},
        ),
        migrations.AlterModelOptions(
            name='submit',
            options={'ordering': ['user_id']},
        ),
    ]