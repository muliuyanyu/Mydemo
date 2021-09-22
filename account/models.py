
from django.db import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    objects=models.Manager()
    uesrname = models.CharField(max_length=20,blank=False,verbose_name='用户名')
    goodsname = models.TextField(verbose_name='物品名称')
    goodsnum = models.SmallIntegerField(default=0,verbose_name='物品数量')
    goodsmy = models.SmallIntegerField(default=0,verbose_name='物品总价（单位为元）')
    createtime = models.DateTimeField(default=now)

    def __str__(self):
        return '用户名称：{}'.format(self.uesrname)

    @classmethod
    def add(cls,uesrname,goodsname,goodsnum,goodsmy,createtime):
        return cls.objects.create(
            uesrname=uesrname,
            goodsname=goodsname,
            goodsnum=goodsnum,
            goodsmy=goodsmy,
            createtime=createtime,

        )


    def update(self,uesrname,goodsname,goodsnum,goodsmy,createtime):
        self.uesrname=uesrname
        self.goodsname=goodsname
        self.goodsnum=goodsnum
        self.goodsmy=goodsmy
        self.createtime=createtime
        self.save()
        return True
