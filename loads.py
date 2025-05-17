import json
from typing import Dict, List
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer

model_ids = ["Qwen/Qwen2.5-1.5B-Instruct",
]

# Placeholder for actual model loading logic
def load_model(model_id: str):

    if model_id not in model_ids:
        print("Not valid model id.")
        return

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer

def load_user_prompts(path: str) -> Dict[str, List[str]]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_system_prompts(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data