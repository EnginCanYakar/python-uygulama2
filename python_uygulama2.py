import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaların tanımlanması
points = [(2, 3), (5, 7), (1, 8), (4, 6)]

# Mesafelerin saklanacağı liste
distances = []

# Mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")

