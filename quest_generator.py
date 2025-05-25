import requests
import json

def generate_quest(biome: str, level: int) -> str:
    prompt = (
        f"Generate a detailed medieval fantasy quest for a level {level} player in a {biome} biome. "
        "Include: quest title, NPC name and backstory, objective, challenges, and rewards."
    )
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt},
            stream=True,
            timeout=60
        )
        quest = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    quest += data.get("response", "")
                except Exception as e:
                    continue

        if quest.strip():
            return quest.strip()
        else:
            return "🧙 No quest generated. Please try again."
        
    except Exception as e:
        print("❌ Error contacting LLM:", e)
        return f"❌ Failed to connect to LLM: {e}"
