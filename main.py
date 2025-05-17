from loads import load_model, load_user_prompts, load_system_prompts
from evaluate import create_response

def main():

    prompts_path = "prompts.json"
    system_prompts_path = "system_prompts.json"
    model_id = "Qwen/Qwen2.5-1.5B-Instruct"

    user_prompts = load_user_prompts(prompts_path)
    #system_prompts = load_system_prompts(system_prompts_path)
    model, tokenizer = load_model(model_id)

    user_prompt = "Give me a short introduction to large language model."
    system_prompt = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
    create_response(model, tokenizer, system_prompt, user_prompt)

if __name__ == "__main__":
    main()

