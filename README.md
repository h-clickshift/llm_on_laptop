# I think I can do something about LLM ~10B with my laptop :sunglasses::sunglasses::sunglasses:
## system
* Apple M2 Pro
* memsize: 32GB

## Here is the list
* Play with Huggingface model ~10B locally  
  * first try [**gemma_7b**](https://huggingface.co/google/gemma-7b), with `python gemma_7b.py`  
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
    
    doing
    
    
    
  
* Train a GPT-2 with private token and dataset(eg. py code model)
* 
