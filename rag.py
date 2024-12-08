import datasets
import gradio as gr
from litellm import completion
import glob

class Retriever:
    def __init__(self):
        self.dataset = datasets.load_dataset("wiki40b", "en")

    def search(self, query: str, semantic_search: bool, key_word_search: bool) -> str:
        return "I am a retriever"

# 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 key
def answerQuestion(api_key: str, query: str, semantic_search: bool, key_word_search: bool) -> str:
    response = completion(
        model="groq/llama3-8b-8192",
        messages=[
            {"role": "user", "content": query}
        ],
        api_key=api_key,
    )
    print(response)
    return response.choices[0].message.content


# main function

if __name__ == "__main__":
    gr.Interface(fn=answerQuestion, inputs=["text", "text", "checkbox", "checkbox"], outputs="text",
                 title="RAG Demo").launch()

# demo = gr.Interface(fn=answearQuestion, inputs=["text", "text", "checkbox", "checkbox"], outputs="text", title="RAG Demo")
# demo.launch()

# write gradio ui with 4 inputs: api_key, query and two flags 'semantic search' and 'key word search'
