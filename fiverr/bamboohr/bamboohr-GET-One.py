import requests

id = 134
# Set the API URL and headers
company_domain = "syncflowsolutions"
api_key = "e828e7c524de6cd2c1e74ae1465bb44496f4b5a5"
url = f"https://api.bamboohr.com/api/gateway.php/{company_domain}/v1/employees/{id}/"
headers = {
    "Accept": "application/json",
    "Authorization": "Basic ZTgyOGU3YzUyNGRlNmNkMmMxZTc0YWUxNDY1YmI0NDQ5NmY0YjVhNTpKRDg2UXA4ZS4qTHNKUXA="
}

# Specify the fields to retrieve and only retrieve current data
params = {
    "fields": "firstName,lastName",
    "onlyCurrent": "true"
}

# Send the GET request and print the response
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    employee_data = response.json()
    print(employee_data)
else:
    print("Error retrieving employee data")
