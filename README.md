### Image Classification Model 🧪 ChemCompute Edition


This repository contains a **Digital Lab Assistant** built with Streamlit. It follows a structured development lifecycle to help students explore chemical properties and reactions through code.

### 📌 Project Overview
The **ChemCompute Lab Assistant** is an educational tool that combines Chemistry with Python programming. It uses Object-Oriented Programming (OOP) to model chemical elements and Regular Expressions (Regex) to parse molecular formulas.


---

### 🔄 Project Development Cycle
This project was developed following a step-by-step Software Development Life Cycle (SDLC):


1. **Requirement Analysis:**

  Planning the conversion of core chemistry concepts (elements, molar mass, bonding) into a digital tool for 9th-grade students.
2.**Data Modeling:**

Creating a structured database of elements including atomic mass and electronegativity.

3.**Core Logic Development (OOP):
   
   ** Designing the `Element` parent class and `Metal`, `NonMetal`, and `NobleGas` child classes to demonstrate property inheritance.

   
4. **Function Engineering:**

 Implementing a `formula_parser` using Regex to break down complex molecular strings into individual atom counts.


7. **UI Integration:**

 Building an interactive dashboard using the Streamlit framework, featuring a sidebar-driven navigation menu.


6.**Testing & Validation:** 

  Verifying the logic with various chemical formulas (e.g., H2O, NaCl) and predicting reaction types.


7. **Deployment:**

   Organizing the repository for cloud hosting (e.g., Streamlit Cloud or GitHub Pages).

---

### 🛠️ Tech Stack
* **Language:** Python 3.x
* **Web Framework:** Streamlit
* **Pattern Matching:** Regular Expressions (re)
* **Programming Paradigm:** Object-Oriented Programming (OOP)

---


### 🚀 Getting Started

### 1. Clone the repository

Bash


git clone [https://github.com/AnzaKayani/ChemCompute.git](https://github.com/AnzaKayani/ChemCompute.git)
cd ChemCompute


### Install Dependencies :

Bash

pip install -r requirements.txt


### Run the Application:
Bash
streamlit run app.py


### 🧪 Database & Classes
The project implements a hierarchy of chemical families:

Parent Class: Element

Child Classes: Metal, NonMetal, and NobleGas

Included Elements: Hydrogen, Oxygen, Sodium, Chlorine, Carbon, and Neon


### 📊 Results & Demonstration
The following results were achieved during the testing phase of the ChemCompute project:

### 1. Element Search Result
* **Input:** Na
* **Output:** Name: Sodium, Mass: 22.99, Group: Metal, Property: "Shiny and good conductor"

### 2. Molar Mass Calculation
* **Input:** C6H12O6 (Glucose)*
* **Processing:** Regex identified 6 Carbon, 12 Hydrogen, and 6 Oxygen atoms.
* **Result:** `Molar Mass = 180.18 g/mol`

### 3. Bond Prediction
* **Input:** `Na` + `Cl`
* **Logic:** Electronegativity difference > 1.7
* **Result:** `Ionic Bond`

### 4. Reaction Classification
* **Input:** `A + B`
* **Result:** `Synthesis Reaction`



### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to improve the database or prediction algorithms.



