# Generated by Django 3.1 on 2020-08-28 11:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('discription', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('discription', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('code', models.IntegerField(default=0)),
                ('discription', models.CharField(max_length=256)),
                ('is_advanced', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='program.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='program.program'),
        ),
    ]
