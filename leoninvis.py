import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)

# ---------------- VIDEO INITIALIZATION ----------------

# Path to your uploaded video
video_path = r"/mnt/data/64ba2eef-ed13-4e4d-8a2f-3e46fa70da4a.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

# ---------------- BACKGROUND CAPTURE ----------------

background = None

print("Capturing background...")

# Read first 60 frames for cleaner background
for i in range(60):
    ret, background = cap.read()

if background is None:
    print("Error: Failed to capture background")
    exit()

# Flip background horizontally
background = cv2.flip(background, 1)

# Resize background
background = cv2.resize(background, (800, 600))

print("Background captured successfully!")

# ---------------- RESET VIDEO ----------------

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# ---------------- WINDOW SETUP ----------------

cv2.namedWindow("Invisible Blue Cloak", cv2.WINDOW_NORMAL)

# ---------------- MAIN LOOP ----------------

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    # Flip frame horizontally for mirror effect
    frame = cv2.flip(frame, 1)

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ---------------- BLUE COLOR DETECTION ----------------
    # Tuned specifically for your uploaded video

    lower_blue = np.array([85, 20, 120])
    upper_blue = np.array([120, 120, 255])

    # Create blue mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # ---------------- MASK CLEANING ----------------

    kernel = np.ones((3, 3), np.uint8)

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Expand detected area slightly
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Blur edges for smoother invisibility effect
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    # Inverse mask
    mask_inv = cv2.bitwise_not(mask)

    # ---------------- INVISIBILITY EFFECT ----------------

    # Replace blue area with background
    invisible_part = cv2.bitwise_and(background, background, mask=mask)

    # Keep non-blue parts visible
    visible_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both images
    final_output = cv2.add(invisible_part, visible_part)

    # ---------------- DISPLAY WINDOWS ----------------

    # Main invisibility output
    cv2.imshow("Invisible Blue Cloak", final_output)

    # Optional debug mask window
    cv2.imshow("Blue Mask", mask)

    # Press ESC to quit
    key = cv2.waitKey(25)

    if key == 27:
        break

# ---------------- CLEANUP ----------------

cap.release()
cv2.destroyAllWindows()