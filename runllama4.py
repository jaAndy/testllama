from transformers import AutoTokenizer
import transformers 
import torch
model = "/root/EE/output/version2/503B_FT_lr1e-5_ep5_top1_2023-08-25/checkpoint-610"
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

CHAT_EOS_TOKEN_ID = 32002


def inference(prompt="Придумай 10 самых необычных рецептов блинчиков, желательно так, чтобы их ингредиенты сочетались между собой, а ещё лучше, чтобы их можно было бы приготовить дома"): # "Are secretory phospholipases A2 secreted from ciliated cells and increase mucin and eicosanoid secretion from goblet cells? You just need to answer yes or no"
    formatted_prompt = (
        f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
    )


    sequences = pipeline(
        formatted_prompt,
        do_sample=True,
        top_k=50,
        top_p = 0.9,
        num_return_sequences=1,
        repetition_penalty=1.1,
        max_new_tokens=1024,
        eos_token_id=CHAT_EOS_TOKEN_ID,
    )

    # for seq in sequences:
    #     print(f"Result: {seq['generated_text']}")
    return sequences[0]['generated_text']

# ret = inferece()
# print(ret)
import datasets

pubmed_dataset = datasets.load_dataset("qiaojin/PubMedQA", "pqa_artificial")

for sample_id in range(100): # pubmed_dataset['train'][: 100]:
    sample = pubmed_dataset['train'][sample_id]
    print(sample)
    question = sample['question']
    answer = inference(question)
    print(f'Q: {question}\nA:{answer}')
