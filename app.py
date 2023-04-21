import gradio as gr
import openai
import pandas as pd 
import numpy as np
import os
openai.api_key="openai_apiKey"
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

def similarity(input):
    df= pd.read_csv("meg_embeddings.csv")
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)
    input = input
    input_vector = get_embedding(input, engine="text-embedding-ada-002")
    df["similarities"] = df['embedding'].apply(lambda x: cosine_similarity(x, input_vector))
    sorted_df =df.sort_values("similarities", ascending=False)
    top_row = sorted_df.loc[0]
    return sorted_df.iloc[0][["text", "similarities"]]
    
input_text = gr.inputs.Textbox(label="Enter your text here")
text_output = gr.outputs.Textbox(label="Most similar text")
similarity_output = gr.outputs.Textbox(label="Similarity score")

ui = gr.Interface(fn=similarity,
                  inputs=input_text,
                  outputs=[text_output, similarity_output],
                  title="Semantic Plagiarism Checker",
                  description="Check if your text is semantically similar to pre-existing texts to prevent plagiarism.",
                  theme="compact",
                  layout="vertical",
                  inputs_layout="stacked",
                  outputs_layout="stacked",
                  allow_flagging=False)



ui.launch()