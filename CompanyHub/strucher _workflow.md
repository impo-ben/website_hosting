Company Website

│

├── Landing Page

│      ├── Company Introduction

│      ├── Vision \& Mission

│      ├── Services

│      ├── Portfolio

│      └── Contact

│

├── Dashboard

│      ├── Company Statistics

│      ├── Projects Completed

│      ├── Employees

│      ├── Revenue Graphs

│      └── Recent Activities

│

├── Portfolio

│      ├── Images

│      ├── Videos

│      ├── Project Details

│      └── Categories

│

├── Shopping Store

│      ├── Products

│      ├── Categories

│      ├── Cart

│      ├── Checkout

│      ├── Orders

│      └── UPI Payment

│

├── User Accounts

│      ├── Register

│      ├── Login

│      ├── Profile

│      ├── Orders

│      └── Wishlist

│

└── Admin Panel

&#x20;      ├── Manage Company Info

&#x20;      ├── Upload Portfolio Images

&#x20;      ├── Add Products

&#x20;      ├── Manage Orders

&#x20;      ├── Manage Users

&#x20;      └── Dashboard Analytics









company\_site/



│

├── company\_site/

│      settings.py

│      urls.py

│      wsgi.py

│

├── home/

│      views.py

│      models.py

│      urls.py

│

├── portfolio/

│      models.py

│      views.py

│      urls.py

│

├── shop/

│      models.py

│      cart.py

│      views.py

│      urls.py

│

├── accounts/

│      models.py

│      views.py

│

├── dashboard/

│      views.py

│

├── payments/

│      views.py

│

├── media/

│      products/

│      portfolio/

│

├── static/

│      css/

│      js/

│      images/

│

├── templates/

│

└── manage.py



### 

### User Workflow



Visitor



↓



Home Page



↓



View Company



↓



Portfolio



↓



Shop



↓



Add to Cart



↓



Checkout



↓



UPI Payment



↓



Order Confirmation



↓



Admin receives Order





### Admin Workflow





Admin Login



↓



Dashboard



↓



Manage Company



↓



Upload Portfolio Images



↓



Add Products



↓



Update Stock



↓



View Orders



↓



Confirm Payment



↓



Dispatch Product





### Dashboard cards



Total Projects

Products

Orders

Revenue

Users



### Charts



Monthly Sales

Projects Completed

Visitors

Revenue



### Shopping Cart

Product



↓



Add to Cart



↓



Quantity



↓



Address



↓



Payment



↓



Success



↓



Invoice



### Login System



Use Django Authentication.



Register



↓



Email



Password



↓



Login



↓



Dashboard



### Image Upload



Django Admin already allows image upload.



Example:



Admin



↓



Add Product



↓



Choose Image



↓



Save



↓



Website Automatically Updates



### Product Page

Product Image



Name



Description



Price



★★★★★



Add to Cart



Buy Now



### Checkout Page

Shipping Address



Phone



Email



UPI Payment



↓



Place Order





### (UPI QR Code)



Display a QR Code.



Customer scans.



Pays.



Uploads screenshot.



Admin verifies.







### Project Workflow (High-Level)



Visitor

&#x20;  │

&#x20;  ▼

Home Page

&#x20;  │

&#x20;  ├── Company Introduction

&#x20;  ├── Portfolio

&#x20;  ├── Products (Phase 2)

&#x20;  ├── Contact

&#x20;  │

&#x20;  ▼

Register/Login

&#x20;  │

&#x20;  ▼

Shop

&#x20;  │

&#x20;  ▼

Cart

&#x20;  │

&#x20;  ▼

Checkout

&#x20;  │

&#x20;  ▼

QR Code Payment

&#x20;  │

&#x20;  ▼

Upload Payment Screenshot

&#x20;  │

&#x20;  ▼

Admin Verifies Payment

&#x20;  │

&#x20;  ▼

Order Confirmed



### Tech Stack



Backend



Django



Database



SQLite (development)



PostgreSQL (production)



Frontend



HTML



CSS



Bootstrap



JavaScript



Charts



Chart.js



Icons



Bootstrap Icons



Authentication



Django Auth



Media



Pillow



Deployment



Gunicorn



Nginx



Ubuntu VPS



### Future Features



Product search

Categories

Wishlist

Coupons

GST invoice

Order tracking

Email notifications

Admin analytics

Customer reviews

Inventory management

Delivery partner integration

PDF invoice generation

Multi-admin roles

REST API for a mobile app

