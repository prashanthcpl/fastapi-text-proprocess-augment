from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
import random
import re

# Download required NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

app = FastAPI()

# Store dataset in memory
dataset = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Text Processing API"}

@app.post("/load")
async def load_dataset():
    try:
        with open("sample.txt", "r") as file:
            global dataset
            dataset = file.readlines()
            dataset = [line.strip() for line in dataset]
        return {"message": f"Loaded {len(dataset)} lines from dataset"}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="sample.txt not found")

@app.get("/view")
async def view_dataset():
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset is empty. Please load dataset first.")
    return {"dataset": dataset}

@app.get("/normalize")
async def normalize_text():
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset is empty. Please load dataset first.")
    
    result = []
    for text in dataset:
        # Convert to lowercase and remove special characters
        normalized = text.lower()
        normalized = re.sub(r'[^a-zA-Z\s]', '', normalized)
        result.append({
            "original": text,
            "normalized": normalized
        })
    
    return {"results": result}

@app.get("/augment")
async def augment_text():
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset is empty. Please load dataset first.")
    
    def augment_word(word):
        if len(word) <= 3:  # Don't modify very short words
            return word
            
        operations = ['substitute', 'delete', 'insert']
        operation = random.choice(operations)
        
        chars = 'abcdefghijklmnopqrstuvwxyz'
        pos = random.randint(1, len(word)-2)  # Don't modify first or last char
        
        if operation == 'substitute':
            return word[:pos] + random.choice(chars) + word[pos+1:]
        elif operation == 'delete':
            return word[:pos] + word[pos+1:]
        else:  # insert
            return word[:pos] + random.choice(chars) + word[pos:]
    
    result = []
    for text in dataset:
        words = text.split()
        # Randomly select one word to augment
        if words:
            idx = random.randint(0, len(words)-1)
            words[idx] = augment_word(words[idx])
        augmented_text = " ".join(words)
        result.append({
            "original": text,
            "augmented": augmented_text
        })
    
    return {"results": result} 