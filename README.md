# 🏡 Odoo Real Estate Management Module

A custom **Real Estate Management Module developed using Odoo 19**, as part of a three-day Odoo development workshop. This project explores Odoo's ORM, custom models, XML views, menu actions, relational fields, access control, and business logic.

The module provides a foundation for managing property records, property types, tags, buyers, salespersons, and property offers within the Odoo framework.

## 📌 Project Overview

The purpose of this project is to gain practical experience in developing custom business applications using the Odoo framework. It demonstrates how Python models, XML-based user interfaces, and access-control rules work together to create an integrated application.

The project follows Odoo's modular architecture and uses its built-in ORM to define data models and relationships between properties, offers, contacts, and users.

## ✨ Key Features

### 🏠 Property Management
- Create and manage real estate property records.
- Store property descriptions, availability dates, expected prices, and selling prices.
- Record the number of bedrooms, living area, and garden area.
- Calculate total property area automatically from living and garden areas.
- Track property status through a selection field.

### 🗂️ Property Types and Tags
- Organize properties by property type.
- Assign tags to properties for easier categorization.
- Configure color-coded property tags.
- Apply uniqueness constraints to property type and tag names.

### 🤝 Offer Management
- Create property offers associated with properties and buyers.
- Record offer prices and offer statuses.
- Implement actions to accept or refuse offers.
- Update the associated property's buyer, selling price, and status when an offer is accepted.
- Include validation checks for offer-related business rules.

### 👥 Relationships and Additional Information
- Link properties with salesperson and buyer records.
- Use relational fields to connect properties, types, tags, offers, users, and contacts.
- Display additional property information through organized form sections.

### 🖥️ Odoo User Interface
- XML-defined list and form views for property records.
- Dedicated views for property types, tags, and offers.
- Menu entries and window actions for navigating the application.
- A status bar for displaying property states.

### 🔐 Access Control and Data Validation
- Configure model-level permissions through `ir.model.access.csv`.
- Define access for internal users using Odoo's built-in user group.
- Apply database constraints to validate property prices and enforce unique names.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Odoo 19 | ERP framework and application platform |
| Python | Business logic and model definitions |
| XML | Views, actions, and menu configuration |
| PostgreSQL | Odoo's underlying database |
| Odoo ORM | Database operations and model relationships |
| CSV | Model access-control configuration |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project documentation |

## 📂 Project Structure

```text
odoo-real-estate-workshop/
│
├── estate/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── estate_property.py
│   │   ├── estate_property_offer.py
│   │   ├── estate_property_tag.py
│   │   └── estate_property_type.py
│   │
│   ├── security/
│   │   └── ir.model.access.csv
│   │
│   ├── views/
│   │   ├── estate_menus.xml
│   │   ├── estate_property_views.xml
│   │   ├── estate_property_offer_views.xml
│   │   ├── estate_property_tag_views.xml
│   │   ├── estate_property_type_views.xml
│   │   └── res_users_views.xml
│   │
│   ├── __init__.py
│   └── __manifest__.py
│
└── README.md
```

## ⚙️ Prerequisites

Before installing the module, ensure you have:

- Odoo 19 installed and configured.
- Python available in your environment.
- PostgreSQL configured for your Odoo installation.
- Access to an Odoo database.
- Git, if you want to clone the repository.

**Note:** This project is intended to be installed as a custom Odoo addon within an existing Odoo environment, rather than as a standalone Python application.

## 🚀 Installation and Setup

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/InsaSaleem/odoo-real-estate-workshop.git
```

Navigate to the repository:

```bash
cd odoo-real-estate-workshop
```

### 2. Copy the Module into Your Odoo Addons Directory

Copy the `estate` folder into a directory included in your Odoo `addons_path`.

For example, on a Windows installation:

```text
C:\Program Files\Odoo 19.0\server\addons\estate
```

Alternatively, you can keep the module in a separate custom addons directory and add that directory to your Odoo configuration.

### 3. Verify the Module Files

Make sure the `estate` folder contains:

- `__manifest__.py`
- `__init__.py`
- `models/`
- `views/`
- `security/`

The manifest declares the module dependency and lists the XML and CSV files that Odoo must load.

### 4. Restart the Odoo Server

Restart your Odoo server after adding the module so the server can detect the custom addon.

### 5. Update the Apps List

1. Log in to your Odoo database.
2. Enable Developer Mode.
3. Open the Apps menu.
4. Update the Apps List.
5. Search for **Real Estate**.

### 6. Install the Module

Select the Real Estate module and click **Install**.

Once installed successfully, open the module's menus to access the available property management features.

### Alternative: Install or Update Through the Command Line

From your Odoo server directory, use the appropriate Python executable and configuration file:

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE_NAME -u estate
```

Replace `YOUR_DATABASE_NAME` with your actual Odoo database name. The `-u estate` option updates the module; use `-i estate` instead if you are installing it for the first time through the command line.

The command assumes that `estate` is available through the configured addons path and that the server can connect to the specified database.

## 🧠 Concepts Practiced

This project provided practical exposure to the following Odoo development concepts:

- **Custom Models:** Creating business entities with Odoo's ORM.
- **Field Types:** Working with character, text, date, numeric, selection, and relational fields.
- **Computed Fields:** Using `@api.depends` to calculate total property area.
- **Relational Data:** Implementing `Many2one`, `Many2many`, and `One2many` relationships.
- **Business Logic:** Defining Python methods and validation rules for property offers.
- **XML Views:** Designing list and form views for Odoo models.
- **Window Actions and Menus:** Connecting application navigation to model views.
- **Access Control:** Configuring model permissions through CSV files.
- **Data Integrity:** Applying database constraints to enforce business rules.
- **Module Configuration:** Defining dependencies and data files through `__manifest__.py`.

## 🎯 Learning Outcomes

Through this workshop project, I gained practical experience in:

- Understanding Odoo's modular architecture and development workflow.
- Creating custom models and defining relationships between business entities.
- Connecting Python business logic with XML-based interfaces.
- Working with computed fields, model constraints, and validation methods.
- Configuring module access permissions and application navigation.
- Understanding how custom addons integrate with an existing Odoo installation.

## 🔮 Future Improvements

Potential enhancements for future development include:

- Adding advanced property search and filtering.
- Improving property lifecycle transitions and offer validation.
- Introducing additional property statistics and dashboard views.
- Adding automated tests for models and business logic.
- Enhancing access permissions with role-specific security rules.
- Improving form layouts and user experience.

These are potential future enhancements and are not claimed as completed features.

## 📚 Workshop Context

This repository documents practical development work completed during a **three-day Odoo workshop**. It serves as a learning portfolio demonstrating my introduction to ERP customization and hands-on experience with Odoo module development.

## 👩‍💻 Author

**Insa Saleem**

Computer Science Student | Odoo Development Learner | Web Development & Data Analytics Enthusiast

- **GitHub:** [InsaSaleem](https://github.com/InsaSaleem)
- **Repository:** [odoo-real-estate-workshop](https://github.com/InsaSaleem/odoo-real-estate-workshop)

---

⭐ If you find this project useful for learning Odoo development, feel free to explore the code and share your feedback.

*Built as part of my ongoing journey in software development, ERP systems, and practical technology projects.*
#   o d o o - r e a l - e s t a t e - w o r k s h o p  
 #   o d o o - r e a l - e s t a t e - w o r k s h o p  
 #   o d o o - r e a l - e s t a t e - w o r k s h o p  
 