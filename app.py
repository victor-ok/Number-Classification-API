from flask import Flask, jsonify, request
from flask_cors import CORS
from urllib.request import urlopen
import json

app = Flask(__name__)
CORS(app)

def get_math_properties(number):
    """
    Calculates and returns interesting mathematical properties of a given number.

    Args:
    number: The input number.

    Returns:
    A dictionary containing the calculated properties and a fun fact.
    """
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": check_number(number),
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact(number),
    }

def is_prime(number):
  """Checks if a num is prime."""
  if number <= 1:
    return False
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True

def is_perfect(number):
    """checks if a num is a perfect num"""
    # Sum = 0
    # for i in range(1, number):
    #     if(number % i == 0):
    #         Sum = Sum + i
    # if (Sum == number):
    #     return True
    # else:
    #     return False
    if number < 1:
       return False
    Sum = sum(i for i in range(1, number) if number % i == 0)
    return Sum == number

def digit_sum(number):
    summ = sum(int(d) for d in str(abs(number)))
    
    return summ

def is_armstrong_number(number):
    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of cubes 
    of its individual digits. 

    Args:
    num: The number to check.

    Returns:
    True if the number is an Armstrong number, False otherwise.
    """
    number = abs(number)
    digits =[int(d) for d in str(number)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == number

def check_number(number):
  """
  Checks if a number is an Armstrong number and/or even/odd.

  Args:
    num: The number to check.

  Returns:
    A list containing the results:
      - "armstrong" if the number is an Armstrong number.
      - "even" if the number is even.
      - "odd" if the number is odd.
  """
  results = []
  if is_armstrong_number(number):
    results.append("armstrong")
  if number % 2 == 0:
    results.append("even")
  else:
    results.append("odd")
  return results

def fun_fact(number):
   try:
       URL = f"http://numbersapi.com/{number}/?json"

       with urlopen(URL) as response:
          body = response.read()
       fact = json.loads(body)
       fun_fact = fact["text"]

       return fun_fact
   except Exception:
      return "No fun fact available at the moment"

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/api/classify-number', methods=['GET'])
def get_math_properties_endpoint():
    """Endpoint to retrieve mathematical properties of a number."""
    num = request.args.get('number')
    if request.method == 'GET' and num is not None:
        try:
            number = int(float(num))
            properties = get_math_properties(number)
            return jsonify(properties)
        except ValueError:
            return jsonify({
               "number": request.args.get('number'),
               "error": True,
               }), 400

if __name__ == '__main__':
  app.run(debug=False) 
