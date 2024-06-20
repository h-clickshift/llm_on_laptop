# Dreams can be true 🐇 <- 🐢  
# inference speedup outline  
* quantization （float32 -> float16 -> int8）
* paralelle
* system level optimize

| Model       |MEM consume   | Dtype           | Device         |Time Cost(s) |Prompt  |Response|  
| ------------|------------- | --------------- |-----------------|--|--|--|
| chatglm-6b    | 18GB  |    float16   |mps| 13  | HI,I am a language model.     |  I am here to assist you with any questions you may have. How can I help you today?
| chatglm-6b    | ?GB  |    bfloat16   |mps| running...  | HI,I am a language model.     |  

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
   change model dtype to float32 with `model.to(device, dtype=torch.bfloat16)`  
    > ** time cost:21.84215497970581s **  33.3% ↘️ 🎱  
    > ** time per token: 1.465056906231649 **  
