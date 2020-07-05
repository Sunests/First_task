from django.db import models


class Hotel(models.Model):
    hotel_id = models.IntegerField('номер отеля')
    name = models.CharField('название отеля', max_length=150)
    city = models.CharField('название города', max_length=50)
    street = models.CharField('название улицы', max_length=50)
    house_number = models.CharField('номер дома', max_length=30)
    index = models.CharField('индекс почтового отделения', max_length=10)
    rooms_number = models.IntegerField('кол-во комнат')

    def __str__(self):
        return f"{self.name} (отель №{self.hotel_id})"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_id = models.IntegerField('номер комнаты')
    type = models.CharField('Тип комнаты(эконом, бизнес, люкс)', max_length=15)
    private_bath = models.BooleanField('Есть ли собственная ванна, True - есть, False - нет')
    private_toilet = models.BooleanField('Есть ли собственный туалет, True - есть, False - нет')
    sleeping_berth_number = models.DecimalField('Кол-во спальных мест, не больше 5', max_digits=5, decimal_places=0)
    double_bed = models.BooleanField('Есть ли двуспальная кровать, True - есть, False - нет')
    television_set = models.BooleanField('Есть ли телевизор, True - есть, False - нет')
    balcony = models.BooleanField('Есть ли балкон, True - есть, False - нет')

    def __str__(self):
        return f"{self.hotel.name}: {self.room_id}"

