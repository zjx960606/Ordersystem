from django.db import models

# Create your models here.


class City(models.Model):
    """
    城市地点
    """
    city_name = models.CharField(max_length=20, verbose_name="城市地点")


class Restaurant(models.Model):
    """
    餐厅表
    """

    rname = models.CharField(max_length=20, verbose_name='餐厅名称')
    location = models.CharField(max_length=20, verbose_name='餐厅位置')
    rate = models.IntegerField(verbose_name='评级', null=True)
    imgs = models.ImageField(upload_to='hotpic',null=True)
    price = models.IntegerField(default=45,null=True)



class Order_from(models.Model):
    """
    订单表
    """
    order_type = models.CharField(max_length=20, verbose_name='订单类型')
    time = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')


class Suggest(models.Model):
    """
    建议表
    """
    subject = models.CharField(max_length=20, verbose_name='主题')
    message = models.TextField(verbose_name='内容')














