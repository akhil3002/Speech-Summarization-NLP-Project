from transformers import BartForConditionalGeneration, BartTokenizer
import textwrap

def split_text(input_text, max_chars=1024):
    return textwrap.wrap(input_text, max_chars)

def summarize_chunk(chunk, model, tokenizer, max_length=130, min_length=30):
    inputs = tokenizer.encode("summarize: " + chunk, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize_long_text(input_text, max_chunk_size=1024, max_length=130, min_length=30):
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    chunks = split_text(input_text, max_chars=max_chunk_size)
    summaries = [summarize_chunk(chunk, model, tokenizer, max_length, min_length) for chunk in chunks]
    return " ".join(summaries)