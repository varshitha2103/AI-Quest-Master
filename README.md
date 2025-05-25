# AI-Quest-Master
AI Quest Master is a web application that generates immersive, medieval fantasy quests based on user-selected biomes and player levels. Powered by Mistral LLM (via Ollama) and built with Gradio, it’s the perfect tool for game masters, writers, and creative adventurers!

🚀 Features
✅ Generate detailed medieval fantasy quests
✅ Select a biome and player level for tailored outputs
✅ Easy-to-use web interface built with Gradio
✅ Local LLM integration via Ollama (no API keys required!)
✅ Ready for integration into games like Minecraft

📸 Demo
<img width="956" alt="res1" src="https://github.com/user-attachments/assets/48e2c77d-ee2b-46a8-ae56-f93c9e7c42d8" />

🏗️ Tech Stack
Python 3.11+
Gradio for web UI
Ollama for local LLM serving
Mistral LLM for generating quests

🛠️ Setup Instructions
1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

2️⃣ Set Up Ollama and LLM
Install Ollama: https://ollama.com
Pull the Mistral model:
```bash
ollama pull mistral
```

Confirm it’s available:
```bash
ollama list
```
3️⃣ Run the App
```bash
python ui.py
```

Access the web app at:
👉 http://127.0.0.1:7860

🔥 Example Output
```yaml
Quest Title: "The Broken Pact of the Sun-Scarred Plains"
NPC Name: Elder Garrick (a wise, aging ranger)
Backstory: ...
Objective: ...
Challenges: ...
```

🧩 Future Enhancements
🌍 Add more biomes (e.g., tundra, cave, volcano)
🧭 Export quests as PDF/Markdown
🎮 Integrate with Minecraft server for live quests
🎨 Enhance UI with fantasy-themed styling
