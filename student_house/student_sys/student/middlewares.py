from symbol import pass_stmt
import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class TimeItMiddleware(MiddlewareMixin):

    # 用户进入时的第一个方法，一般在做一些校验，用户登录等，返回值为HttpResponse或者None，为None则继续执行，否则只执行process_response
    def process_request(self, request):
        self.start_time=time.time()
        return 

    # 用户进入时的第二个方法，func是我们要执行的view方法，返回值与process_request一样
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response=func(request)
        costed=time.time()-start
        print('process view {:.2f}s'.format(costed))
        return response
    

    # 用户进入时出错才执行。
    def process_exception(self, request, exception):
        pass
    
    # 用户进入时的第三个方法，如果使用了模板的response，也就是render返回值，就会进入方法增删改模板
    def process_template_response(self, request, response):
        return response

    # 用户进入时的第四个方法，如果使用了模板的response，这里处理response
    def process_response(self, request, response):
        costed=time.time()-self.start_time
        print('process request to response cost {:.2f}s'.format(costed))
        return response
        
