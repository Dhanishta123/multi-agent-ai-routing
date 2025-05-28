import os
import json
from memory.shared_memory import SharedMemory

class JSONAgent:
    def __init__(self):
        self.memory = SharedMemory()

    def process(self, json_payload, source_id):
        print(f"[JSONAgent] Processing JSON data from source: {source_id}")
        required_fields = ["invoice_number", "date", "amount"]
        missing_fields = [field for field in required_fields if field not in json_payload]
        standardized = {
            "invoice_id": json_payload.get("invoice_number", "UNKNOWN"),
            "date": json_payload.get("date", "UNKNOWN"),
            "amount": json_payload.get("amount", 0),
            "client": json_payload.get("client", "UNKNOWN"),
            "status": "valid" if not missing_fields else "missing fields"
        }
        result = {
            "status": "Processed",
            "missing_fields": missing_fields,
            "normalized_data": standardized
        }
        self.memory.log(source_id + "_json", result)
        os.makedirs("outputs", exist_ok=True)
        output_path = os.path.join("outputs", f"{source_id}_json.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"[JSONAgent] Output successfully saved to: {output_path}")
        return result
