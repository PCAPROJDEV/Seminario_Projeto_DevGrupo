import matplotlib.pyplot as plt
import numpy as np

# Pontos do triângulo (não colineares)
triangle_points = np.array([[0.2, 0.2], [0.8, 0.2], [0.5, 0.8]])
triangle_labels = [+1, -1, +1]
triangle_coords = ['A', 'B', 'C']

# Pontos do quadrado
square_points = np.array([[0.2, 0.2], [0.8, 0.2], [0.8, 0.8], [0.2, 0.8]])
square_labels = [+1, -1, +1, -1]
square_coords = ['P1', 'P2', 'P3', 'P4']

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Esquerda: VC=3
axs[0].set_title("Separação de 3 pontos (VC = 3)")
for i, (pt, label, name) in enumerate(zip(triangle_points, triangle_labels, triangle_coords)):
    axs[0].scatter(*pt, c='blue' if label == +1 else 'red', marker='o' if label == +1 else 'x', s=100)
    axs[0].text(pt[0] + 0.02, pt[1] + 0.02, f"{name}: {label}", fontsize=11)

axs[0].set_xlim(0, 1)
axs[0].set_ylim(0, 1)
axs[0].set_aspect('equal')
axs[0].grid(True)

# Direita: VC > 3 falha
axs[1].set_title("Rotulação alternada de 4 pontos (VC < 4)")
for i, (pt, label, name) in enumerate(zip(square_points, square_labels, square_coords)):
    axs[1].scatter(*pt, c='blue' if label == +1 else 'red', marker='o' if label == +1 else 'x', s=100)
    axs[1].text(pt[0] + 0.02, pt[1] + 0.02, f"{name}: {label}", fontsize=11)

axs[1].set_xlim(0, 1)
axs[1].set_ylim(0, 1)
axs[1].set_aspect('equal')
axs[1].grid(True)

plt.tight_layout()
output_path = "vc_dimension.png"
plt.savefig(output_path, dpi=360)
plt.close()

