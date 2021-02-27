import cv2
import numpy as np

img_array = []

print("Array created...")

for filename in range(5364):
    img = cv2.imread(
        f"/Users/edwardgallyot/Documents/VSCode Projects/P5_test/{filename}.png"
    )
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    print(f"Image {filename} copied...")


print("Setting Output...")

out = cv2.VideoWriter(
    "Visualisation_4K_1.mov",
    cv2.VideoWriter_fourcc("m", "p", "4", "v"),
    44100 / 1837,
    size,
    True,
)


for i in range(len(img_array)):
    print(f"Writing to .mov file image: {i}...")
    out.write(img_array[i])

print("Finished!")
out.release()
