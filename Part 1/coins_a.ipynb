import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# **Step 1: Improve Contrast Using CLAHE**
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_gray = clahe.apply(gray)

# **Step 2: Apply GaussianBlur to Reduce Noise**
blurred = cv2.GaussianBlur(enhanced_gray, (15, 15), 0)

# **Step 3: Adaptive Thresholding for Better Edge Detection**
adaptive_thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)

# **Step 4: Morphological Operations to Close Gaps**
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# **Step 5: Edge Detection Using Canny**
edges = cv2.Canny(morph, 50, 150)

# **Step 6: Find Contours**
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# **Step 7: Draw Contours on the Original Image**
detected_coins = image.copy()
cv2.drawContours(detected_coins, contours, -1, (0, 255, 0), 2)

# **Step 8: Display Results Using Matplotlib**
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Original Image with Detected Coins
axs[0].imshow(cv2.cvtColor(detected_coins, cv2.COLOR_BGR2RGB))
axs[0].set_title(f"Detected Coins: {len(contours)}")
axs[0].axis("off")

# Edge Detection Image
axs[1].imshow(edges, cmap="gray")
axs[1].set_title("Edge Detection")
axs[1].axis("off")

# Adaptive Thresholding Image
axs[2].imshow(adaptive_thresh, cmap="gray")
axs[2].set_title("Adaptive Thresholding")
axs[2].axis("off")

plt.show()

# Print Total Count
print(f"Total number of coins detected: {len(contours)}")
