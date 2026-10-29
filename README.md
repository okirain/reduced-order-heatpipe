# AeroHeat-ROM: Space Reactor Two-Phase Heat Pipe Simulator & Quarto Thesis
**Author:** Muhammad Naufal Tamimi (NIM: 20/456315/TK/50445)  
**Department:** Departemen Teknik Nuklir dan Teknik Fisika (DTNTF), Fakultas Teknik  
**Institution:** Universitas Gadjah Mada (UGM), Yogyakarta, Indonesia

## Project Overview
This repository contains:
1. `heatpipe_rom.py`: Standalone Reduced-Order Numerical Model (ROM) for two-phase alkali metal heat pipe flow in microgravity.
2. Complete Quarto Skripsi / Thesis Project complying with the UGM DTNTF 2025 formatting guidelines.
3. NASA KRUSTY experimental field validation benchmarks (NASA TM-2018-219702).
4. Indonesian Space Reactor (ISR, Khandaq et al., 2020) heat pipe retrofit design and accident analyses.

## How to Render the Quarto Thesis
Ensure Quarto is installed (https://quarto.org/):
```bash
# Render to HTML book
quarto render --to html

# Render to formal PDF (requires TinyTeX / LaTeX)
quarto render --to pdf

# Preview live in browser
quarto preview
```

## How to Run the Python Simulator
```bash
# Run validation against NASA KRUSTY field data
python3 heatpipe_rom.py --mode validate_krusty --output summary

# Run ISR retrofit simulation at 1150 K
python3 heatpipe_rom.py --mode apply_isr --temp 1150 --output summary

# Custom simulation
python3 heatpipe_rom.py --mode simulate --power 8200 --temp 1150 --gravity 0.0 --output summary
```
