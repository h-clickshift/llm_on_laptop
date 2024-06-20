# Nice 3.8B 🏀
❓❓❓**Both Mem and Cpu Time increase a lot on MPS vs CPU which is Uncommon sense**

| Model       |MEM consume   | Dtype           | Device         |Time Cost(s) |Prompt  |Response|  
| ------------|------------- | --------------- |-----------------|--|--|--|
| Phi-3-mini-128k-instruct    | 15GB  |    float32   |cpu| 13  | HI,I am a language model.     |  How can I assist you today?
| Phi-3-mini-128k-instruct   | **25GB**  |    float32   |mps| **70**  | HI,I am a language model.     |  How can I assist you today?

## [Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)  
  **##Prompt##**  
  >HI,I am a language model.
  
  **##Response##**  
  >How can I assist you today?    
  * mps
  ![image](https://github.com/h-clickshift/llm_on_laptop/assets/117718271/24048324-6a58-40ff-9f4d-30ccbf55b92b)

  * cpu
  ![image](https://github.com/h-clickshift/llm_on_laptop/assets/117718271/12dfa097-c2e6-42f9-9e59-9ed959b58ea3)
