# Django Multi-Role Authentication System

![Python](https://img.shields.io/badge/Python-3.9.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Pip](https://img.shields.io/badge/Pip-25.1.1-orange)

A complete authentication system with multi-role dashboards (Admin, Editor, Customer), password recovery, and environment-based configuration.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Server](#running-the-server)
- [Test Accounts](#test-accounts)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Custom Commands](#custom-commands)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features
✅ **Core Authentication**  
- User registration with email verification
- Login/logout functionality
- Password reset via email
- Session management

✅ **Role-Based Access Control**  
- Django Admin (default)
- Custom Admin Dashboard
- Editor Dashboard
- Customer Dashboard

✅ **Security**  
- Password hashing
- CSRF protection
- Environment-based secret management
- Secure session cookies

✅ **Additional Features**  
- Responsive templates
- Form validation
- Error handling
- Activity logging

## Prerequisites
- Python 3.9.11
- Pip 25.1.1
- Virtualenv (recommended)
- PostgreSQL/MySQL (optional)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/projectname.git
cd projectname
