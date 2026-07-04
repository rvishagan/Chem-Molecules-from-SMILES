"""
CS3C, Final, Molecule implementation with Graph
Ragavishagan Rajasekar
"""


from Molecule import *
import unittest

class BondTestCase(unittest.TestCase):

    def testBondInitializeWithBondTypes(self):
        single_bond_string = Bond(("C", "H"), "C", "H", "Single")
        single_bond_int = Bond(("C", "H"), "C", "H", 1)
        single_bond_tuple = Bond(("C", "H"), "C", "H", (1, "Single"))
        self.assertEqual(str(single_bond_int), str(single_bond_tuple))
        self.assertEqual(str(single_bond_int), str(single_bond_string))
        self.assertEqual(str(single_bond_tuple), str(single_bond_string))
        double_bond_string = Bond(("C", "H"), "C", "H", "Double")
        double_bond_int = Bond(("C", "H"), "C", "H", 2)
        double_bond_tuple = Bond(("C", "H"), "C", "H", (2, "Double"))
        self.assertEqual(str(double_bond_int), str(double_bond_tuple))
        self.assertEqual(str(double_bond_int), str(double_bond_string))
        self.assertEqual(str(double_bond_tuple), str(double_bond_string))
        triple_bond_string = Bond(("C", "H"), "C", "H", "Triple")
        triple_bond_int = Bond(("C", "H"), "C", "H", 3)
        triple_bond_tuple = Bond(("C", "H"), "C", "H", (3, "Triple"))
        self.assertEqual(str(triple_bond_int), str(triple_bond_tuple))
        self.assertEqual(str(triple_bond_int), str(triple_bond_string))
        self.assertEqual(str(triple_bond_tuple), str(triple_bond_string))
        aromatic_bond_string = Bond(("C", "H"), "C", "H", "Aromatic")
        aromatic_bond_int = Bond(("C", "H"), "C", "H", 1.5)
        aromatic_bond_tuple = Bond(("C", "H"), "C", "H", (1.5, "Aromatic"))
        self.assertEqual(str(aromatic_bond_int), str(aromatic_bond_tuple))
        self.assertEqual(str(aromatic_bond_int), str(aromatic_bond_string))
        self.assertEqual(str(aromatic_bond_tuple), str(aromatic_bond_string))

        print(single_bond_string)
        print(single_bond_int)
        print(single_bond_tuple)
        print(double_bond_string)
        print(double_bond_int)
        print(double_bond_tuple)
        print(triple_bond_string)
        print(triple_bond_int)
        print(triple_bond_tuple)
        print(aromatic_bond_string)
        print(aromatic_bond_int)
        print(aromatic_bond_tuple)
        print(repr(single_bond_string))
        print(repr(single_bond_int))
        print(repr(single_bond_tuple))
        print(repr(double_bond_string))
        print(repr(double_bond_int))
        print(repr(double_bond_tuple))
        print(repr(triple_bond_string))
        print(repr(triple_bond_int))
        print(repr(triple_bond_tuple))
        print(repr(aromatic_bond_string))
        print(repr(aromatic_bond_int))
        print(repr(aromatic_bond_tuple))

class AtomTestCase(unittest.TestCase):


    def testAtomInitializeWithDifferentElements(self):
        hydrogen_name = Atom("Hydrogen", 1) # initialize with name
        hydrogen_number = Atom(1, 1) # initialize with number
        hydrogen_symbol =  Atom("H", 1) # initialize with symbol
        hydrogen_tuple = Atom((1, "H", "Hydrogen"), 1) # initialize with everything in a tuple
        hydrogen_different_initializations = [hydrogen_name, hydrogen_number, hydrogen_symbol, hydrogen_tuple]
        print(hydrogen_different_initializations)
        for hydrogens in hydrogen_different_initializations:
            self.assertEqual(str(hydrogens), "Atom=(H1, [])")
        carbon_name = Atom("Carbon", 1)  # initialize with name
        carbon_number = Atom(6, 1)  # initialize with number
        carbon_symbol = Atom("C", 1)  # initialize with symbol
        carbon_tuple = Atom((6, "C", "Carbon"), 1)  # initialize with everything in a tuple
        carbon_different_initializations = [carbon_name, carbon_number, carbon_symbol, carbon_tuple]
        print(carbon_different_initializations)
        for carbons in carbon_different_initializations:
            self.assertEqual(str(carbons), "Atom=(C1, [])")
        oxygen_name = Atom("Oxygen", 1)  # initialize with name
        oxygen_number = Atom(8, 1)  # initialize with number
        oxygen_symbol = Atom("O", 1)  # initialize with symbol
        oxygen_tuple = Atom((8, "O", "Oxygen"), 1)  # initialize with everything in a tuple

        oxygen_different_initializations = [oxygen_name, oxygen_number, oxygen_symbol, oxygen_tuple]
        print(oxygen_different_initializations)

        for oxygens in oxygen_different_initializations:
            self.assertEqual(str(oxygens), "Atom=(O1, [])")

    def testAddBonds(self):
        # make water which is H20
        O1 = Atom(8,1)
        H1 = Atom(1, 1)
        H2 = Atom(1, 2)
        water = [O1, H1, H2] # this is a test before Molecule class is implemented
        O1.add_bond(H1, 1)
        O1.add_bond(H2, 1)
        expected = "[Atom=(O1, ['O1-H1', 'O1-H2']), Atom=(H1, ['O1-H1']), Atom=(H2, ['O1-H2'])]"
        self.assertEqual(expected,str(water))

