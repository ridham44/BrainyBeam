# Build a python program which returns the no. of paragraph , count of words, count of sentences and doc size of .txt document.
#15/12/2024

import os
import re


def analyze_text_file(file_path):
    

    try:
        
        if not os.path.exists(file_path):
            return {"error": "File not found."}

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)

        words = text.split()
        word_count = len(words)

        sentences = re.split(r'[.!?]', text)
        sentence_count = len([s for s in sentences if s.strip()])

        file_size = os.path.getsize(file_path)

        return {
            "paragraphs": paragraph_count,
            "words": word_count,
            "sentences": sentence_count,
            "file_size_bytes": file_size
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    file_path = input("Enter the path to the .txt file: ")
    analysis = analyze_text_file(file_path)

    if "error" in analysis:
        print(f"Error: {analysis['error']}")
    else:
        print("Text File Analysis:")
        print(f"Paragraphs: {analysis['paragraphs']}")
        print(f"Words: {analysis['words']}")
        print(f"Sentences: {analysis['sentences']}")
        print(f"File Size: {analysis['file_size_bytes']} bytes")
