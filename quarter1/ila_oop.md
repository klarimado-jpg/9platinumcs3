# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation means keeping an object's data and the methods that manage that data together while controlling direct access to it. In the inventory system, a Product object can contaain properties such as name, price, and quantity, with methods like add_stock() and remove_stock(). This helps prevent accidental changes to important inventory data and keeps the program organized.

### 2. Abstraction
Abstraction means showing only the important features of an object while hiding unnecessary details. For example, a Product class can provide a sell_product() method without requiring the rest of the program to know exactly how the stock quantity is updated. This makes the inventory system easier to use and to understand.

### 3. Inheritance 
Inheritance allows one class to receive properties and methods from another class. For example, a general Product class could be the parent of FoodProduct and Householdproduct, allowing both classes to share properties such as name, price, and quantity. This reduces issues like repeated code and it makes it easier to add new types of products. 

### 4. Polymorphism
Polyomrphism allows different objects to use the same method name but perform the method differently. For example, FoodProduct and HouseholdProduct could both have a display_info() method, but each could display information specific to its product type. This makes the inventory system more flexible because the same method can work with different kinds of product.

### Example diagram:
product = name, price, quantity -> add_stock(), remove_stock(), display_info() -> FoodProduct/HouseholdProduct

### Reflection
Among the four pillars, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It would keep all the important information such as product prices and number of stocks which are protected and organized inside. Methods could control how inventory is added, removed, or updated which reduces accidental errors. Overall, encapsulation would make the system more organized and easier to maintain. 