from PIL import Image
import pytesseract
import io

class OCRService:
    @staticmethod
    def extract_text(image_bytes: bytes) -> str:
        image = Image.open(io.BytesIO(image_bytes))
        image = image.convert("RGB")
        return pytesseract.image_to_string(image)
