import json
from loads import load_model, load_user_prompts, load_system_prompts
from get_response import create_response, process_prompts, process_all_system_prompts
from evaluate import analyze_response_leaks

def main():

    prompts_path = "prompts.json"
    system_prompts_path = "system_prompts.json"
    model_id = "Qwen/Qwen2.5-1.5B-Instruct"

    secret = "abc123"
    user_prompts = load_user_prompts(prompts_path)
    system_prompts = load_system_prompts(system_prompts_path, secret)

    # process_all_system_prompts(model_id, system_prompts, user_prompts, output_path="all_responses.json")
    stats = analyze_response_leaks("all_responses.json", "leak_stats.json", secret=secret)



if __name__ == "__main__":
    main()

