from transformers import AutoTokenizer, AutoModelForCausalLM
import os,torch
import multiprocessing
from res_profile import *
def load_model(path, device):
    cache_dir = os.path.join(os.path.dirname(__file__), path.split("/")[-1])
    model = AutoModelForCausalLM.from_pretrained(path, cache_dir=cache_dir, trust_remote_code=True)
    model.to(torch.device(device))
    tokenizer = AutoTokenizer.from_pretrained(path, cache_dir=cache_dir)
    return model, tokenizer

def generate(input_text, model, tokenizer, device):
    input_ids = tokenizer(input_text, return_tensors="pt").to(torch.device(device))
    import time
    t0 = time.time()
    outputs = model.generate(**input_ids, max_length=100)
    t1 = time.time()
    print(f"** time cost:{t1 - t0}s **")
    num_tokens = len(outputs[0])
    print(f"** time per token: {num_tokens/(t1 - t0)} **")
    print(tokenizer.decode(outputs[0]))


def run(pid, model, device, input_text):
    plot_process = multiprocessing.Process(target=update_plot, args=(pid,model))
    plot_process.start()
    model, tok = load_model(model, device)
    generate(input_text, model, tok, device)
    plot_process.kill()


if __name__ == "__main__":
    pid = os.getpid()
    print(f"** Current Process ID: {pid} **")
    # run(pid, "google/gemma-7b", "mps", "HI,I am a language model.")
    # run(pid, "mistralai/Mistral-7B-v0.3", "mps", "HI,I am a language model.")
    run(pid, "microsoft/Phi-3-mini-128k-instruct", "mps", "HI,I am a language model.")
    print("done")