class MoleculeTestCase(unittest.TestCase):
    def testInitializeWithoutSmiles(self):
        mol = Molecule()
        mol.add_atom("C")
        mol.add_atom("C") # Should add as C2
        mol.add_bond("C1", "C2", 2)
        expected = """Molecule Smiles: 
Atoms: 
Atom=(C1, ['C1=C2'])
Atom=(C2, ['C1=C2'])
Bonds: 
C1=C2"""
        self.assertEqual(str(mol), expected) # Should be C1 double bonded to C2
        for _ in range(4):
            mol.add_atom("H")
        mol.add_bond("C1", "H1", 1)
        mol.add_bond("C1", "H2", 1)
        mol.add_bond("C2", "H3", 1)
        mol.add_bond("C2", "H4", 1)
         # This is a molecule of Ethylene
        ethylene = """Molecule Smiles: 
Atoms: 
Atom=(C1, ['C1-H1', 'C1-H2', 'C1=C2'])
Atom=(C2, ['C1=C2', 'C2-H3', 'C2-H4'])
Atom=(H1, ['C1-H1'])
Atom=(H2, ['C1-H2'])
Atom=(H3, ['C2-H3'])
Atom=(H4, ['C2-H4'])
Bonds: 
C1-H1
C1-H2
C1=C2
C2-H3
C2-H4"""

        self.assertEqual(str(mol), ethylene)

    def testInitializeSmiles(self):
        mol = Molecule("CCO")
        expected = """Molecule Smiles: CCO
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'O1-C2'])
Atom=(O1, ['O1-C2'])
Bonds: 
C1-C2
O1-C2"""
        self.assertEqual(expected, str(mol))

    def testInitializeSmilesWithTwoLetterElement(self):
        mol = Molecule("CCCl")
        expected = """Molecule Smiles: CCCl
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'Cl1-C2'])
Atom=(Cl1, ['Cl1-C2'])
Bonds: 
C1-C2
Cl1-C2"""
        self.assertEqual(expected, str(mol))

    def testInitializeSmilesWithRing(self):
        mol = Molecule("C1CCCCC1")
        expected = """Molecule Smiles: C1CCCCC1
Atoms: 
Atom=(C1, ['C1-C2', 'C1-C6'])
Atom=(C2, ['C1-C2', 'C2-C3'])
Atom=(C3, ['C2-C3', 'C3-C4'])
Atom=(C4, ['C3-C4', 'C4-C5'])
Atom=(C5, ['C4-C5', 'C5-C6'])
Atom=(C6, ['C1-C6', 'C5-C6'])
Bonds: 
C1-C2
C1-C6
C2-C3
C3-C4
C4-C5
C5-C6"""
        self.assertEqual(str(mol), expected)


    def testInitializeSmilesWithRingClosingOfSpecialBondType(self):
        mol = Molecule("OC1CCCCC=1N")
        expected = """Molecule Smiles: OC1CCCCC=1N
Atoms: 
Atom=(C1, ['C1-C2', 'C1=C6', 'O1-C1'])
Atom=(C2, ['C1-C2', 'C2-C3'])
Atom=(C3, ['C2-C3', 'C3-C4'])
Atom=(C4, ['C3-C4', 'C4-C5'])
Atom=(C5, ['C4-C5', 'C5-C6'])
Atom=(C6, ['C1=C6', 'C5-C6', 'N1-C6'])
Atom=(N1, ['N1-C6'])
Atom=(O1, ['O1-C1'])
Bonds: 
C1-C2
C1=C6
C2-C3
C3-C4
C4-C5
C5-C6
N1-C6
O1-C1"""
        self.assertEqual(str(mol), expected)

    def testInitialSmilesWithNestedBranches(self):
        mol = Molecule("CC((O)C)C")
        expected = """Molecule Smiles: CC((O)C)C
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'C2-C3', 'C2-C4', 'O1-C2'])
Atom=(C3, ['C2-C3'])
Atom=(C4, ['C2-C4'])
Atom=(O1, ['O1-C2'])
Bonds: 
C1-C2
C2-C3
C2-C4
O1-C2"""
        self.assertEqual(str(mol), expected)

    def testInitialSmilesWithConsecutiveBranches(self):
        mol = Molecule("CC(C)(C)C")
        expected = """Molecule Smiles: CC(C)(C)C
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'C2-C3', 'C2-C4', 'C2-C5'])
Atom=(C3, ['C2-C3'])
Atom=(C4, ['C2-C4'])
Atom=(C5, ['C2-C5'])
Bonds: 
C1-C2
C2-C3
C2-C4
C2-C5"""
        self.assertEqual(str(mol), expected)

    def testInitialSmilesWithBranchesAndBonds(self):
        mol = Molecule("CC(C(=O)O)O")
        expected = """Molecule Smiles: CC(C(=O)O)O
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'C2-C3', 'O3-C2'])
Atom=(C3, ['C2-C3', 'O1=C3', 'O2-C3'])
Atom=(O1, ['O1=C3'])
Atom=(O2, ['O2-C3'])
Atom=(O3, ['O3-C2'])
Bonds: 
C1-C2
C2-C3
O1=C3
O2-C3
O3-C2"""
        self.assertEqual(str(mol), expected)

    def testInitialSmilesWithAbsurdAmountsOfNestedBranches(self):
        mol = Molecule("CC(C(C(C)C)C)C")
        expected = """Molecule Smiles: CC(C(C(C)C)C)C
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'C2-C3', 'C2-C8'])
Atom=(C3, ['C2-C3', 'C3-C4', 'C3-C7'])
Atom=(C4, ['C3-C4', 'C4-C5', 'C4-C6'])
Atom=(C5, ['C4-C5'])
Atom=(C6, ['C4-C6'])
Atom=(C7, ['C3-C7'])
Atom=(C8, ['C2-C8'])
Bonds: 
C1-C2
C2-C3
C2-C8
C3-C4
C3-C7
C4-C5
C4-C6"""
        self.assertEqual(str(mol), expected)

    def testInitialSmilesWithRingOpenAndBranch(self):
        mol = Molecule("CC1(C)CCCC1")
        expected = """Molecule Smiles: CC1(C)CCCC1
Atoms: 
Atom=(C1, ['C1-C2'])
Atom=(C2, ['C1-C2', 'C2-C3', 'C2-C4', 'C2-C7'])
Atom=(C3, ['C2-C3'])
Atom=(C4, ['C2-C4', 'C4-C5'])
Atom=(C5, ['C4-C5', 'C5-C6'])
Atom=(C6, ['C5-C6', 'C6-C7'])
Atom=(C7, ['C2-C7', 'C6-C7'])
Bonds: 
C1-C2
C2-C3
C2-C4
C2-C7
C4-C5
C5-C6
C6-C7"""
        self.assertEqual(str(mol), expected)


    def testInitialSmilesWithDoubleRing(self):
        mol = Molecule("C12(CCCCC2)CCCCC1")
        expected = """Molecule Smiles: C12(CCCCC2)CCCCC1
Atoms: 
Atom=(C1, ['C1-C11', 'C1-C2', 'C1-C6', 'C1-C7'])
Atom=(C10, ['C10-C11', 'C9-C10'])
Atom=(C11, ['C1-C11', 'C10-C11'])
Atom=(C2, ['C1-C2', 'C2-C3'])
Atom=(C3, ['C2-C3', 'C3-C4'])
Atom=(C4, ['C3-C4', 'C4-C5'])
Atom=(C5, ['C4-C5', 'C5-C6'])
Atom=(C6, ['C1-C6', 'C5-C6'])
Atom=(C7, ['C1-C7', 'C7-C8'])
Atom=(C8, ['C7-C8', 'C8-C9'])
Atom=(C9, ['C8-C9', 'C9-C10'])
Bonds: 
C1-C11
C1-C2
C1-C6
C1-C7
C10-C11
C2-C3
C3-C4
C4-C5
C5-C6
C7-C8
C8-C9
C9-C10"""
        self.assertEqual(str(mol), expected)


    def testCaffiene(self):
        caffeine = Molecule("CN1C(=O)N(C)C2=C1C(=O)N(C)C=N2")
        print("______ CAFFEINE _________")
        print(caffeine)

    def testAsprin(self):
        print("______ ASPIRIN _________")
        aspirin = Molecule("CC(=O)OC1=CC=CC=C1C(=O)O")
        print(aspirin)

    def testGlucose(self):
        print("______ GLUCOSE _________")
        glucose = Molecule("C(C1C(C(C(C(O1)O)O)O)O)O")
        print(glucose)

    def testCholesterol(self):
        print("______ CHOLESTEROL _________")
        cholesterol = Molecule("CC(C)CCCC(C)C1CCC2C1(CCC3C2CC=C4C3(CCC(C4)O)C)C")
        print(cholesterol)

