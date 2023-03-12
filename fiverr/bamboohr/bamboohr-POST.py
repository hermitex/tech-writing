import requests

url = "https://api.bamboohr.com/api/gateway.php/syncflowsolutions/v1/employees/"

payload = {
    "firstName": "Tiberius",
    "lastName": "Mairura"
}
headers = {
    "content-type": "application/json",
    "authorization": "Basic ZTgyOGU3YzUyNGRlNmNkMmMxZTc0YWUxNDY1YmI0NDQ5NmY0YjVhNTpKRDg2UXA4ZS4qTHNKUXA="
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    employee_location = response.headers.get('Location')
    print(f'Employee Location: {employee_location}')
    print(response.text)
except requests.exceptions.HTTPError as error:
    print(f"HTTP error occurred: {error}")
except Exception as error:
    print(f"An error occurred: {error}")
