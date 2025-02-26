import cv2
import numpy as np

def count_coins(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # **Step 1: Improve Contrast Using CLAHE**
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(gray)

    # **Step 2: Apply Stronger GaussianBlur to Suppress Patterns**
    blurred = cv2.GaussianBlur(enhanced_gray, (25, 25), 0)  # Increased kernel size

    # **Step 3: Otsu’s Thresholding for Better Segmentation**
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # **Step 4: Morphological Operations to Remove Small Noise**
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)

    # **Step 5: Find Contours and Filter Out Small Areas (Patterns Inside Coins)**
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]  # Ignore small patterns

    # **Step 6: Count Total Coins**
    coin_count = len(filtered_contours)
    print(f"Total number of coins detected: {coin_count}")

    # **Step 7: Draw Contours on the Original Image**
    detected_coins = image.copy()
    cv2.drawContours(detected_coins, filtered_contours, -1, (0, 255, 0), 2)

    # **Step 8: Display the Processed Image with Count**
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(detected_coins, cv2.COLOR_BGR2RGB))
    plt.title(f"Total Coins Detected: {coin_count}")
    plt.axis("off")
    plt.show()

# **Run the Function**
count_coins("coins.jpg")
