URL Shortener Project
Overview

This URL shortener project provides a comprehensive solution for shortening long URLs, generating QR codes, creating advertisement pages,
and analyzing link performance using machine learning to detect bad links. Additionally, it includes features for creating business cards, 
in-app advertisements, and a WhatsApp chatbot for link shortening.

Features

  Shorten long links
  Machine learning to determine bad links
  Create advertisement pages
  Generate QR codes
  In-app ads and chat functionality
  Business card creation
  Detailed link analytics (clicks, referrers)
  Graphical representation of analytics

Installation
Prerequisites

    Python 3.8 or higher
    Django 3.2 or higher
    pip (Python package installer)

Clone the Repository

bash

    git clone https://github.com/nanabright775/Final-Year-Project.git
    cd Final-Year-Project/Ushortner

Create a Virtual Environment

bash

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies

bash

    pip install -r requirements.txt

Setting up the Database

Apply the migrations to set up the database:

bash

    python manage.py migrate

Create a Superuser

Create an admin user to access the Django admin panel:

bash

    python manage.py createsuperuser

Tailwind CSS Setup

This project uses Tailwind CSS and flowbite for styling. Follow these steps to set it up:

Install Tailwind CSS
bash
   
    npm install -D tailwindcss
Initialize Tailwind CSS:

bash

    npx tailwindcss init

Run the build script:

bash

    npm run build:css

Install Flowbite 

Flowbite is an open source library of interactive components built on top of Tailwind CSS and it can be
installed using NPM and required as a plugin inside Tailwind CSS.

Install Flowbite as a dependency using NPM:

    npm install flowbite


Run the Development Server

Start the Django development server:

bash

    python manage.py runserver

Access the Application

Open your web browser and go to:


    http://127.0.0.1:8000/

Usage

  Shortening a URL: Enter the long URL and click "Shorten."
  Viewing Analytics: Access detailed analytics from the dashboard.
  Generating QR Codes: Get QR codes for shortened URLs.
  Creating Advertisements: Use the in-app advertisement feature to create and manage ads.
  Detection: uses machine learning to detect a good and a bad link
  create a bussiness card to share
  create a advertisment website

Project Structure

    shortener/: Main Django application
    templates/: HTML templates for the web pages
    static/: Static files (CSS, JavaScript, images)
    models.py: Database models
    views.py: Application views
    urls.py: URL routing
    forms.py: Forms for user input
    admin.py: Django admin configurations

Contributing

Contributions are hereby accepted 
License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Contact

For any questions or inquiries, please contact Bright Atsiatorme at nanabrightatsiatorme@gmail.com.

Images
![Screenshot 2024-07-28 at 21-33-40 ShortenIt - Your URL Shortener Solution](https://github.com/user-attachments/assets/a9f7c9fc-e642-4c02-9868-61b035792208)
![Screenshot 2024-07-28 at 21-42-51 Dashboard](https://github.com/user-attachments/assets/8084ea89-3fbf-4b77-96b5-e8c33239bb86)

![Screenshot 2024-07-28 at 21-44-14 Dashboard](https://github.com/user-attachments/assets/c3da5101-ff68-4deb-9cc4-e0356d7068cc)

![Screenshot 2024-07-28 at 21-44-42 creat a link](https://github.com/user-attachments/assets/5501e56a-9a7b-4392-91b5-71872aca668b)

![Screenshot 2024-07-28 at 21-45-11 Business Card](https://github.com/user-attachments/assets/52a33491-4715-42b9-8532-5f88b87b4746)

![Screenshot 2024-07-28 at 21-46-10 Analytics](https://github.com/user-attachments/assets/303efc7a-9a27-4e97-bd59-7531cfa97074)

![Screenshot 2024-07-28 at 21-46-46 Detection](https://github.com/user-attachments/assets/718b0902-4b36-4872-a100-53c32c5079b2)
![Screenshot 2024-07-29 at 12-53-26 Create AD Page](https://github.com/user-attachments/assets/82e96103-7080-40d3-95c8-83c6593efd1a)

