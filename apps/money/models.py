# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class money(models.Model):
    amount = models.IntegerField(null=True, blank=True, verbose_name=u"金额")
    bank = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"银行")
    person = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"持有人")
    buy_date = models.DateField(null=True, blank=True, verbose_name=u"购买日期")
    valid_date = models.DateField(null=True, blank=True, verbose_name=u"生效日期")
    financial_type = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"理财类型")
    
    # 固定期限理财
    fixed_days = models.IntegerField(null=True, blank=True, verbose_name=u"指定天数")
    finish_date = models.DateField(null=True, blank=True, verbose_name=u"结束日期")
    return_rate = models.FloatField(null=True, blank=True, verbose_name=u"年化收益率")
    
    # 非固定
    latest_value = models.FloatField(null=True, blank=True, verbose_name=u"当前净值")
    latest_date = models.DateField(null=True, blank=True, verbose_name=U"更新日期")

    class Meta:
        db_table = "money_info"
