import subprocess
import sys
import os

sys.stderr = open(os.devnull, 'w')

def suppress_console_error():
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.kernel32.GetConsoleMode(-1, None)
        except Exception:
            pass

suppress_console_error()

import gradio as gr

def run_ollama(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama3.1:8b', prompt],
        stdout=subprocess.PIPE
    )
    return result.stdout.decode('utf-8')

def generate_response(prompt):
    response = run_ollama(prompt)
    return response

interface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Llama 3.1 Text Generator",
    description="Generate text using the Llama 3.1 model via Ollama."
)

if __name__ == "__main__":
    interface.launch()
