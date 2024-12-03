import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def read_text_from_images(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' nie istnieje.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, file_name)
            try:
                image = Image.open(image_path)
                text = pytesseract.image_to_string(image)
                print(f"Tekst odczytany z pliku {file_name}:\n{text}\n")
            except Exception as e:
                print(f"Błąd podczas odczytywania pliku {file_name}: {e}")


if __name__ == "__main__":
    read_text_from_images("zdjecia")
