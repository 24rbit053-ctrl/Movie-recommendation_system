import json
with open(r"C:\Users\Vigneshwaran M\.gemini\antigravity\brain\5b58cd4a-f4b6-4562-a19a-f09c7a0f3a2f\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f_in:
    for line in f_in:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step is not None and 600 <= step < 695:
                print(f"Step {step} (source={data.get('source')}, type={data.get('type')}):")
                content = data.get("content", "")
                if content:
                    print("  Content:", repr(content[:400]) + "...")
                if "tool_calls" in data and data["tool_calls"]:
                    print("  Tool calls:")
                    for tc in data["tool_calls"]:
                        print(f"    - {tc.get('name')}: {list(tc.get('arguments', {}).keys())}")
        except Exception as e:
            pass
