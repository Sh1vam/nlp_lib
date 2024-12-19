from transformers import pipeline
# Load pre-trained QA model
qa_model = pipeline("question-answering")
# Example context and question
def q_a(context,question):
  # Answer the question
  answer = qa_model(question=question, context=context)
  return  answer['answer']

# Load pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")
# Example prompt
def generat(prompt):
  # Generate text
  generated_text = generator(prompt, max_length=50, num_return_sequences=1)
  returngenerated_text[0]['generated_text'])
