from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student # 核心app服务
from .forms import StudentForm # 核心app的表单

# Create your views here.

# 这里完成注册的表单，需要在前端 index.html 展示
# 函数第一个参数必须是request，而不能是简写req
def index(request):
    students=Student.get_all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # cleaned_data=form.cleaned_data #  注意，这里会调用clean_qq，也调用了 reverse 方法
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()
            # 上述代码可以简化为
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context={
        'students':students,
        'form': form,
    }

    return render(request,'index.html', context=context)

class IndexView(View):
    tamplate_name='index.html'

    def get_context(self):
        students=Student.get_all()
        context={
        'students':students,
        }
        return context
        
    def get(self,request):
        context=self.get_context()
        form= StudentForm()
        context.update({
            'form':form
        })
        return render(request,self.tamplate_name, context=context)

    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context=self.get_context()
        context.update({
            'form':form
        })
        return render(request,self.tamplate_name, context=context)

