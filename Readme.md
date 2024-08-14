# Mini-Box Project

Welcome to the Mini-Box project! This application is designed to manage attendance, assignments, and tasks, inspired by the functionalities of DarwinBox.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
  - [Backend (Django)](#backend-django)
  - [Frontend (React with Vite)](#frontend-react-with-vite)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Mini-Box is a full-stack application built to handle various educational management tasks. It includes functionalities for tracking attendance, managing assignments, and organizing tasks for students.

## Technologies Used

- **Frontend:** React, Vite
- **Backend:** Django, Django REST Framework
- **Database:** MongoDB
- **Environment Management:** Python Virtual Environment (`venv`)
- **Other:** Django Channels, JWT for Authentication

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Node.js 14+ and npm**
- **MongoDB**

### Setup Instructions

Follow these steps to set up the project on your local machine:
##
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/minibox.git
   cd minibox
##
2. **Delete Existing Virtual Environment (if applicable):**

   If there’s an existing virtual environment named `box`, delete it using:

   ```bash
   rm -rf box
##
3. **Create a New Virtual Environment:**


    *python -m venv your-venv-name*
##
4. **Activate the Virtual Environment:**

    a. **Windows:**


    *your-venv-name\Scripts\activate*
 ##   
5. **macOS/Linux:**


    *source your-venv-name/bin/activate*
##
6. **Install Backend Dependencies:**


    *pip install -r requirements.txt*
##
7. **Install Frontend Dependencies:**

    **cd frontend**
    
    **npm install**