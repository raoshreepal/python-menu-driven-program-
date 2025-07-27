## 📘 Python Inheritance Types - README Files

---

### ✅ 1. **Single Inheritance**

**Description:**
In single inheritance, a child class inherits from one parent class.

**Example Use Case:**
A `Car` class inherits from a `Vehicle` class.

**Key Benefits:**

* Simple
* Easy to manage

---

### ✅ 2. **Multiple Inheritance**

**Description:**
A class inherits from more than one parent class.

**Example Use Case:**
A `TechLead` inherits from `EmployeeDetails`, `Skills`, `ProjectInfo`, `Certification`, and `TeamHandling`.

**Key Benefits:**

* Combines multiple responsibilities
* Code reuse

**Important Note:**
Watch for method name conflicts (Method Resolution Order - MRO).

---

### ✅ 3. **Multilevel Inheritance**

**Description:**
A child inherits from a parent, and another class inherits from the child.

**Example Use Case:**
`Intern` → `JuniorDeveloper` → `SeniorDeveloper`

**Key Benefits:**

* Chain of command
* Reuse of intermediate functionality

---

### ✅ 4. **Hierarchical Inheritance**

**Description:**
Multiple classes inherit from a single parent class.

**Example Use Case:**
`ListOps`, `SetOps`, `DictOps`, `TupleOps` inherit from `DataStructureOps`

**Key Benefits:**

* Centralized base functionality
* Specialized child classes

---

### ✅ 5. **Hybrid Inheritance**

**Description:**
Combination of two or more types of inheritance.

**Example Use Case:**
`LoanAccount` inherits from `Loan` and `Account` where `Loan` already inherits from `Customer`

**Key Benefits:**

* Complex real-world modeling
* Flexible hierarchy
