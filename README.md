# 🧪 ChemCompute Digital Lab Assistant

ChemCompute is an interactive, Streamlit-powered laboratory assistant designed for science students. This tool leverages Python's Object-Oriented Programming (OOP) and Regular Expressions (Regex) to help students explore chemical properties, calculate molecular metrics, and predict reaction outcomes.

## 🚀 Key Features

* **🔎 Element Search:** Explore a database of elements. [cite_start]The system uses OOP inheritance to categorize elements into **Metals**, **Non-Metals**, and **Noble Gases**, providing specific physical properties for each[cite: 80, 96, 99, 100].
* **⚛️ Molar Mass Calculator:** Enter chemical formulas (like `H2O` or `NaCl`). [cite_start]The application uses a Regex-based parser to count atoms and calculate total molar mass based on the element database[cite: 140, 142, 171].
* [cite_start]**🔗 Bond Predictor:** Input two element symbols to determine if they form an **Ionic** or **Covalent** bond based on their electronegativity difference[cite: 189, 196, 197].
* [cite_start]**🔥 Reaction Predictor:** Identify reaction types such as **Synthesis**, **Decomposition**, and **Combustion** based on simplified chemical notations[cite: 212, 218].

## 🛠️ Technical Implementation

* [cite_start]**Object-Oriented Programming:** Implements encapsulation (using private attributes for atomic numbers) and inheritance (specific `properties()` methods for different element groups)[cite: 87, 96].
* [cite_start]**Regular Expressions (Regex):** Utilizes the pattern `r'([A-Z][a-z]?)(\d*)'` to accurately parse element symbols and their respective counts from a formula string[cite: 142].
* **Streamlit Framework:** Provides a clean, sidebar-driven user interface for real-time calculation and data visualization.

## 📦 Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ChemCompute.git](https://github.com/YOUR_USERNAME/ChemCompute.git)
    cd ChemCompute
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## 🧪 Element Database
The current system includes data for:
* [cite_start]**Hydrogen (H):** Non-Metal, Mass 1.008 [cite: 3, 26-30]
* [cite_start]**Oxygen (O):** Non-Metal, Mass 16.00 [cite: 4, 31-35]
* [cite_start]**Sodium (Na):** Metal, Mass 22.99 [cite: 5, 36-40]
* [cite_start]**Chlorine (Cl):** Non-Metal, Mass 35.45 [cite: 6, 41-45]
* [cite_start]**Carbon (C):** Non-Metal, Mass 12.01 [cite: 7, 46-50]
* [cite_start]**Neon (Ne):** Noble Gas, Mass 20.18 [cite: 77-78, 132-137]
