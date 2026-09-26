# Asset Module - Global Oceon Project
Author: ToluGold
Group: B
# Asset Module - Global Oceon Project
asset module
GROUP B PROJECT AUTHOR:Tolugold2704

Subsea System Utilisation Project purpose This project is a small Python model for checking the utilisation of two subsea components:

SubseaJumper, assessed for operating pressure and applied tension. RiserSystem, assessed for applied tension and bending moment. The utilisation() method compares the applied load with the allowable capacity. A result of 1.0 means 100% utilisation. The status_report() method reports PASS when utilisation is at or below 100%, and OVER LIMIT when it is above 100%.

Installation Clone or download this repository. Open a terminal in the project folder. Confirm that Python 3 is installed: python --version This project uses only Python's built-in libraries, so no extra packages need to be installed.

Usage Run the included example:

python subsea_systems.py Example output:

Jumper-J01: PASS - utilisation 80.0% Riser-R01: PASS - utilisation 85.0% You can also use the classes in your own Python file:

from subsea_systems import SubseaJumper, RiserSystem

jumper = SubseaJumper( name="Jumper-J01", design_pressure_bar=350.0, operating_pressure_bar=280.0, tension_capacity_kn=1200.0, applied_tension_kn=800.0, )

riser = RiserSystem( name="Riser-R01", tension_capacity_kn=2000.0, applied_tension_kn=1700.0, bending_capacity_knm=900.0, applied_bending_knm=500.0, )

print(jumper.status_report()) print(riser.status_report())
