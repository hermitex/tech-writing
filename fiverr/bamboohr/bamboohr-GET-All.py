import requests

subdomain = 'syncflowsolutions'
api_key = 'e828e7c524de6cd2c1e74ae1465bb44496f4b5a5'


# Replace {subdomain} and {api_key} with your BambooHR credentials
url = f"https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/employees/directory"

headers = {
    "Accept": "application/json",
    "Authorization": "Basic ZTgyOGU3YzUyNGRlNmNkMmMxZTc0YWUxNDY1YmI0NDQ5NmY0YjVhNTpKRDg2UXA4ZS4qTHNKUXA="
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    employee_data = response.json()
    # Do something with the employee data
    print(employee_data)
else:
    print('Error retrieving employee data')
