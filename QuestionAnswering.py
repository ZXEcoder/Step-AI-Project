from transformers import pipeline

class QuestionAnswering:
    def __init__(self):
        self.qa_pipeline = pipeline('question-answering')

    def answer_question(self, question, context):
        result = self.qa_pipeline(question=question, context=context)
        return result['answer']

if __name__ == "__main__":
    qa = QuestionAnswering()
    context = "Provide context text here"
    question = "What is the question?"
    answer = qa.answer_question(question, context)
    print(f"Answer: {answer}")
