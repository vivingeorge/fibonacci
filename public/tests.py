from django.test import TestCase

# Create your tests here.
from .models import FibonacciNumber

class AnimalTestCase(TestCase):
    def setUp(self):
        FibonacciNumber.objects.create(number=1, value=1)
        FibonacciNumber.objects.create(number=2, value=1)
        FibonacciNumber.objects.create(number=3, value=2)
        FibonacciNumber.objects.create(number=40, value=102334155)

    def test_animals_can_speak(self):
        fibonacci_number_1 = FibonacciNumber.objects.get(number=1)
        fibonacci_number_2 = FibonacciNumber.objects.get(number=2)
        fibonacci_number_3 = FibonacciNumber.objects.get(number=3)
        fibonacci_number_40 = FibonacciNumber.objects.get(number=40)

        self.assertEqual(fibonacci_number_1.value, 1)
        self.assertEqual(fibonacci_number_2.value, 1)
        self.assertEqual(fibonacci_number_3.value, 2)
        self.assertEqual(fibonacci_number_40.value, 102334155)