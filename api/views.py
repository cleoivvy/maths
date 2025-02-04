import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NumberProperties
from .serializers import NumberPropertiesSerializer

class ClassifyNumberView(APIView):
    def get(self, request):
        number = request.GET.get('number')
        if number is None or not number.isdigit():
            return Response({'error': 'Invalid input. Please provide a valid number.'}, status=400)

        number = int(number)
        try:
            number_properties = NumberProperties.objects.get(number=number)
        except NumberProperties.DoesNotExist:
            number_properties = classify_number(number)
            number_properties.save()

        serializer = NumberPropertiesSerializer(number_properties)
        return Response(serializer.data)

def classify_number(number):
    is_prime = is_prime_number(number)
    is_perfect = is_perfect_number(number)
    properties = get_properties(number)
    digit_sum = sum(int(digit) for digit in str(number))
    fun_fact = get_fun_fact(number)

    return NumberProperties(
        number=number,
        is_prime=is_prime,
        is_perfect=is_perfect,
        properties=','.join(properties),
        digit_sum=digit_sum,
        fun_fact=fun_fact
    )

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n):
    if n < 1:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

def get_properties(n):
    properties = []
    if is_prime_number(n):
        properties.append('prime')
    if is_perfect_number(n):
        properties.append('perfect')
    return properties

def get_fun_fact(number):
    try:
        response = requests.get(f'http://numbersapi.com/{number}?json=true')
        response.raise_for_status() 
        return response.json()['text']
    except requests.RequestException as e:
        return f"Error fetching fun fact: {str(e)}"
