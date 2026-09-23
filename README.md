<p align="center">
    <img src="eventportal/static/img/final.png" alt="Logo" width="300">
    <h1 align="center">College Event Management Web Application</h1>
</p>

<p align="center">
  <strong>Stay connected with your college events and community through our innovative event portal!</strong><br>
  <a href="https://college-event-portal-0c76.onrender.com/"><strong>Live Website: college-event-portal-0c76.onrender.com</strong></a>
</p>

<hr>

##  Introduction

**College Event Portal** is a user-friendly website created with HTML, CSS, JavaScript, and Flask, tailored to streamline event registration processes within college campuses. The website provides a seamless experience for both event organizers and participants, offering a comprehensive platform to browse, register, and manage various events.

##  Key Features

- **User Authentication:** Secure login and registration for students to browse and manage their events.
- **Event Dashboard:** A modern, responsive grid to discover new events happening around the campus.
- **Ticket Generation:** Automatically generates a digital ticket complete with a barcode upon registering for an event.
- **Admin Panel:** A comprehensive admin desk built with Flask-Admin that allows administrators to easily manage users, create new events, and download lists of attendees.
- **Email Notifications:** Background threading implemented to seamlessly send confirmation emails to users upon event registration.
- **Fully Responsive:** Optimized for desktops, tablets, and mobile devices.

##  Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Mail
- **Frontend:** HTML5, Vanilla CSS3 (Custom Responsive Grid), JavaScript
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Deployment:** Hosted live on Render

##  Installation & Local Development

To run this project locally on your machine, follow these steps:

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/College-Event-Portal.git
   cd College-Event-Portal
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Ensure you set up any required environment variables such as `SECRET_KEY`, `DATABASE_URL`, and SMTP credentials if you plan to test the email functionality.

5. **Run the Application**
   ```sh
   python app.py
   ```
   *The app will be accessible at http://127.0.0.1:5000*

##  Acknowledgements

* [Ejin](https://github.com/ejinbt/)
* [WOC](https://discord.com/invite/program)

##  License

Distributed under the MIT License. See `LICENSE` for more information.
