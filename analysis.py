import numpy as np
import matplotlib.pyplot as plt

def function1(x):
    """y = 1.486*sqrt(x) for x in [0, 2.310089]"""
    return 1.486 * np.sqrt(x)

def function2(x):
    """y = -0.149*x^2 + 1.1139*x + 0.4805 for x in [2.310089, 5.201381]"""
    return -0.149*x**2 + 1.1139*x + 0.4805

def function3(x):
    """y = -0.3463*x^2 + 3.153*x - 4.7882 for x in [5.201381, 6.163728]"""
    return -0.3463*x**2 + 3.153*x - 4.7882

def function4(x):
    """y = 1.946*sqrt(-(x-6.75)) for x in [6.163728, 6.75]"""
    return 1.946 * np.sqrt(-(x - 6.75))

def volume_by_revolution(func, a, b, n=10000):
    """Calculate volume using method of disks (Riemann sum)."""
    dx = (b - a) / n
    volume = 0
    
    for i in range(n):
        x = a + i * dx
        radius = func(x)
        disk_volume = np.pi * radius**2 * dx
        volume += disk_volume
    
    return volume

def calculate_balloons_needed(person_mass_kg=55):
    balloon_volume_m3 = 0.01083  # m³ (10.83 liters)
    balloon_mass_kg = 0.003  # kg (3 g)
    air_density = 1.2250  # kg/m³
    helium_density = 0.178  # kg/m³
    person_volume_m3 = 0.054  # m³ (54 liters)
    
    archimedes_force = air_density * 9.80665 * balloon_volume_m3  # N
    helium_mass = helium_density * balloon_volume_m3  # kg
    total_balloon_mass = balloon_mass_kg + helium_mass  # kg
    gravity_force = total_balloon_mass * 9.80665  # N
    lifting_force_per_balloon = archimedes_force - gravity_force  # N
    
    person_weight = person_mass_kg * 9.80665  # N
    
    numerator = air_density * person_volume_m3 - person_mass_kg
    denominator = balloon_mass_kg - air_density * balloon_volume_m3
    balloons_needed = numerator / denominator
    
    return {
        'lifting_force_per_balloon_N': lifting_force_per_balloon,
        'liftable_mass_per_balloon_kg': lifting_force_per_balloon / 9.80665,
        'balloons_needed': balloons_needed,
        'person_weight_N': person_weight
    }

boundaries = [
    (function1, 0, 2.310089, "Function 1: y = 1.486√x"),
    (function2, 2.310089, 5.201381, "Function 2: y = -0.149x² + 1.1139x + 0.4805"),
    (function3, 5.201381, 6.163728, "Function 3: y = -0.3463x² + 3.153x - 4.7882"),
    (function4, 6.163728, 6.75, "Function 4: y = 1.946√(-(x-6.75))")
]

total_volume = 0

for i, (func, a, b, description) in enumerate(boundaries, 1):
    volume = volume_by_revolution(func, a, b)
    total_volume += volume
    
    print(f"\n{description}")
    print(f"  Interval: [{a:.3f}, {b:.3f}]")
    print(f"  Volume: {volume:.3f} cm³")
    print(f"  Volume: {volume/1000:.3f} liters")

print(f"Total calculated volume: {total_volume:.2f} cm³")
print(f"Total calculated volume: {total_volume/1000:.3f} liters")
print(f"Experimental volume: 10.75 liters")
print(f"Difference: {abs(total_volume/1000 - 10.75):.3f} liters")

results = calculate_balloons_needed(55)

print(f"Lifting force per balloon: {results['lifting_force_per_balloon_N']:.5f} N")
print(f"Can lift approximately: {results['liftable_mass_per_balloon_kg']*1000:.1f} g")
print(f"\nFor a 55 kg person:")
print(f"  Person's weight: {results['person_weight_N']:.1f} N")
print(f"  Balloons needed: {int(np.ceil(results['balloons_needed']))}")
print(f"  Exact calculation: {results['balloons_needed']:.1f} balloons")

balloons_needed = int(np.ceil(results['balloons_needed']))
cost_per_balloon = 100  # rubles
total_cost = balloons_needed * cost_per_balloon

print(f"\nCost calculation (100 rubles per balloon):")
print(f"  Total cost: {total_cost:,} rubles")

plt.figure(figsize=(12, 6))

x_points = []
y_points = []

for func, a, b, description in boundaries:
    x = np.linspace(a, b, 100)
    y = func(x)
    x_points.extend(x)
    y_points.extend(y)
    plt.plot(x, y, linewidth=2, label=description.split(":")[0])

plt.plot(x_points, y_points, 'k-', alpha=0.3, linewidth=3, label='Balloon profile')

x_points_mirror = [-x for x in x_points]
plt.plot(x_points_mirror, y_points, 'k-', alpha=0.3, linewidth=3)

plt.xlabel('x (cm)', fontsize=12)
plt.ylabel('y (cm)', fontsize=12)
plt.title('Balloon Profile Approximation\nPolina Nikulina, May 2024', fontsize=14, pad=20)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.axis('equal')

plt.tight_layout()
plt.savefig('balloon_profile.png', dpi=300)
print("\nPlot saved as 'balloon_profile.png'")
plt.show()
