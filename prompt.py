from transformers import AutoTokenizer, AutoModelForCausalLM


try:
    print('Loading model...')
    model_checkpoint = "vicgalle/gpt2-alpaca-gpt4"
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

    model_options = [
        ("adamthekiwi/toki-pona", "DistilGPT2 trained on toki-pona data with custom prompt formatting"),
        ("adamthekiwi/toki-pona-better", "DistilGPT2 trained on toki-pona data with more prompt data, more epochs, and warmup steps"),
        ("adamthekiwi/toki-pona-gpt2-alpaca-better", "Pretrained GPT2 on GPT4 alpaca dataset. Trained with more variation in prompts. Uses same data as non-alpaca models but with alpaca prompt formatting"),
        ("adamthekiwi/toki-pona-gpt2-alpaca-best", "Pretrained GPT2 on GPT4 alpaca dataset. Trained with encyclopedia data. Uses same data as non-alpaca models but with alpaca prompt formatting"),
        # ("adamthekiwi/toki-pona-gpt2-alpaca", "Pretrained GPT2 on GPT4 alpaca dataset. Uses same data as non-alpaca models but with alpaca prompt formatting"),
        # ("adamthekiwi/toki-pona-gpt2", "GPT2 trained on toki-pona data with custom prompt formatting"),
    ]

    chosen_model = model_options[0]
    try:
        for i, x in enumerate(model_options):
            print(f'[{i+1}] {x[0]}: {x[1]}')
        chosen_model = model_options[int(input(f'Choose a model (default {chosen_model[0]}): '))-1]
    except KeyboardInterrupt:
        print('Goodbye!')
        exit(0)
    except Exception as e:
        print(f'Using default model ({chosen_model[0]})')

    model_test = AutoModelForCausalLM.from_pretrained(chosen_model[0])

    num_beams = 3
    try:
        num_beams = int(input(f'Enter number of beams to use in beam search (default {num_beams}): '))
    except KeyboardInterrupt:
        print('Goodbye!')
        exit(0)
    except Exception as e:
        num_beams = 3
        print(f'Using default number of beams ({num_beams})')

    max_length = 100
    try:
        max_length = int(input(f'Enter max length of output (default {max_length}): '))
    except KeyboardInterrupt:
        print('Goodbye!')
        exit(0)
    except Exception as e:
        print(f'Using default max length ({max_length})')

    while True:
        print('Encoding prompt...')
        prompt = input('Enter an instruction prompt: ')

        # input_ids = tokenizer.encode(f'''{prompt}\n=====\n''', return_tensors='pt')
        # print('Generating...')
        prompt = f'''Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:\n'''
        input_ids = tokenizer.encode(prompt, return_tensors='pt')
        print(prompt)
        
        # output = model_test.generate(input_ids, max_length=max_length, num_beams=num_beams, no_repeat_ngram_size=3, early_stopping=True)
        # print(f'{tokenizer.decode(output[0], skip_special_tokens=True)}')
        # input_ids = tokenizer.encode(f'''{prompt}\n=====\n''', return_tensors='pt')
        # input_ids = tokenizer.encode(f'''{prompt}\n>>>>>\n''', return_tensors='pt')
        print('Generating...')
        try:
            output = model_test.generate(input_ids, max_length=max_length, num_beams=num_beams, no_repeat_ngram_size=3, early_stopping=True)
        except KeyboardInterrupt:
            continue
        except Exception as e:
            print(e)
            exit(1)

        print(f'{tokenizer.decode(output[0], skip_special_tokens=True)}')
        # input_ids = tokenizer.encode(f'''Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:\n''', return_tensors='pt')
except KeyboardInterrupt:
    print('Goodbye!')
    exit(0)
except Exception as e:
    print(e)
    exit(1)