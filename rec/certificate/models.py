from django.db import models
from power_plant.models import PowerPlant
from user.models import User

class Certificate(models.Model):
    supplier = models.ForeignKey(PowerPlant, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    is_jeju = models.BooleanField(default=False)
    supply_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.supplier.name} | {self.supply_date} | {self.quantity}"
    
    
class Transaction(models.Model):
    target = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_info')
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='buyer_info')
    
    
    def __str__(self):
        return f"공급자: {self.target.supplier} | 가격: {self.price}원"