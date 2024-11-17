from transformers import pipeline

# Use a pre-trained summarization model for information extraction
def extract_information(prompt):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(prompt, max_length=50, min_length=25, do_sample=False)
    return result[0]["summary_text"]