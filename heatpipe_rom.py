#!/usr/bin/env python3
"""
AeroHeat-ROM: Two-Phase Space Reactor Heat Pipe Simulator
Author: Muhammad Naufal Tamimi (NIM: 20/456315/TK/50445)
Departemen Teknik Nuklir dan Teknik Fisika (DTNTF), Fakultas Teknik
Universitas Gadjah Mada (UGM), Yogyakarta, Indonesia
"""

import math
import json
import sys
import argparse
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Tuple, Optional

# Thermophysical properties of sodium and liquid metals
class FluidProperties:
    @staticmethod
    def sodium(T: float) -> Dict[str, float]:
        T = max(371.0, min(1500.0, float(T)))
        rho_l = 1011.8 - 0.22054 * T - 1.9226e-5 * (T**2) + 5.637e-9 * (T**3)
        ln_p_bar = 11.9463 - (12633.73 / T) - 0.5 * math.log(T)
        p_sat = math.exp(ln_p_bar) * 1.0e5
        M_w = 0.02299
        R_u = 8.31446
        dimer_frac = max(0.0, min(0.35, 0.05 + 2.0e-4 * (T - 800.0)))
        M_eff = M_w * (1.0 + dimer_frac)
        R_g_eff = R_u / M_eff
        rho_v = p_sat / (R_g_eff * T)
        h_fg = 5.25e6 * ((1.0 - (T / 2503.0)) ** 0.38) if T < 2503.0 else 3.8e6
        ln_mu = -6.4406 - 0.3958 * math.log(T) + (556.835 / T)
        mu_l = math.exp(ln_mu)
        mu_v = 1.8e-7 * (T ** 0.6)
        sigma = max(0.01, 0.2405 - 1.0e-4 * T)
        k_l = 124.67 - 0.11381 * T + 5.5226e-5 * (T**2) - 1.1842e-8 * (T**3)
        cp_l = 1630.14 - 0.83354 * T + 4.6283e-4 * (T**2)
        return {"fluid": "Sodium", "T": T, "rho_l": rho_l, "rho_v": rho_v,
                "p_sat": p_sat, "h_fg": h_fg, "mu_l": mu_l, "mu_v": mu_v,
                "sigma": sigma, "k_l": k_l, "cp_l": cp_l, "gamma": 1.33, "R_g": R_g_eff}

# Run via terminal:
# python3 heatpipe_rom.py --mode validate_krusty --output summary
# python3 heatpipe_rom.py --mode apply_isr --temp 1150 --output summary
