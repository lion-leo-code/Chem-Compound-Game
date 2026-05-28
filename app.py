# app.py
from flask import Flask, render_template
import json # To convert Python sets to JSON-serializable lists

app = Flask(__name__)

# --- Game Data (from your original Python code) ---
elementNames = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
    "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
    "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]
elementSymbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
valencies = [
    [-1, +1],         # Hydrogen
    [0],              # Helium
    [0],              # Lithium (simplified for game, was [+1])
    [+2],             # Beryllium
    [-3, +3],         # Boron
    [+2, +4],         # Carbon
    [-3, +1, +3, +5], # Nitrogen
    [-2],             # Oxygen
    [-1],             # Fluorine
    [0],              # Neon
    [+1],             # Sodium
    [+2],             # Magnesium
    [+3],             # Aluminium
    [-4, +2, +4],     # Silicon
    [-3, +1, +3, +5], # Phosphorus
    [-2, +2, +4, +6], # Sulfur
    [-1, +1, +3, +5, +7], # Chlorine
    [0],              # Argon
    [+1],             # Potassium
    [+2],             # Calcium
    [+3],             # Scandium
    [+2, +3, +4],     # Titanium
    [+2, +3, +4, +5], # Vanadium
    [+2, +3, +6],     # Chromium
    [+2, +3, +4, +7], # Manganese
    [+2, +3],         # Iron
    [+2, +3],         # Cobalt
    [+1, +2],         # Nickel
    [+1, +2],         # Copper
    [+2],             # Zinc
    [+1, +2, +3],     # Gallium
    [+2, +4],         # Germanium
    [-3, +3, +5],     # Arsenic
    [-2, +2, +4, +6], # Selenium
    [-1, +1, +5],     # Bromine
    [0],              # Krypton
    [+1],             # Rubidium
    [+2],             # Strontium
    [+3],             # Yttrium
    [+2, +3, +4],     # Zirconium
    [+3, +5],         # Niobium
    [+2, +3, +4, +6], # Molybdenum
    [+7],             # Technetium
    [+2, +3, +4, +6, +8], # Ruthenium
    [+3],             # Rhodium
    [+2, +4],         # Palladium
    [+1],             # Silver
    [+2],             # Cadmium
    [+1, +3],         # Indium
    [+2, +4],         # Tin
    [+3, +5],         # Antimony
    [+2, +4, +6],     # Tellurium
    [-1, +1, +5],     # Iodine
    [0],              # Xenon
    [+1],             # Caesium
    [+2],             # Barium
    [+3],             # Lanthanum
    [+3, +4],         # Cerium
    [+3, +4],         # Praseodymium
    [+3],             # Neodymium
    [+3],             # Promethium
    [+3],             # Samarium
    [+3],             # Europium
    [+3],             # Gadolinium
    [+3],             # Terbium
    [+3],             # Dysprosium
    [+3],             # Holmium
    [+3],             # Erbium
    [+3],             # Thulium
    [+2, +3],         # Ytterbium
    [+3],             # Lutetium
    [+4],             # Hafnium
    [+5],             # Tantalum
    [+6],             # Tungsten
    [+7],             # Rhenium
    [+4, +6, +8],     # Osmium
    [+3, +4],         # Iridium
    [+2, +4],         # Platinum
    [+1, +3],         # Gold
    [+1, +2],         # Mercury
    [+1, +3],         # Thallium
    [+2, +4],         # Lead
    [+3, +5],         # Bismuth
    [+2, +4, +6],     # Polonium
    [-1, +1, +3, +5, +7], # Astatine
    [0],              # Radon
    [+1],             # Francium
    [+2],             # Radium
    [+3],             # Actinium
    [+4],             # Thorium
    [+5],             # Protactinium
    [+3, +4, +6],     # Uranium
    [+3, +4, +6, +7], # Neptunium
    [+3, +4, +6],     # Plutonium
    [+3, +4, +6],     # Americium
    [+3, +4],         # Curium
    [+3],             # Berkelium
    [+3],             # Californium
    [+3],             # Einsteinium
    [+3],             # Fermium
    [+2, +3],         # Mendelevium
    [+2, +3],         # Nobelium
    [+3],             # Lawrencium
    [+4],             # Rutherfordium
    [+5],             # Dubnium
    [+6],             # Seaborgium
    [+7],             # Bohrium
    [+8],             # Hassium
    [0],              # Meitnerium (unknown)
    [0],              # Darmstadtium (unknown)
    [0],              # Roentgenium (unknown)
    [0],              # Copernicium (unknown)
    [0],              # Nihonium (unknown)
    [0],              # Flerovium (unknown)
    [0],              # Moscovium (unknown)
    [0],              # Livermorium (unknown)
    [0],              # Tennessine (unknown)
    [0]               # Oganesson (unknown)
]
NOBLE_GASES = {"He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"}
compounds = [
    {"formula": "H₂O", "atoms": {"H": 2, "O": 1}, "name": "Water"},
    {"formula": "CO₂", "atoms": {"C": 1, "O": 2}, "name": "Carbon Dioxide"},
    {"formula": "NaCl", "atoms": {"Na": 1, "Cl": 1}, "name": "Table Salt"},
    {"formula": "CH₄", "atoms": {"C": 1, "H": 4}, "name": "Methane"},
    {"formula": "NH₃", "atoms": {"N": 1, "H": 3}, "name": "Ammonia"},
    {"formula": "HCl", "atoms": {"H": 1, "Cl": 1}, "name": "Hydrochloric Acid"},
    {"formula": "O₂", "atoms": {"O": 2}, "name": "Oxygen Gas"},
    {"formula": "N₂", "atoms": {"N": 2}, "name": "Nitrogen Gas"},
    {"formula": "Cl₂", "atoms": {"Cl": 2}, "name": "Chlorine Gas"},
    {"formula": "H₂", "atoms": {"H": 2}, "name": "Hydrogen Gas"},
    {"formula": "CO", "atoms": {"C": 1, "O": 1}, "name": "Carbon Monoxide"},
    {"formula": "SO₂", "atoms": {"S": 1, "O": 2}, "name": "Sulfur Dioxide"},
    {"formula": "MgO", "atoms": {"Mg": 1, "O": 1}, "name": "Magnesium Oxide"},
    {"formula": "Al₂O₃", "atoms": {"Al": 2, "O": 3}, "name": "Aluminum Oxide"}
]

@app.route("/")
def index():
    # Pass all necessary data to the HTML template
    return render_template(
        "index.html",
        element_names=json.dumps(elementNames),
        element_symbols=json.dumps(elementSymbols),
        valencies=json.dumps(valencies),
        noble_gases=json.dumps(list(NOBLE_GASES)), # Convert set to list for JSON serialization
        compounds_data=json.dumps(compounds)
    )
if __name__ == "__main__":
    app.run(debug=True) # debug=True allows for automatic reloading on code changes