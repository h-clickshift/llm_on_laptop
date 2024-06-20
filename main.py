from transformers import AutoTokenizer, AutoModelForCausalLM
import os, torch
import multiprocessing
from res_profile import *


def load_model(path, device, dtype):
    cache_dir = os.path.join(os.path.dirname(__file__), path.split("/")[-1])
    model = AutoModelForCausalLM.from_pretrained(path, cache_dir=cache_dir, trust_remote_code=True, torch_dtype=dtype)
    model.to(torch.device(device))
    # for name, parm in model.named_parameters():
    #     print(f"{name} - {parm.dtype} ")
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
    print(f"** time per token: {num_tokens / (t1 - t0)} **")
    print(tokenizer.decode(outputs[0]))


def run(pid, model, device, input_text, dtype=torch.float32):
    plot_process = multiprocessing.Process(target=update_plot, args=(pid, model))
    plot_process.start()
    try:
        model, tok = load_model(model, device, dtype)
        generate(input_text, model, tok, device)
    except RuntimeError as e:
        print(f"** Error:{e} **")
        plot_process.kill()
    plot_process.kill()


if __name__ == "__main__":
    pid = os.getpid()
    print(f"** Current Process ID: {pid} **")
    # run(pid, "google/gemma-7b", "mps", "HI,I am a language model.")
    # run(pid, "mistralai/Mistral-7B-v0.3", "mps", "HI,I am a language model.")
    run(pid, "microsoft/Phi-3-mini-128k-instruct", "cpu",
        "HI,I am a language model.")  # torch.float16 get RuntimeError: "addmm_impl_cpu_" not implemented for 'Half'
    print("done")
