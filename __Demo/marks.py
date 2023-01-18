import speech_recognition as sr
from transformers import TFMarianMTModel, MarianTokenizer

model1 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-ar')
tokenizer1 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-ar')        
model2 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-fr')
tokenizer2 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-fr')
model3 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-fr-ar')
tokenizer3 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-fr-ar')
model4 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-fr-en')
tokenizer4 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-fr-en')
model5 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ar-en')
tokenizer5 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ar-en')
model6 = TFMarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ar-fr')
tokenizer6 = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ar-fr')

def translate(text,source_lg,target_language):
    if source_lg == "en" and target_language == "ar":
        input_ids = tokenizer1.encode(text, return_tensors="pt")
        outputs = model1.generate(input_ids)
        translated_text = tokenizer1.decode(outputs[0], skip_special_tokens=True)
        return translated_text


    elif source_lg == "en" and target_language == "fr":
        input_ids = tokenizer2.encode(text, return_tensors="pt")
        outputs = model2.generate(input_ids)
        translated_text = tokenizer2.decode(outputs[0], skip_special_tokens=True)
        return translated_text
        
    elif source_lg == "fr" and target_language == "ar":
        input_ids = tokenizer3.encode(text, return_tensors="pt")
        outputs = model3.generate(input_ids)
        translated_text = tokenizer3.decode(outputs[0], skip_special_tokens=True)
        return translated_text
    elif source_lg == "fr" and target_language == "en":
        input_ids = tokenizer4.encode(text, return_tensors="pt")
        outputs = model4.generate(input_ids)
        translated_text = tokenizer4.decode(outputs[0], skip_special_tokens=True)
        return translated_text
    elif source_lg == "ar" and target_language == "en":
        input_ids = tokenizer5.encode(text, return_tensors="pt")
        outputs = model5.generate(input_ids)
        translated_text = tokenizer5.decode(outputs[0], skip_special_tokens=True)
        return translated_text
    
    elif source_lg == "ar" and target_language == "fr":
        input_ids = tokenizer6.encode(text, return_tensors="pt")
        outputs = model6.generate(input_ids)
        translated_text = tokenizer6.decode(outputs[0], skip_special_tokens=True)
        return translated_text
    else:
        return "Invalid target language"
        

"""text='PyTorch Hub is a pre-trained model repository designed to facilitate research reproducibility.'
translate(text,"en","ar")
translate(text,"en","fr")"""