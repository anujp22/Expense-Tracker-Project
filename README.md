# Expense-Tracker-Project
## Inprogress

**Expense Tracker Project** is a web application that provides user authentication features, including registration, login, logout, and a simple dashboard. It uses Flask for the backend, and PostgreSQL for the database, and incorporates secure password hashing. It will handle user inputs based on their expenses and category inputted then processed on the backend.

## Features

- **User Registration:** Allows users to register with a valid email, username, and password.
- **User Login:** Enables users to log in securely with their credentials.
- **Session Management:** Maintains user sessions for authenticated access to certain routes.
- **Password Hashing:** Utilizes secure password hashing to protect user credentials.
- **Dashboard Access:** Users with an active session can access a simple dashboard.
- **Data Analysis:** Expenses processed and categorized using Data Science Focused Libraries.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Set Environment Variables:**
   `DB_name`: Database name
   `DB_user`: Database user
   `DB_password`: Database password
   `DB_host_name`: Database hostname
   `DB_port`: Database port
4. **Run the Application:**
   ```bash
   python main.py
5. **Access the Application:
   Open a web browser and go to http://localhost:5000/
## Requirements
- Python 3.x
- Flask 3.0.0
- Other dependencies in requirements.txt
## Contributing
Contributions are welcome! If you'd like to contribute to the project, follow these steps:
1. Fork the repository
2. Make your changes
3. Submit a pull request
## License
This project is under the MIT License
