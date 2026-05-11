import streamlit as st
import re

st.set_page_config(page_title="ChemCompute", layout="centered")

st.title("🧪 ChemCompute Digital Lab Assistant")

st.markdown("""
This tool helps students:

• Search **element properties**  
• Calculate **molar mass of molecules**  
• Predict **ionic or covalent bonds**  
• Identify **chemical reaction types**
""")

# -----------------------------
# Element Database
# -----------------------------

elements = {
    "H": ("Hydrogen", 1.008, "NonMetal", 2.20),
    "O": ("Oxygen", 16.00, "NonMetal", 3.44),
    "Na": ("Sodium", 22.99, "Metal", 0.93),
    "Cl": ("Chlorine", 35.45, "NonMetal", 3.16),
    "C": ("Carbon", 12.01, "NonMetal", 2.55),
    "Ne": ("Neon", 20.18, "NobleGas", 0)
}

# -----------------------------
# OOP + Encapsulation
# -----------------------------

class Element:

    def __init__(self, symbol, name, mass, group, electronegativity):
        self.symbol = symbol
        self.name = name
        self.mass = mass
        self.group = group
        self.__atomic_num = None
        self.electronegativity = electronegativity

    def display(self):
        return {
            "Symbol": self.symbol,
            "Name": self.name,
            "Atomic Mass": self.mass,
            "Group": self.group,
            "Electronegativity": self.electronegativity
        }


# -----------------------------
# Inheritance
# -----------------------------

class Metal(Element):
    def properties(self):
        return "Metal: Shiny and good conductor"


class NonMetal(Element):
    def properties(self):
        return "NonMetal: Poor conductor"


class NobleGas(Element):
    def properties(self):
        return "Noble Gas: Chemically inert"


# -----------------------------
# Sidebar Navigation
# -----------------------------

menu = st.sidebar.selectbox(
    "Choose Tool",
    ["Element Search", "Molar Mass Calculator", "Bond Predictor", "Reaction Predictor"]
)

# =============================
# Element Search
# =============================

if menu == "Element Search":

    st.header("🔎 Element Search")

    symbol = st.text_input("Enter Element Symbol (Example: Na, O)")

    if symbol:

        if symbol in elements:

            name, mass, group, en = elements[symbol]

            if group == "Metal":
                element = Metal(symbol, name, mass, group, en)

            elif group == "NonMetal":
                element = NonMetal(symbol, name, mass, group, en)

            else:
                element = NobleGas(symbol, name, mass, group, en)

            st.success("Element Found")

            st.table(element.display())

            st.info(element.properties())

        else:

            st.error("Element not found")


# =============================
# Formula Parser
# =============================

def count_atoms(formula):

    atoms = {}

    pattern = r'([A-Z][a-z]?)(\d*)'

    for (element, count) in re.findall(pattern, formula):

        count = int(count) if count else 1

        atoms[element] = atoms.get(element, 0) + count

    return atoms


# =============================
# Molar Mass Calculator
# =============================

def molar_mass(formula):

    atoms = count_atoms(formula)

    total = 0

    for element, count in atoms.items():

        if element in elements:
            total += elements[element][1] * count

    return total


if menu == "Molar Mass Calculator":

    st.header("⚛ Molar Mass Calculator")

    formula = st.text_input("Enter Chemical Formula (Example: H2O, CO2)")

    if formula:

        atoms = count_atoms(formula)

        st.subheader("Atom Count")

        st.table(atoms)

        mass = molar_mass(formula)

        st.success(f"Molar Mass = {mass} g/mol")


# =============================
# Bond Predictor
# =============================

def bond_type(e1, e2):

    en1 = elements[e1][3]
    en2 = elements[e2][3]

    diff = abs(en1 - en2)

    if diff > 1.7:
        return "Ionic Bond"

    else:
        return "Covalent Bond"


if menu == "Bond Predictor":

    st.header("🔗 Bond Predictor")

    e1 = st.text_input("First Element Symbol")
    e2 = st.text_input("Second Element Symbol")

    if e1 and e2:

        if e1 in elements and e2 in elements:

            result = bond_type(e1, e2)

            st.success(result)

        else:

            st.error("Element not found in database")


# =============================
# Reaction Predictor
# =============================

def reaction_type(reaction):

    match reaction:

        case "A+B":
            return "Synthesis Reaction"

        case "AB":
            return "Decomposition Reaction"

        case "Hydrocarbon + O2":
            return "Combustion Reaction"

        case _:
            return "Unknown Reaction"


if menu == "Reaction Predictor":

    st.header("🔥 Reaction Predictor")

    reaction = st.text_input("Enter Reaction Type (A+B, AB, Hydrocarbon + O2)")

    if reaction:

        result = reaction_type(reaction)

        st.success(result)