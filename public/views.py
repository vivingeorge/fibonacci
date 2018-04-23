from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import FibonacciNumber
from django_redis import get_redis_connection
import time


def get_fibonacci(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def home(request):
    load_time = time.time()
    no = None
    fib_no = None
    if request.GET.get('no'):
        no = int(request.GET.get('no'))
        if no >= 0 and no <= 20000:
            redis_client = get_redis_connection("default")
            redis_key = "fibonacci_" + str(no)
            redis_result = redis_client.get(redis_key)
            if redis_result:
                fib_no = redis_result.decode('utf-8')
            else:
                try:
                    result = FibonacciNumber.objects.get(number=no)
                    fib_no = result.value
                except ObjectDoesNotExist:
                    fib_no = get_fibonacci(no)
                    if no <= 90:
                        fibonacci_number = FibonacciNumber()
                        fibonacci_number.number = no
                        fibonacci_number.value = fib_no
                        fibonacci_number.save()
                redis_client.set(redis_key, fib_no)
    processing_time = time.time() - load_time
    return render(request, 'public/home.html', {'no': no, 'fib_no': fib_no, 'processing_time': processing_time})
