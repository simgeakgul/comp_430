import json
from tqdm import tqdm
from loads import load_model

def create_response(model, tokenizer, system_prompt, user_prompt) :

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response

def process_list(model_id, system_prompt, user_prompts, output_path="responses.json"):
    
    model, tokenizer = load_model(model_id)
    results = {}
    for category, prompts in user_prompts.items():
        results[category] = []
        for prompt in tqdm(prompts, desc=f"Processing category: {category}"):
            response = create_response(model, tokenizer, system_prompt, prompt)
            results[category].append({
                "prompt": prompt,
                "response": response
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"Saved responses to {output_path}")
    return results