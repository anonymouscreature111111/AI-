import cv2

img = cv2.imread("himalayas.webp")

sizes = {
    "small": (200, 200),
    "medium": (400, 400),
    "large": (600, 600)
}

for name, size in sizes.items():
    resized = cv2.resize(img, size)

    cv2.imshow(name.title(), resized)
    cv2.imwrite(f"input_image_{name}.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()