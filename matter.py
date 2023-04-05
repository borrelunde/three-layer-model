from dataclasses import dataclass


@dataclass
class Matter:
    name: str
    density: float  # Density Rho in kg/m^3
    velocity: float  # Velocity c in m/s


# Matters mostly from the Fundamentals of Acoustics - Fourth Edition:
# A10 Tables of Physical Properties of Matter

# Liquids
water_fresh = Matter(name="Water (fresh)", density=998, velocity=1481)
water_sea = Matter(name="Water (sea)", density=1026, velocity=1500)
alcohol = Matter(name="Alcohol (ethyl)", density=790, velocity=1150)
castor = Matter(name="Castor (oil)", density=950, velocity=1540)
mercury = Matter(name="Mercury", density=13600, velocity=1450)
turpentine = Matter(name="Turpentine", density=870, velocity=1250)
glycerin = Matter(name="Glycerin", density=1260, velocity=1980)
water_match = Matter(name="Water match", density=2000, velocity=3500)
oil = Matter(name="OOil", density=850, velocity=1350)

# Fluid-like sea bottoms
red_clay = Matter(name="Red clay", density=1340, velocity=1460)
calcareous_ooze = Matter(name="Calcareous ooze", density=1570, velocity=1470)
coarse_silt = Matter(name="Coarse silt", density=1790, velocity=1540)
quartz_sand = Matter(name="Quartz sad", density=2070, velocity=1730)

# Solids
aluminium = Matter(name="Aluminium", density=2700, velocity=6300)
brass = Matter(name="Brass", density=8500, velocity=4700)
copper = Matter(name="Copper", density=8900, velocity=5000)
iron_cast = Matter(name="Iron (cast)", density=7700, velocity=4350)
lead = Matter(name="Lead", density=11300, velocity=2050)
nickel = Matter(name="Nickel", density=8800, velocity=5850)
silver = Matter(name="Silver", density=10500, velocity=3700)
steel = Matter(name="Steel", density=7700, velocity=6100)
glass = Matter(name="Glass (Pyrex)", density=2300, velocity=5600)
quartz = Matter(name="Quartz (X-cut)", density=2650, velocity=5750)
lucite = Matter(name="Lucite", density=1200, velocity=2650)
concrete = Matter(name='Concrete', density=2600, velocity=3100)
ice = Matter(name="Ice", density=920, velocity=3200)
cork = Matter(name="Cork", density=240, velocity=500)
oak = Matter(name="Oak", density=720, velocity=4000)
pine = Matter(name="Pine", density=450, velocity=3500)
rubber_hard = Matter(name="Rubber (hard)", density=1100, velocity=2400)
rubber_soft = Matter(name="Rubber (soft)", density=950, velocity=1050)
rubber_rho_c = Matter(name="Rubber (rho-c)", density=1000, velocity=1550)
piezo = Matter(name='Piezo', density=7500, velocity=4355)
epoxy = Matter(name='Epoxy', density=1200, velocity=2300)
plexiglass = Matter(name='Plexiglass', density=1200, velocity=2600)

# Gasses
air = Matter(name="Air", density=1.21, velocity=343)
o2 = Matter(name="O2", density=1.43, velocity=317.2)
co2 = Matter(name="CO2", density=1.98, velocity=268.6)
h2 = Matter(name="H2", density=0.09, velocity=1269.5)
steam = Matter(name="Steam", density=0.6, velocity=404.8)
