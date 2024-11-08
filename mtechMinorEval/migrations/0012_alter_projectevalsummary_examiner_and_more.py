# Generated by Django 5.1 on 2024-10-02 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtechMinorEval', '0011_rename_examiner_total_eval_projectevalsummary_examiner_score_and_more'),
        ('users', '0014_faculty_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectevalsummary',
            name='examiner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examiner_eval_summaries', to='users.faculty'),
        ),
        migrations.AlterField(
            model_name='projectevalsummary',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guide_eval_summaries', to='users.faculty'),
        ),
        migrations.AlterField(
            model_name='projectevalsummary',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]
