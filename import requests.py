import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'http://router_ip_address/'  # Replace with the actual IP address of your router
username = 'your_username'
password = 'your_password'

# Create a session and log in to the router
session = requests.Session()
login_payload = {'username': username, 'password': password}
login_response = session.post(url + 'login', data=login_payload)

# Check if login was successful
if login_response.ok:
    # Assuming there's a page that shows browsing history, navigate to that page
    history_page = session.get(url + 'browsing_history')
    
    # Use BeautifulSoup to parse the HTML of the history page (example only)
    soup = BeautifulSoup(history_page.text, 'html.parser')
    
   #example only
   
    website_data = [
    
        ('example.com', '192.168.1.1', 'Desktop', 5000),
        ('example.net', '192.168.1.2', 'Mobile', 4200),
        ('example.org', '192.168.1.3', 'Tablet', 6000),
        ('example.edu', '192.168.1.4', 'Laptop', 5500),
1    ]

    # Find the website with the highest views
    most_viewed_website = max(website_data, key=lambda x: x[3])

    # Print information about the most viewed website
    print("Most Viewed Website:")
    print(f"Website: {most_viewed_website[0]}")
    print(f"IP Address: {most_viewed_website[1]}")
    print(f"Device Name: {most_viewed_website[2]}")
    print(f"Number of Views: {most_viewed_website[3]}")
    

    websites, ips, devices, views = zip(*most_viewed_website)
    plt.figure(figsize=(12, 8))
    plt.bar(websites, views, color='skyblue')
    plt.title('Website-wise Views with IP and Device Name')
    plt.xlabel('Websites')
    plt.ylabel('Number of Views')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.show()



    # Always remember to log out when done
    logout_response = session.get(url + 'logout')
    if logout_response.ok:
        print("Logged out successfully")
    else:
        print("Failed to log out")
    
else:
    print("Login failed")
