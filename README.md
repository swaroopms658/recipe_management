# Recipe Management Application

This repository contains a Recipe Management Application designed to help users manage and organize their personal recipes efficiently.

## Project Overview

The application allows users to:

- Register and log in to their accounts.
- Add new recipes with details such as title, ingredients, instructions, and category.
- Edit or delete existing recipes.
- View a list of all recipes, categorized appropriately.
- Search and filter recipes based on various criteria.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Python, Django
- **Database**: SQLite (default)

## Installation and Setup

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/swaroopms658/recipe_management.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd recipe_management
   ```

3. **Install dependencies**:

   Ensure you have Python installed. It's recommended to use a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for accessing the admin interface):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The application should now be running on `http://127.0.0.1:8000/`.

## Project Structure

- `recipe_management/`: Main application directory containing Django app configurations.
- `static/`: Directory for static files (CSS, JavaScript, images).
- `templates/`: HTML templates for the application.
- `manage.py`: Django's command-line utility for administrative tasks.

## Features

- **User Authentication**: Secure registration and login functionality.
- **Recipe CRUD Operations**: Create, read, update, and delete recipes.
- **Categorization**: Organize recipes into categories (e.g., Breakfast, Lunch, Dinner, Dessert).
- **Search and Filter**: Easily find recipes based on title, ingredients, or category.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

- **GitHub**: [github.com/swaroopms658](https://github.com/swaroopms658)
- **LinkedIn**: [linkedin.com/in/swaroopms658](https://www.linkedin.com/in/swaroopms658)
- **Email**: [your.email@example.com](mailto:your.email@example.com)

Feel free to reach out for collaborations or any inquiries.

---

Thank you for exploring the Recipe Management Application!
