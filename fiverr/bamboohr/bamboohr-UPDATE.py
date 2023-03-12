import requests

id = 134
url = f"https://api.bamboohr.com/api/gateway.php/syncflowsolutions/v1/employees/{id}/"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic ZTgyOGU3YzUyNGRlNmNkMmMxZTc0YWUxNDY1YmI0NDQ5NmY0YjVhNTpKRDg2UXA4ZS4qTHNKUXA="
}
payload = {
    "firstName": "Tiberius .O",
    "lastName": "Mairura"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print('Employee updated successfully!')
else:
    print(f"Error: {response.status_code} - {response.text}")
