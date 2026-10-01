import pdfplumber
from gtts import gTTS


def get_pdf_text(file_path): 
    with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
        pdf_file_text = "".join([page.extract_text() for page in pdf_file.pages])
        pdf_file_text_cleared = pdf_file_text.replace("\n", "")

    return pdf_file_text_cleared


def get_audio_from_text(text):
    audio_text = gTTS(text=text, lang='ru', slow=False)
    audio_text.save("audio.mp3")


def main():
    file_path = "text.pdf"
    text = get_pdf_text(file_path) 
    get_audio_from_text(text)
    

if __name__ == "__main__":
    main()
