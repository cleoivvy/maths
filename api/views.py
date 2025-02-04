import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class ClassifyNumberView(APIView):
    def get(self, request):
        number = request.GET.get('number')
        if not number:
            return Response({'error': 'Please provide a number'}, status=400)

        try:
            number = int(number)
        except ValueError:
            return Response({'number': number, 'error': True}, status=400)

        is_prime = self.is_prime_number(abs(number))
        is_perfect = self.is_perfect_number(abs(number))
        properties = self.get_properties(number)
        digit_sum = sum(int(digit) for digit in str(abs(number)))
        fun_fact = self.get_fun_fact(abs(number))
        data = {
            'number': number,
            'is_prime': is_prime,
            'is_perfect': is_perfect,
            'properties': properties,
            'digit_sum': digit_sum,
            'fun_fact': fun_fact
        }

        return Response(data)

    def is_prime_number(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_number(self, n: int) -> bool:
        if n < 1:
            return False
        return n == sum(i for i in range(1, n) if n % i == 0)
    def get_properties(self, n: int) -> list:
        properties = []
        num_str = str(n)
        if num_str.startswith('-'):
         properties.append('negative')
        else:
            properties.append('positive')
        num_digits = len(num_str.lstrip('-'))
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str.lstrip('-'))
        if armstrong_sum == abs(n):
            if len(properties) < 2:
                properties.append("armstrong")
        if abs(n) % 2 == 0 and len(properties) < 2:
            properties.append("even")
        elif abs(n) % 2 != 0 and len(properties) < 2:
            properties.append("odd")
        return properties


    def get_fun_fact(self, number: int) -> str:
        try:
            response = requests.get(f'http://numbersapi.com/{number}?json=true')
            response.raise_for_status()
            fact = response.json()['text']
            if number < 0:
                fact = fact.replace(str(abs(number)), str(number))
            return fact
        except requests.RequestException as e:
            return f"Error fetching fun fact: {str(e)}"


