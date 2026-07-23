"""
Exceeding the Requirements:
1. Defined universal constants (EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY, 
   WATER_DYNAMIC_VISCOSITY) outside of functions for better maintainability.
2. Added a convert_kpa_to_psi function to convert the final pressure 
   calculation from kilopascals to pounds per square inch (psi).
3. Updated the main function to display the final result in both kPa and psi.
4. Added professional docstrings to all functions to clearly define arguments 
   and return values.
5. Improved code clarity and avoided shadowing by renaming the `reynolds_number` 
   parameter to `reynolds` inside the `pressure_loss_from_pipe_reduction` function.
"""
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
WATER_DENSITY = 998.2                # density of water (kilogram / meter^3)
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # acceleration from Earth's gravity (meter / second^2)
WATER_DYNAMIC_VISCOSITY = 0.0010016        # dynamic viscosity of water (Pascal seconds)
PSI_FROM_KPA = 0.1450377377          # KPA to PSI conversion ratio    

def main():
    # Asks user for input
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    psi = convert_kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals (kPa) or {psi:.1f} pounds per square inch (psi).")

def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column.
    
    Args:
        tower_height: The height of the tower in meters.
        tank_height: The height of the tank walls in meters.
        
    Returns:
        The total height of the water column in meters.
    """
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(water_height):
    """Calculate the water pressure gained due to the height of the water column.
    
    Args:
        water_height: The height of the water column.
        
    Returns:
        The total water pressure gained in kilopascals.
    """
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height) / 1000 

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure lost due to the pipe.
    
    Args:
        pipe_diameter: The diameter of the pipe in meters.
        pipe_length: The length of the pipe in meters.
        friction_factor: The friction factor of the pipe.
        fluid_velocity: The density of water 998.2 (kilogram / meter3).
        
    Returns: The total pressure lost due to the pipe.
    """
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate the pressure lost due to the fittings on the pipes.
    
    Args:
        fluid_velocity: The density of water 998.2 (kilogram / meter3).
        quantity_fittings: number of fittings used.
        
    Returns:The total pressure lost due to the fittings on the pipes.
    """
    return -.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number.
    
    Args:
        hydraulic_diameter: The hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the inner diameter of the pipe.
        fluid_velocity: The density of water 998.2 (kilogram / meter3).
        
    Returns: The calculated Reynolds number.
    """  
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds, smaller_diameter):
    """Calculate lost pressure when water is moving from a large pipe to a smaller one in kilopascals.
    
    Args:
        larger_diameter: The diameter of the larger pipe in meters.
        fluid_velocity: The density of water 998.2 (kilogram / meter3).
        reynolds: The calculated Reynolds number.
        smaller_diameter: The diameter of the smaller pipe in meters.
        
    Returns: The calculated loss of pressure when water is moving from a large pipe to a smaller one in kilopascals.
    """
    k=(.1 + 50 / reynolds) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000

def convert_kpa_to_psi(pressure):
    """Calculate the conversion from kilopascals (kPa) to pounds per square inch (psi).
    
    Args:
        pressure: Calculated water pressure the the house in kilopascals. 

    Returns: The calculated conversion from kilopascals (kPa) to pounds per square inch (psi)."""
    return pressure * PSI_FROM_KPA

if __name__ == "__main__":
    main()