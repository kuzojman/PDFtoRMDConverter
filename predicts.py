from processor import models
import pandas as pd
import os
from pdf2image import convert_from_path
import cv2
import numpy as np
import torch
from PIL import Image
import sys

class construct_df:
    def get_text_detection(img_path):
        """
        Функция для распознавания текста и формул
        Функция получает путь к лиcту для распознавания,
        модель yolo8 выделяет зоны с текстом, формулами и рисунками
        и раздаёт обнаруженные объекты по разным моделям.
        Текст передаём в tesseract
        На выходе получаем датафрейм с лейблом, координатами рамки и распознанным текстом или формулой,
        или ссылкой на изображение.
        Изображения сохраняются как отдельные jpeg файлы.
        """
        
        if os.path.splitext(img_path)[1] == '.pdf':
            img = convert_from_path(img_path, 500)
            img = np.array(img[0])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        else:
            img = img_path
            
        results = models.predict_yolo(img)
        print(results)
        try:
            if results[1] == 'error 0':
                return results[1]
        except IndexError:
            pass
        print(len(results[0].boxes))
        result = results[0]
        df = pd.DataFrame(columns=['image', 'label', 'x1', 'y1', 'x2', 'y2', 'detected'])
        boxes = result.boxes.xyxy   # Координаты боксов
        scores = result.boxes.conf  # Вероятности
        nms_thresh = 0.3
        filtered_detections = torch.ops.torchvision.nms(boxes, scores, nms_thresh)
        for idx in filtered_detections:
            counter=1
            # Извлекаем данные для текущего бокса
            box = result.boxes[idx]  # Объект бокса
            label = result.names[box.cls.item()]  # Извлечение имени класса
            cords = [round(x) for x in box.xyxy[0].tolist()]  # Координаты в формате [x1, y1, x2, y2]
            prob = round(box.conf.item(), 2)  # Уверенность модели

            print("Object type:", label)
            print("Coordinates:", cords)
            print("Probability:", prob)
            print('---')

            # Определяем координаты границ текста
            x1, y1, x2, y2 = cords[0], cords[1], cords[2], cords[3]
            # Загружаем изображение
            if os.path.splitext(img_path)[1] == '.pdf':
                image = img
            else:
                image = cv2.imread(img)
            # Проверяем, что координаты находятся в пределах изображения
            h, w, _ = image.shape
            if 0 <= x1 < x2 <= w and 0 <= y1 < y2 <= h:
                # Обрезаем изображение по указанным координатам
                cropped_image = image[y1:y2, x1:x2]

                # Отображаем обрезанное изображение
                #display(Image.fromarray(cropped_image))
            else:
                print(f"Skipped invalid box with coordinates: {cords}")


            if label == 'Text': 
                text = models.predict_tess(cropped_image)
                new_row = pd.DataFrame({
                'image': [img_path],
                'label': [label],
                'x1': [x1],
                'y1': [y1],
                'x2': [x2],
                'y2': [y2],
                'detected': [text]
                })
                df = pd.concat([df, new_row], ignore_index=True)
                print(f'x1 = {x1} y_m = {(y1+y2)/2}')

            elif label == 'Formula':
                text = models.predict_form(cropped_image)
                
                new_row = pd.DataFrame({
                    'image': [img_path],
                    'label': [label],
                    'x1': [x1],
                    'y1': [y1],
                    'x2': [x2],
                    'y2': [y2],
                    'detected': [text]
                })
                df = pd.concat([df, new_row], ignore_index=True)
                print(f'x1 = {x1} y_m = {(y1+y2)/2}')

            else:
                path_to_cropped_image = f"./pictures/{os.path.basename(img_path)}_pictures_{counter}.jpeg"
                print(path_to_cropped_image)
                Image.fromarray(cropped_image).save(path_to_cropped_image, 'JPEG')
                absolute_path = os.path.abspath(path_to_cropped_image)
                counter += 1

                new_row = pd.DataFrame({
                    'image': [img_path],
                    'label': [label],
                    'x1': [x1],
                    'y1': [y1],
                    'x2': [x2],
                    'y2': [y2],
                    'detected': [f"""![picture_{counter}]({absolute_path})  \n"""]
                })
                df = pd.concat([df, new_row], ignore_index=True)
        df['y_mean'] = (df['y1'] + df['y2'])/2
        return df
if __name__ == '__main__':    
    args = sys.argv[1:]
    func = args[0]
    func_args =  args[1:]
    eval(func)(*func_args)