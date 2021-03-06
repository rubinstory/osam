# Generated by Django 3.0.8 on 2020-09-26 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('account_type', models.CharField(choices=[('military', '군인'), ('counselor', '상담사')], default='', max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Counselor_User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('career', models.TextField()),
            ],
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='Military_User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('rank', models.CharField(max_length=30)),
                ('workplace', models.CharField(max_length=200)),
            ],
            bases=('user.user',),
        ),
    ]
