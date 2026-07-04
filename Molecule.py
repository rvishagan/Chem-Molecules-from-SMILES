"""
CS3C, Final, Molecule implementation with Graph
Ragavishagan Rajasekar
"""
from graph import *

class Bond(Edge):

    def __init__(self, id_, src, dst, bond_type, weight = None):
        super().__init__(id_, src, dst, weight)
        self.bond_type = self.get_bond_type(bond_type)

    def reset_weight(self):
        self.weight = None

    def __str__(self):
        if self.bond_type == (1, "Single"):
            return f"{self.id[0]}-{self.id[1]}"
        elif self.bond_type == (1.5, "Aromatic"):
            return f"{self.id[0]}≃{self.id[1]}"
        elif self.bond_type == (2, "Double"):
            return f"{self.id[0]}={self.id[1]}"
        elif self.bond_type == (3, "Triple"):
            return f"{self.id[0]}≡{self.id[1]}"


    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_bond_type(bond_type):
        # Old way no longer used
        # bond_dictionary = {
        #     "Single": (1, "Single"),
        #     "Aromatic": (1.5, "Aromatic"),
        #     "Double": (2, "Double"),
        #     "Triple": (3, "Triple"),
        #     1: (1, "Single"),
        #     1.5: (1.5, "Aromatic"),
        #     2: (2, "Double"),
        #     3: (3, "Triple"),
        #     (1, "Single") : (1, "Single"),
        #     (1.5, "Aromatic") : (1.5, "Aromatic"),
        #     (2, "Double") : (2, "Double"),
        #     (3, "Triple") : (3, "Triple")
        # }
        bond_terminology = ((1, "Single"), (1.5, "Aromatic"), (2, "Double"), (3, "Triple"))
        if bond_type in bond_terminology:
            return bond_type
        for bond_name in bond_terminology:
            if bond_type in bond_name:
                return bond_name

