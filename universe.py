import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
au = np.array([.387, .723, 1, 1.524, 5.203, 9.537, 19.19, 30.07])
ecc = np.array([.206, .007, .017, .093, .048, .054, .047, .009])
radii = np.array([.383, .949, 1, .532, 11.21, 9.45, 4.01, 3.88])
a, angle = 2.15 * au ** .45, np.deg2rad([20, 75, 130, 190, 235, 285, 325, 355])
phase = np.deg2rad([20, 145, 250, 80, 190, 300, 40, 230])
colors = ["#aaa9a7", "#e9b96e", "#55aaff", "#dc6446", "#d8a978", "#e7ce88", "#82d8df", "#507bd8"]

fig, ax = plt.subplots(figsize=(7, 7), facecolor="#050711")
ax.set_facecolor("#050711")
ax.set_xlim(-12, 12); ax.set_ylim(-12, 12); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
for spine in ax.spines.values(): spine.set_visible(False)
stars = np.random.default_rng(4).uniform(-12, 12, (180, 2))
ax.scatter(stars[:, 0], stars[:, 1], s=1, c="white", alpha=.28, linewidths=0)
theta = np.linspace(0, 2 * np.pi, 300)
for q, e, tilt in zip(a, ecc, angle):
    x, y = q * (np.cos(theta) - e), q * np.sqrt(1 - e * e) * np.sin(theta)
    ax.plot(x * np.cos(tilt) - y * np.sin(tilt), x * np.sin(tilt) + y * np.cos(tilt), color="#6e7893", lw=.45, alpha=.38)
ax.scatter(0, 0, s=520, c="#ffd76a", edgecolors="#fff3bd", linewidths=1.5, zorder=4)
body = ax.scatter(np.zeros(8), np.zeros(8), s=18 * radii ** .7 + 9, c=colors, edgecolors="white", linewidths=.35, zorder=5)
labels = [ax.text(0, 0, n, color="#d7dced", fontsize=6, alpha=.75) for n in names]

def step(frame):
    mean = phase + frame * .075 / a ** 1.5
    anomaly = mean.copy()
    for _ in range(5): anomaly -= (anomaly - ecc * np.sin(anomaly) - mean) / (1 - ecc * np.cos(anomaly))
    x, y = a * (np.cos(anomaly) - ecc), a * np.sqrt(1 - ecc ** 2) * np.sin(anomaly)
    pos = np.column_stack((x * np.cos(angle) - y * np.sin(angle), x * np.sin(angle) + y * np.cos(angle)))
    body.set_offsets(pos)
    for label, point in zip(labels, pos): label.set_position(point + [.14, .14])
    return body, *labels

animation = FuncAnimation(fig, step, interval=16, blit=True, cache_frame_data=False)
plt.show()
