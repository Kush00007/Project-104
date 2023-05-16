import cv2

img = cv2.imread("solar-system.jpg")
texts = {
    "Mercury": (100, 200),
    "Venus": (180, 230),
    "Earth": (300, 190),
    "Mars": (400, 200),
    "Jupiter": (500, 250),
    "Saturn": (700, 200),
    "Uranus": (950, 220),
    "Neptune": (1100, 200),
}
for planet, (x, y) in texts.items():
    cv2.putText(img, planet, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_system_with_name.jpg", img)