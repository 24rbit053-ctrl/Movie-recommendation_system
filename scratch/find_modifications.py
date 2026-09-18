import json

with open(r"C:\Users\Vigneshwaran M\.gemini\antigravity\brain\5b58cd4a-f4b6-4562-a19a-f09c7a0f3a2f\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            content = data.get("content", "")
            if "replace_file_content" in line or "multi_replace_file_content" in line or "write_to_file" in line:
                if any(x in content for x in ["style.css", "index.html", "main.js", "base.html"]):
                    print(f"Step {step} modified file(s). Content hint: {content[:150]}")
        except Exception as e:
            pass
