Below is a detailed `README.md` file that explains how to download, set up, edit, and run the **Online Course Platform** application locally. It also includes instructions for automatically installing dependencies, activating the virtual environment, and running the application.

---

# **Online Course Platform**

This is a **Django-based web application** for managing and enrolling in online courses. It allows instructors to create and manage courses, while learners can enroll in courses and track their progress.

---

## **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Download the Project](#download-the-project)
3. [Set Up the Project](#set-up-the-project)
   - [Automatic Setup (Using Scripts)](#automatic-setup-using-scripts)
   - [Manual Setup](#manual-setup)
4. [Run the Application](#run-the-application)
5. [Edit the Application](#edit-the-application)
6. [Project Structure](#project-structure)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Prerequisites**

Before you begin, ensure you have the following installed on your system:

- **Python 3.10 or higher**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Pip**: Python's package installer (comes pre-installed with Python 3.4+).

---

## **Download the Project**

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the project:

   ```bash
   git clone https://github.com/your-username/online-course-platform.git
   ```

   Replace `your-username` with your GitHub username or the repository URL.

2. **Navigate to the Project Directory**:
   ```bash
   cd online-course-platform
   ```

---

## **Set Up the Project**

### **Automatic Setup (Using Scripts)**

1. **Run the Setup Script**:
   The project includes a setup script to automatically install dependencies and activate the virtual environment.

   - **For Windows**:
     Run the `setup.bat` script:
     ```bash
     setup.bat
     ```

   - **For macOS/Linux**:
     Run the `setup.sh` script:
     ```bash
     chmod +x setup.sh
     ./setup.sh
     ```

   This script will:
   - Create a virtual environment.
   - Install all dependencies listed in `requirements.txt`.
   - Activate the virtual environment.

2. **Verify the Setup**:
   After the script runs, ensure the virtual environment is activated. You should see `(venv)` in your terminal prompt.

---

### **Manual Setup**

1. **Create a Virtual Environment**:
   Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - **For Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **For macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run the following commands to apply migrations and set up the database:
   ```bash
   python manage.py migrate
   ```

---

## **Run the Application**

1. **Start the Development Server**:
   Run the following command to start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

3. **Create a Superuser (Optional)**:
   To access the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Then, log in at:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## **Edit the Application**

1. **Open the Project in Your Code Editor**:
   Use your preferred code editor (e.g., VS Code, PyCharm) to open the project directory.

2. **Make Changes**:
   - Edit the `views.py`, `models.py`, and `templates` files to customize the application.
   - Add new features or modify existing ones.

3. **Test Your Changes**:
   After making changes, restart the development server and test the application in your browser.

---

## **Project Structure**

```
online-course-platform/
├── api-gateway/
├── course-service/
├── user-service/
├── venv/
├── manage.py
├── requirements.txt
├── setup.bat
├── setup.sh
└── README.md
```

- **`api-gateway/`**: Contains the API Gateway microservice.
- **`course-service/`**: Contains the Course microservice.
- **`user-service/`**: Contains the User microservice.
- **`venv/`**: Virtual environment directory (created during setup).
- **`manage.py`**: Django management script.
- **`requirements.txt`**: Lists all project dependencies.
- **`setup.bat`**: Windows setup script.
- **`setup.sh`**: macOS/Linux setup script.
- **`README.md`**: This file.

---

## **Troubleshooting**

1. **Virtual Environment Not Activating**:
   - Ensure you are running the activation command from the correct directory.
   - If the issue persists, delete the `venv` folder and recreate it.

2. **Dependencies Not Installing**:
   - Ensure `pip` is up to date:
     ```bash
     python -m pip install --upgrade pip
     ```
   - Check your internet connection.

3. **Database Errors**:
   - Ensure you have applied all migrations:
     ```bash
     python manage.py migrate
     ```

4. **Port Already in Use**:
   - If port `8000` is already in use, specify a different port:
     ```bash
     python manage.py runserver 8001
     ```

---

## **Contributing**

1. **Fork the Repository**:
   Fork the project repository on GitHub.

2. **Create a New Branch**:
   Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes**:
   Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add your commit message here"
   ```

4. **Push to the Branch**:
   Push your changes to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**:
   Open a pull request on GitHub and describe your changes.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or feedback, please contact:
- **Your Name**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [your-username](https://github.com/your-username)

---

Enjoy building and using the **Online Course Platform**! 🚀