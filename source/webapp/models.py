from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('bras', 'Bras'),
    ('panties', 'Panties'),
    ('swimwear', 'Swim'),
    ('sleepwear', 'Sleep'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Description')
    category = models.CharField(max_length=20, verbose_name="Category", default=CATEGORY_CHOICES[0][0],
                                choices=CATEGORY_CHOICES)
    remainder = models.IntegerField(verbose_name="Remainder")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
