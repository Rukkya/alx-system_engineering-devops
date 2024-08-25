#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API endpoint
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee information
    employee_url = f'{base_url}/users/{employee_id}'
    response = requests.get(employee_url)
    
    # Check if the employee exists
    if response.status_code != 200:
        print(f'Employee with ID {employee_id} not found.')
        return

    employee_data = response.json()
    employee_name = employee_data['name']
    
    # Fetch todos for the employee
    todos_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todos_url)
    
    if response.status_code != 200:
        print(f'Failed to retrieve TODO list for employee ID {employee_id}.')
        return
    
    todos_data = response.json()
    
    # Calculate the progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    
    # Display progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')

if __name__ == '__main__':
    # Ensure an employee ID is provided
    if len(sys.argv) != 2:
        print('Usage: python script.py EMPLOYEE_ID')
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)
    
    # Get the TODO list progress for the given employee ID
    get_employee_todo_progress(emp_id)
