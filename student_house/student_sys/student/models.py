from email.policy import default
from django.db import models

# Create 学生信息.
# 以下代码规范
# 1.类名驼峰，方法与变量小写+下划线
# 2.定义顺序：字段定义、自定义managers属性、class Meta定义、def __str__、def save、def get_absolute_url、其他方法
# 3.特殊的choices参数字段，定义要大写，如SEX_ITEMS


class Student(models.Model):
    SEX_ITEMS=[
        (1,'男'),
        (2,'女'),
        (0,'未知'),
    ]
    STATYS_ITEMS=[
        (0,'申请'),
        (1,'通过'),
        (2,'拒绝'),
    ]
    name=models.CharField(max_length=128, verbose_name="姓名")
    sex=models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession=models.CharField(max_length=128, verbose_name="职业")
    email=models.EmailField(verbose_name="Email")
    qq=models.CharField(max_length=128, verbose_name="QQ")
    phone=models.CharField(max_length=128, verbose_name="电话")

    status=models.IntegerField(choices=STATYS_ITEMS, default=0, verbose_name="审核状态")

    created_time=models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]

    class Meta:
        verbose_name=verbose_name_plural='学员信息'

