# I think I can do something about LLMs ~10B with my laptop :sunglasses::sunglasses::sunglasses:  
💢💢*HERE IS MY STORY：I joined an RLHF competition half a year ago. Unfortunately, due to a lack of GPU resources, my model was only about 60% trained by the time the competition window closed.* 💢💢

## system
* Apple M2 Pro
* memsize: 32GB

## Here is the list
* Play with Huggingface model ~10B locally
  
  | model       |mem consume   | bare run on CPU | bare run on MPS 
  | ------------|------------- | --------------- |-----------------|
  | chatglm3-6b | 18GB(float16)         | 13s  🥇        |   21.8s         |
    | gemma-7b    | 34GB(float32)         | 13321s  🚑     | 11234s     |

  * [**gemma_7b**](https://huggingface.co/google/gemma-7b), with `python gemma_7b.py`  
    **##Prompt##**  
    >HI,I am a language model.
     
    **##Response##**  
    >I am here to help you with your questions. Please tell me what you want me to do.
    >
    >\*\*Here are some of the things I can do:\*\*  
    >\* Provide information on a wide range of topics**    
    >\* Answer questions about grammar, spelling, and punctuation**   
    >\* Help you with writing and editing**  
    >\* Translate text between languages**  
    >\* Provide information on a variety of subjects, such as history, science, and technology**  
    >\*\*Please let me know\*\***
       
    **##Time Cost on CPU##**  
    >** time cost:**13321.635095119476s** **  takes about 4h :cry:  
    >** time per token: 0.0075065860373728505 **
    
    ![image](https://github.com/h-clickshift/llm_on_laptop/assets/117718271/2d277005-05fb-4edb-bad0-6d3c0766b725)

    Given installed memsize 32GB < model mem resident 34GB, **NO OOM accident** :tada:  :thumbsup:
    
    The average CPU consumption is below 25%, with only a single core running. By leveraging the full capabilities of multiple CPU cores, it is possible to achieve a significant speedup.
    
    **## Time Cost on mps##**
    
    >** time cost:**11234.172160863876s** **  speedup by 15.6% ⬆️  😃   
    >** time per token: 0.00890141245550489 **
    
    ![image](https://github.com/h-clickshift/llm_on_laptop/assets/117718271/04f1775f-c6e4-449e-ad01-deff94585e85)

  * [chatglm3-6b](https://huggingface.co/THUDM/chatglm3-6b)  
     **##Prompt##**  
    >HI,I am a language model.
     
    **##Response##**  
    >I am here to assist you with any questions you may have. How can I help you today?
    
    **## Time Cost on MPS ##**
    
   >** time cost:13.22354507446289s **  ⏫ 😸  
   >** time per token: 2.419925959325228 **  
   
   ![image](https://github.com/h-clickshift/llm_on_laptop/assets/117718271/2d1d585e-28a6-495f-8570-b731373a8a0d)

   **## Time Cost on CPU ##**  
   change model dtype to float32 with `model.to(device, dtype=torch.float32)`  
  > ** time cost:21.84215497970581s **  33.3% ↘️ 🎱  
  > ** time per token: 1.465056906231649 **  
  
* Train a GPT-2 with private token and dataset(eg. py code model)
* 
