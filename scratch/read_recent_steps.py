import json

with open(r"C:\Users\Vigneshwaran M\.gemini\antigravity\brain\5b58cd4a-f4b6-4562-a19a-f09c7a0f3a2f\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step in [744, 745]:
                print(f"Step {step}:")
                content = data.get("content", "")
                print(content)
        except Exception as e:
            pass