class Atom(Vertex):

    EdgeClass = Bond
    def __init__(self, element, atom_index):
        self.element = self.get_element_type(element)
        self.bonds = set()
        self.path = Vertex.Path()
        self.atom_index = atom_index

    @property
    def out_edges(self):
        return self.bonds

    @out_edges.setter
    def out_edges(self, data):
        self.bonds = data

    @property
    def atomic_number(self):
        return self.element[0]

    @staticmethod
    def get_element_type(element):
        element_terminology = {
            (1, "H", "Hydrogen"), (2, "He", "Helium"), (3, "Li", "Lithium"), (4, "Be", "Beryllium"),
            (5, "B", "Boron"), (6, "C", "Carbon"), (7, "N", "Nitrogen"), (8, "O", "Oxygen"), (9, "F", "Fluorine"),
            (10, "Ne", "Neon"), (11, "Na", "Sodium"), (12, "Mg", "Magnesium"), (13, "Al", "Aluminum"),
            (14, "Si", "Silicon"), (15, "P", "Phosphorus"), (16, "S", "Sulfur"), (17, "Cl", "Chlorine"),
            (18, "Ar", "Argon"), (19, "K", "Potassium"), (20, "Ca", "Calcium"), (21, "Sc", "Scandium"),
            (22, "Ti", "Titanium"), (23, "V", "Vanadium"), (24, "Cr", "Chromium"), (25, "Mn", "Manganese"),
            (26, "Fe", "Iron"), (27, "Co", "Cobalt"), (28, "Ni", "Nickel"), (29, "Cu", "Copper"), (30, "Zn", "Zinc"),
            (31, "Ga", "Gallium"), (32, "Ge", "Germanium"), (33, "As", "Arsenic"), (34, "Se", "Selenium"),
            (35, "Br", "Bromine"), (36, "Kr", "Krypton"), (37, "Rb", "Rubidium"), (38, "Sr", "Strontium"),
            (39, "Y", "Yttrium"), (40, "Zr", "Zirconium"), (41, "Nb", "Niobium"), (42, "Mo", "Molybdenum"),
            (43, "Tc", "Technetium"), (44, "Ru", "Ruthenium"), (45, "Rh", "Rhodium"), (46, "Pd", "Palladium"),
            (47, "Ag", "Silver"), (48, "Cd", "Cadmium"), (49, "In", "Indium"), (50, "Sn", "Tin"),
            (51, "Sb", "Antimony"), (52, "Te", "Tellurium"), (53, "I", "Iodine"), (54, "Xe", "Xenon"),
            (55, "Cs", "Cesium"), (56, "Ba", "Barium"), (57, "La", "Lanthanum"), (58, "Ce", "Cerium"),
            (59, "Pr", "Praseodymium"), (60, "Nd", "Neodymium"), (61, "Pm", "Promethium"), (62, "Sm", "Samarium"),
            (63, "Eu", "Europium"), (64, "Gd", "Gadolinium"), (65, "Tb", "Terbium"), (66, "Dy", "Dysprosium"),
            (67, "Ho", "Holmium"), (68, "Er", "Erbium"), (69, "Tm", "Thulium"), (70, "Yb", "Ytterbium"),
            (71, "Lu", "Lutetium"), (72, "Hf", "Hafnium"), (73, "Ta", "Tantalum"), (74, "W", "Tungsten"),
            (75, "Re", "Rhenium"), (76, "Os", "Osmium"), (77, "Ir", "Iridium"), (78, "Pt", "Platinum"),
            (79, "Au", "Gold"), (80, "Hg", "Mercury"), (81, "Tl", "Thallium"), (82, "Pb", "Lead"),
            (83, "Bi", "Bismuth"), (84, "Po", "Polonium"), (85, "At", "Astatine"), (86, "Rn", "Radon"),
            (87, "Fr", "Francium"), (88, "Ra", "Radium"), (89, "Ac", "Actinium"), (90, "Th", "Thorium"),
            (91, "Pa", "Protactinium"), (92, "U", "Uranium"), (93, "Np", "Neptunium"), (94, "Pu", "Plutonium"),
            (95, "Am", "Americium"), (96, "Cm", "Curium"), (97, "Bk", "Berkelium"), (98, "Cf", "Californium"),
            (99, "Es", "Einsteinium"), (100, "Fm", "Fermium"), (101, "Md", "Mendelevium"), (102, "No", "Nobelium"),
            (103, "Lr", "Lawrencium"), (104, "Rf", "Rutherfordium"), (105, "Db", "Dubnium"),
            (106, "Sg", "Seaborgium"), (107, "Bh", "Bohrium"), (108, "Hs", "Hassium"), (109, "Mt", "Meitnerium"),
            (110, "Ds", "Darmstadtium"), (111, "Rg", "Roentgenium"), (112, "Cn", "Copernicium"),
            (113, "Nh", "Nihonium"), (114, "Fl", "Flerovium"), (115, "Mc", "Moscovium"), (116, "Lv", "Livermorium"),
            (117, "Ts", "Tennessine"), (118, "Og", "Oganesson")
        }
        if element in element_terminology:
            return element
        for element_name in element_terminology:
            if element in element_name:
                return element_name

    @staticmethod
    def is_smiles_element(element):
        smiles_terminology = {"N", "C", "O", "I", "P", "Cl", "Br", "F", "S", "B"}
        if element in smiles_terminology:
            return True

    def __str__(self):
        return f"{self.__class__.__name__}=({self.id}, {sorted([str(bond) for bond in self.bonds])})"


    @property
    def id(self):
        return str(self.element[1]) + str(self.atom_index)

    def add_bond(self, dst, bond_type):
        id_ = Edge.edge_id(self, dst)
        bond = super().add_edge(id_, dst, self.EdgeClass.get_bond_type(bond_type))
        dst.bonds.add(bond)
        return bond

    def add_edge(self, id_, dst, weight=1):
        return self.add_bond(dst, weight)



