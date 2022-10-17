# from socket import fromshare
from django import forms
from .models import Student

# 这里让用户填写表单，但是逻辑需要展示
# 展示在view层，所以接下来修改view的代码

class StudentForm(forms.ModelForm):
    # 可以给各个字段写验证
    # 这个方法对各个字段都会调用，但定义了 self.cleaned_data['qq']， 所以只对这个字段生效
    def clean_qq(self):
        cleaned_data=self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name','sex','profession',
            'email','qq','phone'
        )
