import MLrecognition
from ExtractTextFromImg import image_to_text
from textscanner import textscanner

textscanner()
TextExtracted=image_to_text('ImageWithText.jpg')
print(TextExtracted)
MLrecognition.prediction(TextExtracted)

