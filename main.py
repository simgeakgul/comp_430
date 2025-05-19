import json
from loads import load_model, load_user_prompts, load_system_prompts
from get_response import create_response, process_list
from evaluate import evaluate_secret_safety

def main():

    prompts_path = "prompts.json"
    system_prompts_path = "system_prompts.json"
    model_id = "Qwen/Qwen2.5-7B-Instruct"
    # model, tokenizer = load_model(model_id)

    secret = "abc123"
    user_prompts = load_user_prompts(prompts_path)
    system_prompts = load_system_prompts(system_prompts_path, secret)

    print(system_prompts["level4"])




if __name__ == "__main__":
    main()

