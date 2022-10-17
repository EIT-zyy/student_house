from tkinter.ttk import Style
from django.test import TestCase, Client

# Create your tests here.


from .models import Student

class StudentTestCase(TestCase):
    # 生成测试数据
    def setUp(self):
        Student.objects.create(
            name='xiannanliu',
            sex=0,
            email='nobody@xiannanliu.com',
            profession='公务员',
            qq='11111114',
            phone='1236',
        )
    
    def test_create_and_sex_show(self):
        student=Student.objects.create(
            name='zeronglan',
            sex=0,
            email='nobody@zeronglan.com',
            profession='程序员',
            qq='11111113',
            phone='1235',
        )
        self.assertEqual(student.get_sex_display(), '男','性别字段跟展示不一致！')

    def test_filter(self):
        student=Student.objects.create(
            name='xiannanliu',
            sex=0,
            email='nobody@xiannanliu.com',
            profession='公务员',
            qq='11111114',
            phone='1236',
        )
        name='xiannanliu'
        
        students=Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应该只存在一个名称为{}的用户'.format(name))
        
    def text_get_index(self):
        client=Client()
        response=client.get('/')
        self.assertEqual(response.statys_code,200,'status code must be 200!')
    
    def test_post_student(self):
        client=Client()
        data=dict(
            name='test_for_post',
            sex=0,
            email='nobody@test.com',
            profession='程序员',
            qq='3333333',
            phone='1237',
        )
        response=client.post('/',data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response=client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain "test_for_post"')
