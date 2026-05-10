import cv2
import numpy as np

def preprocess_malayalam(image_path):
    img = cv2.imread(image_path)

    # Remove color noise
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # CLAHE contrast boost
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    # Adaptive threshold - Malayalam strokes are thin
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 15, 11
    )

    # Deskew
    coords = np.column_stack(np.where(thresh < 255))
    if coords.size:
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = thresh.shape
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
        thresh = cv2.warpAffine(thresh, M, (w, h),
                                flags=cv2.INTER_CUBIC,
                                borderMode=cv2.BORDER_REPLICATE)

    return thresh


def crop_upper_right(image_array):
    h, w = image_array.shape[:2]
    # Top 30% height, right 40% width
    return image_array[0:int(h * 0.30), int(w * 0.40):w]
