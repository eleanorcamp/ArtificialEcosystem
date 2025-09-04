# Artificial Ecosystem Simulation

*A Python-based simulation exploring emergent behaviors in plant-consumer ecosystems.*

---

## Overview
This project simulates an artificial ecosystem with two primary components: **plants** and **eaters**.  
Plants act as a renewable resource that regrows once every season, while eaters consume plants to survive and reproduce.  

The goal of this work is to explore how simple resource-consumer interactions can lead to complex dynamics such as growth, decline, and ecosystem stability.

---

## Features
- Agent-based simulation of plants and eaters  
- Configurable parameters (plant regrowth rate, eater energy cost, reproduction threshold, etc.)  
- Visualization of population dynamics (graphs and simulation snapshots)  
- Reproducible experiments with preset configurations  

---

## Installation & Usage

Clone the repository and install dependencies:

```bash
git clone git@github.com:eleanorcamp/ArtificialEcosystem.git
cd artificial-ecosystem
pip install -r requirements.txt
```

To run a simple simulation:
```bash
python main.py
```

Or to run a simulation with lots of graph output for data analysis:
```bash
python graphing_tools.py
```