class Molecule(Graph):

    VertexClass = Atom

    def __init__(self, smiles=""):
        super().__init__(smiles)
        self._parse_smiles(self.id)

    @property
    def atoms(self):
        return self.vertices

    @property
    def bonds(self):
        return self.edges

    def __str__(self):
        vs = "\n".join(sorted([str(v) for v in self.vertices.values()]))
        es = "\n".join(sorted([str(e) for e in self.edges.values()]))
        return f"Molecule Smiles: {self.id}\n" \
               f"Atoms: \n{vs}\n" \
               f"Bonds: \n{es}"


    def _parse_smiles(self, smiles):
        i = 0
        atoms_dict = dict()
        ring_list = []

        while i < len(smiles):
            if smiles[i:i + 2] in ("Cl", "Br"):
                atoms_dict[i] = self.add_atom(smiles[i:i + 2])
                i += 2
            elif smiles[i].capitalize() in ("B", "C", "N", "O", "P", "S", "F", "I"):
                atoms_dict[i] = self.add_atom(smiles[i].capitalize())
                i += 1
            elif smiles[i].isdigit():
                ring_marker_present = False
                for ring_data in ring_list:
                    if smiles[i] == ring_data[0]:
                        ring_data[1].append(i)
                        ring_marker_present = True
                        break
                if not ring_marker_present:
                    ring_list.append((smiles[i], [i]))
                i += 1
            else:
                i += 1


        atom_list = list(atoms_dict.keys())

        def find_bond_type(section):
            integer_index = []
            selection_index = 0
            for character in section:
                if character.isdigit():
                    integer_index.append(selection_index)
                selection_index += 1
            if len(integer_index) == 0:
                if "=" in section:
                    bond_type = 2
                elif ":" in section:
                    bond_type = 1.5
                elif "#" in section:
                    bond_type = 3
                else:
                    bond_type = 1
            else:
                bond_type = find_bond_type(section[(integer_index[0]+1):])
                return bond_type
            return bond_type

        def find_ring_bond_type(section):
            integer_index = []
            selection_index = 0
            for character in section:
                if character.isdigit():
                    integer_index.append(selection_index)
                selection_index += 1
            if len(integer_index) == 0:
                if "=" in section:
                    bond_type = 2
                elif ":" in section:
                    bond_type = 1.5
                elif "#" in section:
                    bond_type = 3
                else:
                    bond_type = 1
            else:
                bond_type = find_ring_bond_type(section[:(integer_index[0])])
                return bond_type
            return bond_type

        def create_bond(smiles_indices, bond_type):
            if smiles[smiles_indices[0]].islower() and smiles[smiles_indices[1]].islower():
                self.add_bond(atoms_dict[smiles_indices[0]], atoms_dict[smiles_indices[1]], 1.5)
            else:
                self.add_bond(atoms_dict[smiles_indices[0]], atoms_dict[smiles_indices[1]], bond_type)

        def find_ring_atom(smiles_index):
            j = smiles_index
            found_atom = False
            while not found_atom:
                j -= 1
                if smiles[j].isalpha():
                    found_atom = True
            return j, smiles[j:smiles_index+1]

        for i in range(len(atom_list)-1):
            section = smiles[atom_list[i]:atom_list[i+1]]
            bond_type = find_bond_type(section)
            if ")" not in section:
                create_bond((atom_list[i], atom_list[i+1]), bond_type)
            if ")(" in section:
                branches_to_end = section.count("(") - section.count(")")
                l = i
                while branches_to_end < 1:
                    l -= 1
                    temp_section = smiles[atom_list[l]:atom_list[i+1]]
                    branches_to_end = temp_section.count("(") - temp_section.count(")")
                bond_type = find_bond_type(smiles[atom_list[i]:atom_list[i+1]])
                create_bond((atom_list[i+1], atom_list[l]), bond_type)


            elif "(" in section:
                if "((" in section:
                    branches_to_end = section.count("(") - section.count(")")
                    j = i
                    while branches_to_end > 1:
                        j += 1
                        temp_section = smiles[atom_list[i]:atom_list[j]]
                        branches_to_end = temp_section.count("(") - temp_section.count(")")
                    bond_type = find_bond_type(smiles[atom_list[j - 1]:atom_list[j]])
                    create_bond((atom_list[i], atom_list[j]), bond_type)

                branches_to_end = section.count("(") - section.count(")")
                k=i
                while branches_to_end > 0:
                    k += 1
                    temp_section = smiles[atom_list[i]:atom_list[k]]
                    branches_to_end = temp_section.count("(") - temp_section.count(")")

                bond_type = find_bond_type(smiles[atom_list[k-1]:atom_list[k]])
                create_bond((atom_list[i], atom_list[k]), bond_type)


        for ring_data in ring_list:
            paired_ring_indicator_index_list = list(zip(ring_data[1][0::2], ring_data[1][1::2]))
            for paired_ring_indicator in paired_ring_indicator_index_list:
                first_atom_index, first_section = find_ring_atom(paired_ring_indicator[0])
                second_atom_index, second_section = find_ring_atom(paired_ring_indicator[1])
                bond_type = max(find_ring_bond_type(first_section), find_ring_bond_type(second_section))
                bond_index = (first_atom_index, second_atom_index)
                create_bond(bond_index, bond_type)


    def add_atom(self, element):
        element = self.VertexClass.get_element_type(element)
        count = 1
        for atom in self.atoms.values():
            if atom.element == element:
                count += 1
        new_atom = self.VertexClass(element, count)
        self.atoms[new_atom.id] = new_atom
        return new_atom.id

    def add_bond(self, atom1, atom2, bond_type):
        """
        Using src and dst is slightly misleading as there is no direction in this molecular graph.
        This graph is technically built off of a directed graph because edge is directed and so is Bond for
        it inherits from edge. To make sure that the direction actually means something, make it go from
        heavier element to lighter element (which has some significance in chemistry) and from earlier index to
        later index for same element.
        """

        if self.atoms[atom1].atomic_number > self.atoms[atom2].atomic_number:
            self.add_edge(atom1, atom2, bond_type)
        elif self.atoms[atom1].atomic_number < self.atoms[atom2].atomic_number:
            self.add_edge(atom2, atom1, bond_type)
        elif self.atoms[atom1].atom_index < self.atoms[atom2].atom_index:
            self.add_edge(atom1, atom2, bond_type)
        else:
            self.add_edge(atom2, atom1, bond_type)

    def reset_weights(self):
        for bond in self.bonds.values():
            bond.reset_weight()

    def wiener_index(self):
        for bond in self.bonds.values():
            bond.weight = 1 # Every bond is 1 bond so it is one weight
        distances = self.floyd_warshall()
        v_ids = list(distances.keys())
        wiener_index = 0
        for i in range(len(v_ids)):
            for j in range(i + 1, len(v_ids)):
                u, v = v_ids[i], v_ids[j]
                if distances[u][v] == math.inf:
                    raise ValueError # the graph should not be disconnected
                wiener_index += distances[u][v]

        self.reset_weights()
        return wiener_index


    def estimate_boiling_point(self):
        boiling_point_celsius = (181.0 * (self.wiener_index() ** 0.1775)) - 273.15

        halogen_masses = {
            17: 35.45,  # Chlorine
            35: 79.904,  # Bromine
            53: 126.904  # Iodine
        }

        hydrogen_bonding_group_count = 0
        strong_dipole_group_count = 0
        heavy_halogen_count = 0
        aromatic_atom_count = 0
        halogen_mass = 0
        number_rings = 0

        for character in self.id:
            if character.isdigit():
                number_rings += 0.5



        for atom in self.atoms.values():

            if any(bond.bond_type == 1.5 for bond in atom.bonds):
                aromatic_atom_count += 1
            if atom.atomic_number == 8:
                if len(atom.bonds) == 0:
                    strong_dipole_group_count += 2
                if len(atom.bonds) == 1:
                    if list(atom.bonds)[0].bond_type == Bond.get_bond_type(2):
                        strong_dipole_group_count += 1
                    else:
                        hydrogen_bonding_group_count += 1
            elif atom.atomic_number == 7:
                implicit_hydrogens = 3 - sum(bond.bond_type[0] for bond in atom.bonds)
                if implicit_hydrogens >= 2:
                    hydrogen_bonding_group_count += 0.8
                elif implicit_hydrogens >= 1:
                    hydrogen_bonding_group_count += 0.4
                else:
                    strong_dipole_group_count += 0.2
            elif atom.atomic_number in {17, 35, 53}:
                heavy_halogen_count += 1
                halogen_mass += halogen_masses.get(atom.atomic_number)

        boiling_point_celsius += hydrogen_bonding_group_count * 118.5
        boiling_point_celsius += strong_dipole_group_count * 67.0
        boiling_point_celsius += heavy_halogen_count * 42.0
        boiling_point_celsius += aromatic_atom_count * 5.5
        boiling_point_celsius += halogen_mass * 0.45
        boiling_point_celsius += number_rings * 20

        # print(hydrogen_bonding_group_count, strong_dipole_group_count, heavy_halogen_count,
        #       aromatic_atom_count, halogen_mass, "Special counts")

        return round(boiling_point_celsius, 2)
