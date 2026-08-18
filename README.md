# Solar System Simulation

An interactive visualization of the Solar System built with **Python, NumPy, and Matplotlib**.

The simulation models the orbital motion of the eight planets using elliptical orbits and **Kepler's equation**, then visualizes their movement in a real-time animation.


## Features

* ☀️ Sun and all eight planets
* 🪐 Elliptical planetary orbits
* 🌌 Procedurally generated star field
* 📐 Planetary orbital eccentricities
* 🔄 Real-time orbital animation
* 🧮 Numerical solution of Kepler's equation
* 🎨 Minimal dark-space visualization
* ⚡ Lightweight implementation using NumPy and Matplotlib

## Physics

Each planet is assigned approximate orbital parameters based on real Solar System data.

The simulation uses:

* Semi-major axis
* Orbital eccentricity
* Orbital phase
* Orbital inclination/orientation
* Kepler's equation

The orbital position is calculated from:

$$
M = E - e\sin(E)
$$

where:

* $M$ is the mean anomaly
* $E$ is the eccentric anomaly
* $e$ is the orbital eccentricity

Kepler's equation is solved numerically using the **Newton-Raphson method**.

The resulting eccentric anomaly is then converted into Cartesian coordinates to determine each planet's position along its orbit.

## Technologies

* **Python**
* **NumPy**
* **Matplotlib**
* `FuncAnimation`

## Installation

Clone the repository:

```bash
git clone https://github.com/JavadHazbavi/solar-system-simulation.git
cd solar-system-simulation
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python solar_system.py
```

## Project Structure

```text
solar-system-simulation/
│
├── assets/
│   └── solar-system.gif
│
├── solar_system.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Planetary Data

| Planet  | Semi-major Axis (AU) | Eccentricity |
| ------- | -------------------: | -----------: |
| Mercury |                0.387 |        0.206 |
| Venus   |                0.723 |        0.007 |
| Earth   |                1.000 |        0.017 |
| Mars    |                1.524 |        0.093 |
| Jupiter |                5.203 |        0.048 |
| Saturn  |                9.537 |        0.054 |
| Uranus  |               19.190 |        0.047 |
| Neptune |               30.070 |        0.009 |

## Important Note

This project is a **visual and educational simulation**, not a physically accurate Solar System simulator.

For visualization purposes, orbital distances, planet sizes, and animation speed are scaled. The goal is to demonstrate orbital mechanics and scientific visualization rather than reproduce the exact spatial and temporal scales of the Solar System.

## What I Learned

This project combines several concepts from physics and programming:

* Orbital mechanics
* Kepler's laws
* Numerical methods
* Newton-Raphson iteration
* Vectorized NumPy calculations
* Scientific visualization
* Real-time animation with Matplotlib

## License

This project is licensed under the MIT License.
