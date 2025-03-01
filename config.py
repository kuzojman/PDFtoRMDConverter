from transformers import TrOCRProcessor
from optimum.onnxruntime import ORTModelForVision2Seq
import torch
from ultralytics import YOLO
import pytesseract


class config:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata\rus.traindata"'
    pytesseract = pytesseract
    custom_config = r'--oem 3 --psm 6'
    
    processor = TrOCRProcessor.from_pretrained('breezedeus/pix2text-mfr')
    pix2text = ORTModelForVision2Seq.from_pretrained(
        'breezedeus/pix2text-mfr',
        use_cache=False,
        use_io_binding=False,
        provider="CUDAExecutionProvider" if torch.cuda.is_available() else "CPUExecutionProvider"
    )

    yolo = YOLO("./yolo_model/best_v.pt").to(device)