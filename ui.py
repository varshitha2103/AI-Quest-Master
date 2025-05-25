import requests

# Warm up mistral model (optional but useful)
def warmup_model():
    try:
        r = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": "ping",
            "stream": False
        }, timeout=30)
        print("🔥 Mistral model is warmed up.")
    except Exception as e:
        print("⚠️ Could not warm up model:", e)

warmup_model()


import gradio as gr
import subprocess
import time
import psutil
from quest_generator import generate_quest

# 🚀 Check and auto-start Ollama if not running
def start_ollama_if_not_running():
    ollama_running = any("ollama" in (p.name() or "").lower() for p in psutil.process_iter(['name']))
    if not ollama_running:
        print("🧠 Ollama not running. Starting Mistral model...")
        subprocess.Popen(["ollama", "run", "mistral"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(10)  # Give it a few seconds to fully load
    else:
        print("✅ Ollama already running.")

start_ollama_if_not_running()

def run_quest_gen(biome, level):
    try:
        level = int(level)
    except ValueError:
        return "⚠️ Please enter a valid level number."
    return generate_quest(biome, level)

biomes = ["desert", "forest", "swamp", "mountains", "plains", "ocean"]

demo = gr.Interface(
    fn=run_quest_gen,
    inputs=[
        gr.Dropdown(choices=biomes, label="Biome", value="desert"),
        gr.Textbox(label="Player Level", value="7")
    ],
    outputs=gr.Textbox(label="🧙 Generated Quest"),
    title="AI Quest Master",
    description="Generate medieval fantasy quests with Mistral (powered by Ollama)"
)

if __name__ == "__main__":
    demo.launch()
