import pytesseract
from PIL import Image
import cv2
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # converted_img = cv2.medianBlur(img, 3)
    # converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    return converted_img


def read_text_from_images(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' nie istnieje.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, file_name)
            try:
                processed_image = preprocess_image(image_path)

                text = pytesseract.image_to_string(processed_image)
                print(f"Tekst odczytany z pliku {file_name}:\n{text}\n")
            except Exception as e:
                print(f"Błąd podczas odczytywania pliku {file_name}: {e}")


if __name__ == "__main__":
    read_text_from_images("zdjecia")
