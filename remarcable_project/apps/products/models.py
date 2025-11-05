from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category({self.name!r})"

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Tag({self.name!r})"

    class Meta:
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,
                                 related_name="products",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Product({self.name!r})"