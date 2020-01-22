# Generated by Django 3.0.2 on 2020-01-22 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=20, verbose_name='First name')),
                ('last_name', models.TextField(max_length=20, verbose_name='Last name')),
                ('date_of_birth', models.DateField(verbose_name='DOB')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, verbose_name='subject name')),
                ('staff', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=20, verbose_name='First name')),
                ('last_name', models.TextField(max_length=20, verbose_name='Last name')),
                ('date_of_birth', models.DateField(verbose_name='DOB')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('classroom', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='staff',
            field=models.ManyToManyField(blank=True, to='student.Staff'),
        ),
    ]