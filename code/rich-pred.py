#!/usr/bin/env python

"""Calculate richness values based area using a multi-model average

Takes a data file with one area per line as input

Example:
python rich_pred.py datafile.txt

"""

from __future__ import division
import fileinput
from math import log10

def power_eq(x, a, b):
    """Power equation"""
    return a * x ** b

def power_quad_eq(x, a, b, c):
    """Quadratic power equation"""
    return 10 ** (a + b * log10(x) + c * (log10(x) ** 2))

def logarithmic_eq(x, a, b):
    """Logarithmic equation"""
    return a + b * log10(x)

def michaelis_menten_eq(x, a, b):
    """Michaelis Mentent equation"""
    return a * x / (b + x)

def lomolino(x, a, b, c):
    """Lomolino equation"""
    return a / (1 + b ** log10(c / x))

def get_sar_estimate(area, equations, parameters):
    """Return an estimate for species richness using species-area relationships

    Calculates the species richness at a given spatial scale using each of a
    suite of species-area relationship equations and associated paramters.
    Returns the average of those values as an estimate of species richness.
    """
    estimates = []
    for i, equation in enumerate(equations):
        estimates.append(equation(area, *parameters[i]))
    return sum(estimates) / len(estimates)

sar_eqs = [power_eq, power_quad_eq, logarithmic_eq, michaelis_menten_eq, lomolino]
sar_parameters = [[20.81, 0.1896], [1.35, 0.1524, 0.0081],
                  [14.36, 21.16], [85.91, 42.57],
                  [1082.45, 1.59, 390000000]]

if __name__ == "__main__":
    for area in fileinput.input():
        print area.strip() + ',' + str(get_sar_estimate(float(area), sar_eqs, sar_parameters))
