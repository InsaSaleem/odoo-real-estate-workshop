# 🏡 Real Estate Management Module — Odoo 19

A custom **Real Estate Management module developed using Odoo 19** as part of a three-day Odoo development workshop. This project demonstrates practical experience with Odoo's ORM, Python models, XML views, relational fields, access control, and business logic.

The module focuses on managing property records, property types, tags, buyers, salespersons, and property offers within an existing Odoo environment.

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Accessing Odoo Locally](#-accessing-odoo-locally)
- [Odoo Concepts Practiced](#-odoo-concepts-practiced)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Workshop Context](#-workshop-context)
- [Author](#-author)

## 📌 Project Overview

The purpose of this project is to gain hands-on experience developing custom business applications using the Odoo ERP framework.

The module follows Odoo's modular architecture and uses Python models, XML-based user interfaces, relational fields, and access-control configuration to build a foundation for real estate management.

Development focused on the custom `estate` addon rather than modifying the entire Odoo source code.

## ✨ Features

### 🏠 Property Management
- Create and manage real estate property records.
- Store property descriptions, availability dates, expected prices, and selling prices.
- Record bedrooms, living area, and garden area.
- Calculate total property area using living and garden areas.
- Track property status.

### 🗂️ Property Types and Tags
- Categorize properties by type.
- Assign tags to properties.
- Configure color-coded property tags.
- Enforce unique names for property types and tags.

### 🤝 Property Offer Management
- Create offers associated with properties and buyers.
- Record offer prices and offer statuses.
- Accept or refuse offers through model actions.
- Update the associated property's buyer, selling price, and status when an offer is accepted.
- Apply validation rules to offer-related business logic.

### 👥 Relationships and Additional Information
- Link properties with buyers and salespersons.
- Connect properties with types, tags, and offers.
- Use Odoo relational fields to manage related records.
- Organize property information into structured form sections.

### 🖥️ Odoo User Interface
- XML-defined list and form views.
- Dedicated views for properties, property types, tags, and offers.
- Menu entries and window actions for navigation.
- Status bars for displaying property states.

### 🔐 Access Control and Data Validation
- Configure model permissions through `ir.model.access.csv`.
- Define access for internal users.
- Apply constraints for property prices and unique names.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Odoo 19 | ERP framework and application platform |
| Python | Model definitions and business logic |
| Odoo ORM | Database operations and relationships |
| XML | Views, actions, and menu configuration |
| PostgreSQL | Database backend |
| CSV | Model access-control configuration |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

The work shown in this project is organized within the custom `estate` addon.

```text
Workshop/
└── estate/
    ├── __pycache__/
    ├── models/
    ├── security/
    ├── views/
    ├── __init__.py
    └── __manifest__.py
```

### Main Files and Directories

| File or directory | Purpose |
|---|---|
| `estate/` | Main custom real estate addon |
| `estate/models/` | Python models and business logic |
| `estate/security/` | Access-control configuration |
| `estate/views/` | XML views, actions, and menus |
| `estate/__init__.py` | Initializes the Python package and imports model modules |
| `estate/__manifest__.py` | Defines module metadata, dependencies, and data files |
| `estate/__pycache__/` | Python-generated cache files; these are not source files and generally should not be committed |

**Project scope:** My development work focuses on the files and folders inside the `estate` addon shown above. The module is intended to run within an existing Odoo 19 installation.

## ⚙️ Prerequisites

Before running the module, ensure you have:

- Odoo 19 installed and configured.
- Python available in your environment.
- PostgreSQL configured for Odoo.
- An accessible Odoo database.
- Visual Studio Code or another code editor.

### ⚠️ Important: Run as Administrator

**Always run Visual Studio Code and the relevant terminal as Administrator** when working with an Odoo installation located under `C:\Program Files`, if administrator permissions are required.

This helps avoid permission errors when accessing or modifying protected installation files. Use administrator privileges only for trusted code and commands.

## 🚀 Installation and Setup

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/InsaSaleem/odoo-real-estate-workshop.git
```

Navigate to the project directory:

```bash
cd odoo-real-estate-workshop
```

### 2. Place the Addon in an Odoo Addons Directory

Copy the `estate` folder into an addons directory that is included in your Odoo configuration.

For example:

```text
C:\Program Files\Odoo 19.0\server\addons\estate
```

Alternatively, use a separate custom addons directory and add it to the `addons_path` setting in your Odoo configuration file.

### 3. Verify the Addon

Ensure the `estate` folder contains:

- `__manifest__.py`
- `__init__.py`
- `models/`
- `security/`
- `views/`

The manifest must reference the relevant XML and CSV files so Odoo can load them.

### 4. Start or Restart Odoo

Start the Odoo server using your existing configuration. Restart it after adding or changing addon files when necessary.

If your installation is under `C:\Program Files`, open the terminal with the required administrator permissions.

### 5. Open Odoo in Your Browser

Once the Odoo server is running, open the local application:

**[Open Odoo Apps — http://localhost:8069/odoo/apps](http://localhost:8069/odoo/apps)**

This address works when Odoo is running on your own computer and listening on port `8069`.

### 6. Update the Apps List

1. Log in to your Odoo database.
2. Enable Developer Mode.
3. Open the Apps menu.
4. Select **Update Apps List**.
5. Search for the Real Estate module.

### 7. Install the Module

Select the Real Estate module and click **Install**.

After installation, use the module's menus to access the available property management features.

### Alternative: Install or Update Through the Command Line

From your Odoo server directory, run the appropriate command using your Python executable and Odoo configuration file.

For a first-time installation:

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE_NAME -i estate
```

For an existing installation:

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE_NAME -u estate
```

Replace `YOUR_DATABASE_NAME` with your actual Odoo database name. These commands assume that the `estate` addon is available through the configured addons path and that Odoo can connect to the database.

## 🌐 Accessing Odoo Locally

The project is developed and tested through a local Odoo environment.

- **Local Apps URL:** [http://localhost:8069/odoo/apps](http://localhost:8069/odoo/apps)
- **Host:** `localhost`
- **Port:** `8069`
- **Application:** Odoo 19

> **Note:** The local URL is accessible only when the Odoo server is running on your computer. Other users cannot access your local `localhost` address through your GitHub repository.

## 🧠 Odoo Concepts Practiced

- **Custom Models:** Defining business entities with Odoo's ORM.
- **Field Types:** Using character, text, date, numeric, selection, and relational fields.
- **Computed Fields:** Calculating total property area with `@api.depends`.
- **Relational Fields:** Working with `Many2one`, `Many2many`, and `One2many`.
- **Business Logic:** Implementing offer actions and validation rules.
- **XML Views:** Designing list and form interfaces.
- **Window Actions and Menus:** Connecting navigation to model views.
- **Access Control:** Configuring model permissions using CSV files.
- **Data Integrity:** Applying constraints to enforce business rules.
- **Module Configuration:** Defining dependencies and data files through `__manifest__.py`.

## 🔮 Future Improvements

Potential enhancements include:

- Advanced property search and filtering.
- Improved property lifecycle management.
- Additional property statistics and dashboard views.
- Automated tests for models and business logic.
- More granular access permissions.
- Improved form layouts and user experience.

These are planned improvements rather than features claimed as completed.

## 🎯 Learning Outcomes

Through this workshop project, I gained practical experience in:

- Understanding Odoo's modular architecture.
- Creating custom Python models and relational fields.
- Connecting business logic with XML-based interfaces.
- Implementing computed fields and validation rules.
- Configuring access permissions and navigation.
- Integrating a custom addon into an existing Odoo installation.
- Working with Git and GitHub to manage project source code.

## 📚 Workshop Context

This repository documents development work completed during a **three-day Odoo development workshop**. It serves as a learning portfolio demonstrating foundational experience in ERP customization and custom module development.

## 👩‍💻 Author

**Insa Saleem**

Computer Science Student | Odoo Development Learner | Web Development & Data Analytics Enthusiast

- **GitHub Profile:** [InsaSaleem](https://github.com/InsaSaleem)
- **Project Repository:** [odoo-real-estate-workshop](https://github.com/InsaSaleem/odoo-real-estate-workshop)

---

⭐ If you find this project useful for learning Odoo development, feel free to explore the source code and share your feedback.

*Built as part of my ongoing learning journey in software development and ERP systems.*
