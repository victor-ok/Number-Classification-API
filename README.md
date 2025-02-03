# Number Classification API
This Python API classifies numbers (prime, perfect, Armstrong, even/odd) and fetches fun facts using the Numbers API.


## features
- Number Classification: Categorizes numbers as prime, perfect, Armstrong (narcissistic), even, or odd.

- Digit Sum Calculation: Calculates the sum of individual digits in a number.

- Fun Fact Retrieval: Fetches a fun fact about the number using the Numbers API (http://numbersapi.com/).

- JSON Responses: Delivers data in JSON format, enabling easy integration with other applications.

- CORS Support: Handles Cross-Origin Resource Sharing (CORS) requests, making it suitable for web and mobile development.




## Technology Stack

- Programming Language: Python
- Framework: Flask (lightweight web framework)
- Deployment: Render
- Version Control: GitHub (code repository)
- External API: Numbers API (for fun facts)

## Setup & Deploy

I referenced this article to deploy my app on Render successfully.

```http
https://medium.com/@acharyaaarush879/deploy-your-flask-app-on-render-c452a7406fb2
```

Once the API is fully deployed and running, you can send requests to the following endpoint:

```http
GET http://<your_public_ip>/api/classify-number?number=371
```
Replace <your_public_ip> with your deployed instance's public IP address.


## API Reference

#### Classify-number

```http
  GET http://<your_ec2_public_ip>/api/classify-number
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `number` | `int` | **Required** |

##### A successful request for the number 371 will return a JSON response like this:
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}
```
The response includes:

- number: The original number submitted.
- is_prime: True if the number is prime, False otherwise.
- is_perfect: True if the number is perfect, False otherwise.
- properties: A list containing classifications like "armstrong" or "odd".
- digit_sum: The sum of the digits in the number.
- fun_fact: A fun fact retrieved from the Numbers API (if available).
- 
##### An unsuccessful request if you provide an invalid number (e.g., non-numeric characters), the API will return a JSON error response:

```json
{
  "number": abc,
  "error": true,
}
```
