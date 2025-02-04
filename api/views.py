import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NumberProperties
from .serializers import NumberPropertiesSerializer

class ClassifyNumberView(APIView):
    def get(self, request):
        """Handle GET requests to classify a number."""
        number = request.GET.get('number')
        if number is None:
            return Response({'error': 'Invalid input'}, status=400)

        try:
            number = int(number)
        except ValueError:
            return Response({'error': 'Invalid input'}, status=400)

        try:
            number_properties = NumberProperties.objects.get(number=number)
        except NumberProperties.DoesNotExist:
            number_properties = self.classify_number(number)
            number_properties.save()

        serializer = NumberPropertiesSerializer(number_properties)
        return Response(serializer.data)
    def classify_number(self, number: int) -> NumberProperties:
        """Classify a number and return its properties."""
        is_prime = self.is_prime_number(abs(number))
        is_perfect = self.is_perfect_number(abs(number))
        properties = self.get_properties(number)
        digit_sum = sum(int(digit) for digit in str(abs(number)))  
        fun_fact = self.get_fun_fact(abs(number))  

        return NumberProperties(
            number=number,
            is_prime=is_prime,
            is_perfect=is_perfect,
            properties=','.join(properties),
            digit_sum=digit_sum,
            fun_fact=fun_fact
        )

    def is_prime_number(self, n: int) -> bool:
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def is_perfect_number(self, n: int) -> bool:
        """Check if a number is perfect."""
        if n < 1:
            return False
        return n == sum(i for i in range(1, n) if n % i == 0)

    def get_properties(self, n: int) -> list:
        """Get the properties of a number."""
        properties = []
        num_str = str(n)
        if num_str.startswith('-'):  
            properties.append('negative')
        else:
            properties.append('positive')
        num_digits = len(num_str.lstrip('-'))  
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str.lstrip('-'))
        if armstrong_sum == abs(n):  
            properties.append("armstrong")
        if abs(n) % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        return properties
    def get_fun_fact(self, number: int) -> str:
        """Get a fun fact about a number."""
        try:
            response = requests.get(f'http://numbersapi.com/{number}?json=true')
            response.raise_for_status()
            return response.json()['text']
        except requests.RequestException as e:
            return f"Error fetching fun fact: {str(e)}"


