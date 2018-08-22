# Generated by Django 2.1 on 2018-08-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20180815_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer_Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Employer_Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employerName', models.CharField(default='', max_length=50, unique=True)),
                ('currentlySubscribed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionTitle', models.CharField(max_length=400)),
                ('postTime', models.CharField(max_length=400)),
                ('remote', models.BooleanField(default=False)),
                ('employerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employers')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400)),
                ('postTime', models.CharField(max_length=400)),
                ('employerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employers')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employers')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('linkedIn', models.CharField(default='', max_length=50, unique=True)),
                ('twitter', models.CharField(default='', max_length=50, unique=True)),
                ('github', models.CharField(default='', max_length=50, unique=True)),
                ('relocate', models.BooleanField(default=False)),
                ('remote', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pwd', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='HirePartner',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.AddField(
            model_name='students',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Users'),
        ),
        migrations.AddField(
            model_name='student_phones',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Students'),
        ),
        migrations.AddField(
            model_name='student_favorites',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Students'),
        ),
        migrations.AddField(
            model_name='messages',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Students'),
        ),
        migrations.AddField(
            model_name='employers',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Users'),
        ),
        migrations.AddField(
            model_name='employer_phones',
            name='employerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employers'),
        ),
        migrations.AddField(
            model_name='employer_favorites',
            name='employerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Employers'),
        ),
        migrations.AddField(
            model_name='employer_favorites',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Students'),
        ),
    ]