# Calculate the yield curve steepness
def calculate_steepness(bond_2yr, bond_10yr):
    steepness = bond_10yr - bond_2yr
    return steepness

def calculate_ratio(bond_2yr, bond_10yr):
  return bond_2yr/bond_10yr
