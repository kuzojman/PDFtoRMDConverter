# PDF-to-RMD Converter
[![GitHub](https://img.shields.io/github/license/facebookresearch/nougat)](https://github.com/facebookresearch/nougat)
[![PyPI](https://img.shields.io/pypi/v/nougat-ocr?logo=pypi)](https://pypi.org/project/nougat-ocr)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Community%20Space-blue)](https://huggingface.co/spaces/ysharma/nougat)


PDF-to-RMD Converter — это инструмент для автоматического перевода научных текстов с формулами из PDF в R Markdown (RMD). Проект предназначен для ученых, исследователей и специалистов, работающих с технической документацией и математическими формулами.

# 📄 Описание проекта
Проект предоставляет возможность конвертации документов в формате PDF, содержащих текст, математические формулы (LaTeX), таблицы и изображения, в удобный для редактирования формат R Markdown. Это особенно полезно при подготовке публикаций, отчетов или презентаций.

# Основные возможности:

1. Извлечение текста из PDF-документа.
2. Конвертация формул, представленных в формате LaTeX, в корректный синтаксис RMD.
3. Сохранение изображений и таблиц.
4. Генерация выходного файла в формате .Rmd, готового для использования в RStudio или других редакторах.

# 🚀 Установка

Клонируйте репозиторий:
```text
git clone https://github.com/kuzojman/PDFtoRMDConverter
```
Необходимо установить CUDA 12.1 https://developer.nvidia.com/cuda-12-1-0-download-archive

Для работы инструмента необходимо использовать виртуальное окружение Python:  
Установите Anaconda с офицального сайта https://www.anaconda.com/download  
Запустите Anaconda Porompt
Перейдите в католог инструмента: 
```text
cd PDFtoRMDConverter
```
введите команду для создания окружения с зависимостями:
```text
conda env create -f pdftormd_env.yml
```
Активируйте окружение:
```text
conda activate pdftormd
```
Установите torch:
```text
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
Если при использовании инструмента возникнет ошибка, попробуйте установить другую версию torch:
```text
pip uninstall torch torchvision torchaudio
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
Установите tesseract OCR по этой ссылке https://github.com/UB-Mannheim/tesseract/wiki
Также убедитесь, что установлен Poppler — инструмент для обработки PDF.  
# Использование инструмента
В командной строке Anaconda prompt активировать окружение если еще не активировано:
```text
conda activate pdftormd
```
Запуск инструмента:
```text
python setup.py 
```
Введите пути к вашим файлам через пробел:
```text
<путь к файлу 1> <путь к файлу 2> ... <путь к файлу n>
```
Для завершения работы программы введите "N" вместо пути к файлу или нажмите ctr+c, или просто закройте консоль
```text
N
```
Резултаты работы сохраняются в папку results
# 🛠️ Примеры использования
## Пример 1: Конвертация научной статьи
Допустим, у вас есть PDF-документ article.pdf расположеный по пути "C:\example\article.pdf" с текстом и математическими формулами. Чтобы конвертировать его в RMD-файл:

```text
python setup.py 
C:\example\article.pdf
```
Выходной файл article.rmd будет содержать:


---
title: "Название статьи"
author: "Имя Автора"
date: "2024-06-25"
output: html_document
---

# Введение

Научный текст, содержащий объяснение.

## Основные уравнения

Формула:

$$
E = mc^2
$$

Другой текст.

## Графики и изображения

![Описание изображения](image1.png)

## Заключение

Некоторый вывод.
## Пример 2: Обработка нескольких PDF-файлов
Можно запустить скрипт на нескольких файлах:

```text
python convert.py input1.pdf output1.rmd
python convert.py input2.pdf output2.rmd
```
# 📋 Аргументы командной строки

| Аргумент             | Описание                                |Пример|
| ---------------------| ------------------------------------------ |------------------------------------------|
| `input.pdf`        | Путь к входному PDF-файлу                       |article.pdf|
| `output.rmd`| Путь к выходному RMD-файлу                        |article_output.rmd|
| `output.rmd`          | Путь к выходному RMD-файлу |article_output.rmd|
| `--images`  | Сохранение изображений              |--images|
| `--verbose`        | Подробный лог процесса     |--verbose|


# 🔧 Зависимости
 1. Python 3.8+
 2. pypdf2 — для работы с PDF.
 3. pandas — для обработки таблиц.
 4. pandoc — для конвертации текста.
 5. poppler-utils — для обработки встроенных изображений.

# 🤝 Содействие
Если вы хотите внести вклад в проект, пожалуйста, сделайте следующее:

1. Форкните репозиторий.
2. Создайте новую ветку (git checkout -b feature/НоваяФункция).
3. Внесите свои изменения и закоммитьте их (git commit -m 'Добавлена новая функция').
4. Отправьте изменения в вашу ветку (git push origin feature/НоваяФункция).
5. Создайте Pull Request на GitHub.

# 📜 Лицензия
Проект распространяется под лицензией MIT.

# 📧 Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной через vladimir.kuzovkin@bk.ru или откройте новую задачу в разделе Issues.

# 🌟 Благодарности
Спасибо всем, кто участвует в развитии проекта!

