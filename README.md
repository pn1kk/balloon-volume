# Balloon Volume Analysis

Research project investigating the volume of a balloon using integration methods.

## Research Overview

This project calculates the volume of a balloon using:
1. Curve approximation of balloon edges with mathematical functions
2. Volume of revolution using limits and Riemann sums
3. Experimental verification by water displacement
4. Calculation of balloons needed to lift a person

## Key Findings

- **Balloon dimensions**: 33.75 cm length
- **Functions used**:
  1. \(y = 1.486\sqrt{x}\) 
  2. \(y = -0.149x^2 + 1.1139x + 0.4805\)
  3. \(y = -0.3463x^2 + 3.153x - 4.7882\)
  4. \(y = 1.946\sqrt{-(x-6.75)}\)
- **Calculated volume**: 86.63 cm³ (10.83 liters)
- **Experimental volume**: 10.75 liters

## Files

- `nikulina_balloon_volume_report.pdf` - Complete research paper
- `data/balloon_functions.csv` - Function parameters and boundaries
- `analysis.py` - Python implementation of the calculations
- `requirements.txt` - Required Python packages

## Quick Start

```bash
pip install -r requirements.txt
python analysis.py