class MoleculeBoilingPointTestCase(unittest.TestCase):
    def testFindBoilingPointAlkanes(self):
        # Pentane
        mol = Molecule("CCCCC")
        experimental_boiling_point = 36.1
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Isopentane
        mol = Molecule("CC(C)CC")
        experimental_boiling_point = 27.7
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Neopentane
        mol = Molecule("CC(C)(C)C")
        experimental_boiling_point = 9.5
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

    def testFindBoilingPointOxygen(self):
        # Ethanol
        mol = Molecule("CCO")
        experimental_boiling_point = 78.4
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Acetone
        mol = Molecule("CC(=O)C")
        experimental_boiling_point = 56.0
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Butanone
        mol = Molecule("CCC(=O)C")
        experimental_boiling_point = 79.6
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Diethyl Ether
        mol = Molecule("CCOCC")
        experimental_boiling_point = 34.6
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

    def testFindBoilingPointNitrogen(self):
        # Methylamine (Primary)
        mol = Molecule("CN")
        experimental_boiling_point = 6.3
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Dimethylamine (Secondary)
        mol = Molecule("CNC")
        experimental_boiling_point = 8
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Trimethylamine (Tertiary)
        mol = Molecule("CN(C)C")
        experimental_boiling_point = 3.5
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

    def testFindBoilingPointRingsAndAromaticity(self):
        # Cyclopentane
        mol = Molecule("C1CCCC1")
        experimental_boiling_point = 49.2
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=40)

        # Toluene
        mol = Molecule("Cc1ccccc1")
        experimental_boiling_point = 110.6
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=40)

    def testFindBoilingPointHalogens(self):
        # Chloropropane
        mol = Molecule("CCCCl")
        experimental_boiling_point = 46.6
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=40)

        # Bromopropane
        mol = Molecule("CCCBr")
        experimental_boiling_point = 71.0
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Iodopropane
        mol = Molecule("CCCI")
        experimental_boiling_point = 102.5
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)


        # Chloroethane
        mol = Molecule("CCCl")
        experimental_boiling_point = 12.3  # the true boiling point is 12.3
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for {mol.id}")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

    def testFindBoilingPointComplexMolecules(self):
        # Methamphetamine (Secondary Amine + Aromatic Benzene Ring)
        mol = Molecule("CNC(C)Cc1ccccc1")
        experimental_boiling_point = 212.0  # True physical boiling point
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for Methamphetamine")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=40)

        # Nicotine (Fused Aromatic Pyridine Ring + Pyrrolidine Ring + Tertiary Amine)
        mol = Molecule("CN1CCCC1c2cccnc2")
        experimental_boiling_point = 247.0  # True physical boiling point
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for Nicotine")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=40)

        # Paracetamol / Acetaminophen (Aromatic Ring + 1 Phenol Alcohol + 1 Secondary Amide)
        mol = Molecule("CC(=O)Nc1ccc(O)cc1")
        experimental_boiling_point = 420.0  # Standard physical decomposition boiling point calibration baseline
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for Acetaminophen")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

        # Guaifenesin
        mol = Molecule("CC(O)COc1ccccc1OC")
        experimental_boiling_point = 352.2  # True physical boiling point
        predicted_boiling_point = mol.estimate_boiling_point()
        print(f"experimental = {experimental_boiling_point}, predicted = {predicted_boiling_point}, \
        difference = {round(experimental_boiling_point - predicted_boiling_point, 2)}, for Guaifenesin")
        self.assertAlmostEqual(predicted_boiling_point, experimental_boiling_point, delta=20)

del MoleculeBoilingPointTestCase
del MoleculeTestCase
# del AtomTestCase
del BondTestCase
