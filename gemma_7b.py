from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import multiprocessing

def load_model(path, device):
    model = AutoModelForCausalLM.from_pretrained(path)
    model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(path)
    return model, tokenizer

def generate(input_text, model, tokenizer, device):
    input_ids = tokenizer(input_text, return_tensors="pt").to(device)
    import time
    t0 = time.time()
    outputs = model.generate(**input_ids, max_length=100)
    t1 = time.time()
    print(f"** time cost:{t1 - t0}s **")
    num_tokens = len(outputs[0])
    print(f"** time per token: {num_tokens/(t1 - t0)} **")
    print(tokenizer.decode(outputs[0]))

if __name__ == "__main__":
    pid = os.getpid()
    print(f"** Current Process ID: {pid} **")
    from res_profile import *
    plot_process = multiprocessing.Process(target=update_plot, args=(pid,))
    plot_process.start()

    model, tok = load_model("google/gemma-7b-it","cpu")
    input_text = "HI,I am a language model."
    generate(input_text, model, tok, "cpu")
    print("done")

