# Generated by Django 3.1.7 on 2021-03-25 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='date_of_both',
        ),
        migrations.AddField(
            model_name='member',
            name='course',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='fields_of_interest',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='industry_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='introduction',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='name_of_company_or_organization',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='name_of_the_institute_you_took_the_mba_emba',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='your_position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='family_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.BooleanField(null=True),
        ),
        migrations.CreateModel(
            name='MbaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100, null=True)),
                ('graduated', models.BooleanField(null=True)),
                ('faculty', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('completion_status', models.BooleanField(null=True)),
                ('year_of_entered', models.IntegerField(null=True)),
                ('year_of_graduation', models.IntegerField(null=True)),
                ('member', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.member')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralDegreeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100, null=True)),
                ('graduated', models.BooleanField(null=True)),
                ('faculty', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('completion_status', models.BooleanField(null=True)),
                ('year_of_entered', models.IntegerField(null=True)),
                ('year_of_graduation', models.IntegerField(null=True)),
                ('member', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='institute.member')),
            ],
        ),
    ]
