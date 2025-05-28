from memory.shared_memory import SharedMemory
import re
import os
import json

class EmailAgent:
    def __init__(self):
        self.memory = SharedMemory()

    def process(self, email_text, source_id):  
        print(f"[EmailAgent] Processing email from source: {source_id}")  

        sender_match = re.search(r'From:\s*(.+)', email_text)  
        sender = sender_match.group(1).strip() if sender_match else "Unknown"  

        urgency = "High" if "urgent" in email_text.lower() else "Normal"  
 
        summary = email_text.strip()[:200]  

        result = {  
            "sender": sender,  
            "urgency": urgency,  
            "summary": summary  
        }  

        self.memory.log(source_id + "_email", result)  

        os.makedirs("outputs", exist_ok=True)  
  
        output_path = os.path.join("outputs", f"{source_id}_email.json")  
        with open(output_path, "w", encoding="utf-8") as f:  
            json.dump(result, f, indent=2)  

        print(f"[EmailAgent] Output successfully saved to: {output_path}")  
        return result