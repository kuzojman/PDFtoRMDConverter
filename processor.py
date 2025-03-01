import cv2
from corrected_text import corrected_text
from PIL import Image
from config import config
import sys

class models: 
    def predict_tess(cropped_image):
        
        
        cleared = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        cleared = cv2.resize(cleared, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
        
        cleared = cv2.equalizeHist(cleared)
        
        _, cleared = cv2.threshold(cleared, 50, 255, cv2.THRESH_BINARY)
        
        cleared = config.pytesseract.image_to_string(cleared, lang='rus', config=config.custom_config)
        print("Распознанный текст:", cleared)
            
        corrected = corrected_text.corect_text(cleared)
        corrected = corrected.strip()
        print("Исправленный текст:", corrected)
        

        return corrected

    def predict_form(cropped_image):

        image_fps = Image.fromarray(cropped_image)
        


        pixel_values = config.processor(images=image_fps, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(config.device)
        generated_ids = config.pix2text.generate(pixel_values)
        generated_text = config.processor.batch_decode(generated_ids, skip_special_tokens=True)
        text = generated_text[0]
        text = text.replace('\\\\', '\\')
        text = f'${text}$'
        print(text)
        
        return text


    def predict_yolo(img):
        return config.yolo.predict(img, save_txt=False)        

