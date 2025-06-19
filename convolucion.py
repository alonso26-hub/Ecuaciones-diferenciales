import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

A = np.array([1, 2, 3, 3, 4, 5, 6])
B = np.array([2, 3, 4, 5, 6, 7, 8])
C = np.convolve(A, B)
I = list(range(len(C)))

print("Convolución:")
print(C)
print("Tamaño de la convolución:", len(C))
print("Índices:", I)

plt.figure(figsize=(15, 10))

plt.subplot(1, 2, 1)
plt.stem(I, C, basefmt=" ", linefmt="teal", markerfmt="o", label='x(t) * g(t)')
plt.xlabel('n', fontsize=12)
plt.ylabel('x(t)*g(t)', fontsize=12)
plt.title('Convolución de x(t) * g(t)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.subplot(1, 2, 2)
plt.plot(range(len(A)), A, 'o-', label='x(t)', color='darkorange', markersize=8)
plt.plot(range(len(B)), B, 's--', label='g(t)', color='royalblue', markersize=8)
plt.xlabel('n', fontsize=12)
plt.ylabel('x(t) y g(t)', fontsize=12)
plt.title('Señales x(t) y g(t)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
