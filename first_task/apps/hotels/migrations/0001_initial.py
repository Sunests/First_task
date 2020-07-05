# Generated by Django 2.2 on 2020-07-01 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hotel', models.IntegerField(verbose_name='номер отеля')),
                ('name', models.CharField(max_length=150, verbose_name='название отеля')),
                ('city', models.CharField(max_length=50, verbose_name='название города')),
                ('street', models.CharField(max_length=50, verbose_name='название улицы')),
                ('house_number', models.CharField(max_length=30, verbose_name='номер дома')),
                ('index', models.CharField(max_length=10, verbose_name='индекс почтового отделения')),
                ('rooms_number', models.IntegerField(verbose_name='кол-во комнат')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(verbose_name='номер комнаты')),
                ('type', models.CharField(max_length=15, verbose_name='Тип комнаты(эконом, бизнес, люкс)')),
                ('private_bath', models.BooleanField(verbose_name='Есть ли собственная ванна, True - есть, False - нет')),
                ('private_toilet', models.BooleanField(verbose_name='Есть ли собственный туалет, True - есть, False - нет')),
                ('sleeping_berth_number', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Кол-во спальных мест, не больше 5')),
                ('double_bed', models.BooleanField(verbose_name='Есть ли двуспальная кровать, True - есть, False - нет')),
                ('television_set', models.BooleanField(verbose_name='Есть ли телевизор, True - есть, False - нет')),
                ('balcony', models.BooleanField(verbose_name='Есть ли балкон, True - есть, False - нет')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel')),
            ],
        ),
    ]