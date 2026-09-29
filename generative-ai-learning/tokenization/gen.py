import tiktoken

text = "I'm Iron Man!"

tokenizer = tiktoken.encoding_for_model(model_name="gpt-4")
tokenIds = tokenizer.encode(text)

print(tokenizer.decode(tokenIds))

print(tokenIds)


print()
print('=' * 52)
print()


# Check Online :- https://huggingface.co/spaces/Xenova/the-tokenizer-playground

# Tokenization experiment using Hugging Face Tokenizer Playground
# Tokens : 5
# Characters : 13

resultIds = [40, 2846, 16979, 2418, 0]
result = tokenizer.decode(resultIds)
print(result)


