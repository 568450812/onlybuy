# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-17 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(default='20190601HHMMSSXXXXXX', max_length=20, verbose_name='订单号')),
                ('status', models.IntegerField(choices=[(0, '订单关闭'), (1, '待付款'), (2, '待发货'), (3, '配送中'), (4, '交易完成')], default=0, verbose_name='订单状态')),
                ('real_money', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='实际价格')),
                ('logistics', models.CharField(default='北京市东城区珠市口东大街6号珍贝大厦三层达内科技', max_length=300, verbose_name='物流信息')),
                ('amount', models.IntegerField(default=0, null=True, verbose_name='数量')),
                ('bank', models.CharField(default='unpay', max_length=50, verbose_name='支付方式加卡号')),
                ('dealtime', models.DateTimeField(auto_now_add=True, verbose_name='交易时间')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='商品名称', max_length=300, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品交易时价格')),
                ('amount', models.IntegerField(default=0, null=True, verbose_name='交易数量')),
                ('goodsimg', models.CharField(default='/images/default.png', max_length=100, verbose_name='产品图')),
                ('spec_name', models.CharField(default='规格', max_length=300, verbose_name='规格名称')),
                ('spec_info', models.CharField(max_length=300, verbose_name='规格信息')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
    ]
