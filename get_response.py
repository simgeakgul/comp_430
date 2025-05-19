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

def process_prompts(model, tokenizer, system_prompt, user_prompts, output_path="responses.json"):
    
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


def process_all_system_prompts(model_id, system_prompts, user_prompts, output_path="all_responses.json"):
    model, tokenizer = load_model(model_id)
    all_results = {}

    for level_name, system_prompt in system_prompts.items():
        all_results[level_name] = {"system_prompt": system_prompt}

        for category, prompts in user_prompts.items():
            category_results = []

            for prompt in tqdm(prompts, desc=f"{level_name} → {category}"):
                response = create_response(model, tokenizer, system_prompt, prompt)
                category_results.append({
                    "user_prompt": prompt,
                    "response":    response
                })

            all_results[level_name][category] = category_results

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(all_results, f, ensure_ascii=False, indent=2)
            print(f"    ✔ Saved {len(category_results)} items for {level_name}/{category}")

    return all_results

