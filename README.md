**README.md**

# TaskPRJ - Setting Up Instructions

1. **Install Python:**

   - Ensure Python is installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Packages:**

   ```
   pip install -r requirements.txt
   ```

3. **Make Migrations:**

   ```
   python manage.py makemigrations
   ```

4. **Apply Migrations:**

   ```
   python manage.py migrate
   ```

5. **Run the Server:**

   ```
   python manage.py runserver
   ```

6. **Access the Application:**

- Once the server is running, you can access the TaskPRJ application in your web browser at `http://127.0.0.1:8000/` OR Test it on <strong>PostMan</strong>.

**Images:**

- ![](./demoImages/contacts_view.png)
- ![](./demoImages/login.png)
- ![](./demoImages/mark_spam.png)
- ![](./demoImages/register.png)
- ![](./demoImages/search_by_name.png)
- ![](./demoImages/search_by_num.png)

## Project Structure

- **`taskprj/`**: Main project directory containing settings, URLs, and WSGI configurations.
- **`restapp/`**: Django app directory containing models, views, serializers, and admin configurations.
- **`populatedata.py`**: Script to populate the database with sample data.
- **`requirements.txt`**: File listing the required Python packages for the project.
