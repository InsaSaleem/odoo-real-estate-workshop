# 🏡 Real Estate Management Module — Odoo 19

A custom **Real Estate Management module built with Odoo 19** as part of a three-day Odoo development workshop. This project demonstrates practical experience with Odoo's modular architecture, ORM, Python models, XML views, relational fields, access control, and business logic.

The module provides functionality for managing properties, property types, tags, buyers, salespersons, and property offers within an existing Odoo environment.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Core Odoo Concepts](#-core-odoo-concepts)
- [Future Enhancements](#-future-enhancements)
- [Learning Outcomes](#-learning-outcomes)
- [Workshop Context](#-workshop-context)
- [Author](#-author)

## 📌 Overview

The Real Estate Management module is a learning project designed to explore how custom business applications can be developed within the Odoo ERP framework.

It follows Odoo's modular architecture, combining Python model definitions, XML-based user interfaces, relational data structures, and access-control configuration to create a property management application.

The project focuses on foundational Odoo development practices and provides a starting point for further customization and enhancement.

## ✨ Features

### 🏠 Property Management

- Create and manage real estate property records.
- Store property descriptions, availability dates, expected prices, and selling prices.
- Track bedrooms, living area, and garden area.
- Calculate total property area using living and garden areas.
- Manage property lifecycle status.

### 🗂️ Property Types and Tags

- Categorize properties by type.
- Assign multiple tags to property records.
- Configure color-coded tags.
- Enforce unique names for property types and tags.

### 🤝 Property Offer Management

- Create offers linked to properties and buyers.
- Record offer prices and offer statuses.
- Accept or refuse offers through model actions.
- Update the associated property's buyer, selling price, and status when an offer is accepted.
- Apply validation rules to offer-related business logic.

### 👥 Relational Data Management

- Associate properties with salespersons and buyers.
- Connect properties to types, tags, and offers.
- Use Odoo relational fields to maintain connections between business records.
- Organize property information into structured form sections.

### 🖥️ User Interface

- XML-defined list and form views.
- Dedicated views for properties, property types, tags, and offers.
- Window actions and menu entries for application navigation.
- Status bars for displaying property states.
- Additional user-related view configuration.

### 🔐 Access Control and Data Validation

- Configure model permissions through `ir.model.access.csv`.
- Define access rules for internal users.
- Apply database constraints for price validation and unique names.
- Use Odoo model logic to validate business operations.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Odoo 19** | ERP framework and application platform |
| **Python** | Business logic and model definitions |
| **Odoo ORM** | Database operations and model relationships |
| **XML** | Views, actions, and menu configuration |
| **PostgreSQL** | Database backend |
| **CSV** | Model access-control configuration |
| **Git & GitHub** | Version control and project hosting |
| **Visual Studio Code** | Development environment |

## 📂 Project Structure

```text
odoo-real-estate-workshop/
└── estate/
    ├── models/
    │   ├── __init__.py
    │   ├── estate_property.py
    │   ├── estate_property_offer.py
    │   ├── estate_property_tag.py
    │   └── estate_property_type.py
    ├── security/
    │   └── ir.model.access.csv
    ├── views/
    │   ├── estate_menus.xml
    │   ├── estate_property_views.xml
    │   ├── estate_property_offer_views.xml
    │   ├── estate_property_tag_views.xml
    │   ├── estate_property_type_views.xml
    │   └── res_users_views.xml
    ├── __init__.py
    └── __manifest__.py
```

## ⚙️ Prerequisites

Before installing the module, ensure that you have:

- Odoo 19 installed and configured.
- Python available in your environment.
- PostgreSQL configured for your Odoo installation.
- An accessible Odoo database.
- Git installed if you intend to clone the repository.

> **Note:** This is a custom Odoo addon, not a standalone Python application. It must be installed within an existing Odoo environment.

## 🚀 Installation and Setup

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/InsaSaleem/odoo-real-estate-workshop.git
```

Navigate to the cloned repository:

```bash
cd odoo-real-estate-workshop
```

### 2. Configure the Addons Directory

Copy the `estate` directory into an Odoo addons directory, or keep it in a separate custom addons directory.

For example, on Windows:

```text
C:\Program Files\Odoo 19.0\server\addons\estate
```

Alternatively, configure a separate custom addons directory in your Odoo configuration file and ensure it is included in `addons_path`.

### 3. Verify the Module Files

Ensure that the `estate` directory contains:

- `__manifest__.py`
- `__init__.py`
- `models/`
- `views/`
- `security/`

The manifest defines the module's metadata, dependencies, and data files.

### 4. Restart Odoo

Restart the Odoo server after placing the module in the configured addons directory.

### 5. Update the Apps List

1. Sign in to your Odoo database.
2. Enable Developer Mode.
3. Open the Apps menu.
4. Select **Update Apps List**.
5. Search for the Real Estate module.

### 6. Install the Module

Select the module and click **Install**.

After installation, use the configured menus to access the property management features.

### Alternative: Install or Update from the Command Line

From your Odoo server directory, run the following command using the appropriate Python executable and configuration file:

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE_NAME -i estate
```

Use `-i estate` for initial installation. To update an already installed module, use:

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE_NAME -u estate
```

Replace `YOUR_DATABASE_NAME` with your actual database name. These commands assume that Odoo can locate the module through its configured addons path and connect to the database.

## 🧠 Core Odoo Concepts

This project provides practical exposure to:

- **Custom Models:** Defining business entities using Odoo's ORM.
- **Field Types:** Working with character, text, date, numeric, selection, and relational fields.
- **Computed Fields:** Calculating property area with `@api.depends`.
- **Relational Fields:** Using `Many2one`, `Many2many`, and `One2many` relationships.
- **Business Logic:** Implementing actions and validation rules for property offers.
- **XML Views:** Creating list and form interfaces.
- **Window Actions and Menus:** Connecting application navigation to model views.
- **Access Control:** Defining model permissions through CSV configuration.
- **Data Integrity:** Applying constraints to enforce business rules.
- **Module Configuration:** Managing dependencies and data files through `__manifest__.py`.

## 🔮 Future Enhancements

Potential improvements include:

- Advanced property search, filtering, and sorting.
- More comprehensive property lifecycle management.
- Additional validation for property offers and transactions.
- Property statistics and dashboard views.
- Automated tests for models and business logic.
- Role-specific access permissions.
- Improved form layouts and user experience.

These items are proposed enhancements and are not represented as completed features.

## 🎯 Learning Outcomes

Through this workshop project, I gained practical experience in:

- Understanding Odoo's modular architecture and development workflow.
- Creating custom models and defining relationships between business entities.
- Connecting Python business logic with XML-based interfaces.
- Implementing computed fields, model constraints, and validation methods.
- Configuring access permissions and application navigation.
- Integrating a custom addon into an existing Odoo installation.

## 📚 Workshop Context

This repository documents development work completed during a **three-day Odoo development workshop**. It serves as a learning portfolio demonstrating foundational knowledge of ERP customization and hands-on experience building a custom Odoo module.

## 👩‍💻 Author

**Insa Saleem**

Computer Science Student | Odoo Development Learner | Web Development & Data Analytics Enthusiast

- **GitHub Profile:** [InsaSaleem](https://github.com/InsaSaleem)
- **Project Repository:** [odoo-real-estate-workshop](https://github.com/InsaSaleem/odoo-real-estate-workshop)

---

⭐ If you find this project useful for learning Odoo development, feel free to explore the source code and share your feedback.

*Built as part of my ongoing learning journey in software development and ERP systems.*
