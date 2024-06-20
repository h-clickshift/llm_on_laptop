# I think I can do something about LLMs ~10B with my laptop :sunglasses::sunglasses::sunglasses:  
💢💢*HERE IS MY STORY：I joined an RLHF competition half a year ago. Unfortunately, due to a lack of GPU resources, my model was only about 60% trained by the time the competition window closed.* 💢💢

## system
* Apple M2 Pro
* memsize: 32GB

## Here is the list
* Play with Huggingface model ~10B locally
  
  | model       |mem consume   | bare run on CPU | bare run on MPS 
  | ------------|------------- | --------------- |-----------------|
  | Phi-3-mini-128k-instruct(3.8B) | 23GB         | 5s  🥇      |  **70s** |
  | chatglm3-6b | 18GB(float16)         | 13s  🥈     |   21.8s   |
  | gemma-7b    | 34GB(float32)         | 13321s  🚑     | 11234s 🚑     |
  | Mistral-7B-v0.3    | 28GB(float32)         |  never try      | 15275s 🚑     |

  * [gemma_7b](https://github.com/h-clickshift/llm_on_laptop/blob/main/x/gemma_7b.md)
  * [chatglm-b6](https://github.com/h-clickshift/llm_on_laptop/edit/main/x/chatglm3-6b.md)
  * [Mistral-7B-v0.3](https://github.com/h-clickshift/llm_on_laptop/blob/main/x/Mistral-7B-v0.3.md)
  * [hi-3-mini-128k-instruct](https://github.com/h-clickshift/llm_on_laptop/blob/main/x/Phi-3-mini-128k-instruct.md)

* Train a GPT-2 with private token and dataset(eg. py code model)
* 
