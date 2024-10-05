# Router-Interaction

This Python script interacts with a router's admin panel to retrieve internet browsing history and analyze the data. It logs in to the router's interface, fetches browsing history, identifies the most visited websites, and visualizes the data using a bar chart.

## How It Works

The script uses the `requests` library to create a session and log into the router via its web interface. Once logged in, it retrieves the browsing history page using `BeautifulSoup` for HTML parsing. After extracting the data, it processes it to find the most viewed websites and provides a simple bar chart visualization.

### Main Steps

1. **Login to Router**: The script sends a POST request to log in to the router using a session.
2. **Fetch Browsing History**: After logging in, it navigates to the browsing history page and scrapes the data using `BeautifulSoup`.
3. **Data Analysis**: The script processes the browsing history data to find the website with the most views and prints its details.
4. **Visualization**: It plots the number of views per website in a bar chart using `matplotlib`.
5. **Logout**: Once the process is complete, the script logs out of the router to end the session.

### Prerequisites

- Python 3.x
- The following Python libraries must be installed:
  - **requests**: To handle HTTP requests.
  - **beautifulsoup4**: For parsing HTML content.
  - **matplotlib**: For plotting data in graphs.

You can install these dependencies by running:

```bash
pip install requests beautifulsoup4 matplotlib
