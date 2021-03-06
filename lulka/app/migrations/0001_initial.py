# Generated by Django 4.1.dev20220226170756 on 2022-02-27 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('brands', models.ManyToManyField(to='app.brand')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.title')),
            ],
        ),
    ]
