from utils.file_parser import detect_format, extract_text
from memory.shared_memory import SharedMemory
import re

class ClassifierAgent:
    def __init__(self):
        self.memory = SharedMemory()

    def classify(self, input_data, source_id):
        file_format = detect_format(input_data)
        text = extract_text(input_data, file_format)

        intent = self._detect_intent(text)
        self.memory.log(source_id, {"format": file_format, "intent": intent})
        return file_format, intent

    def _detect_intent(self, text):
        if re.search(r'invoice', text, re.IGNORECASE):
            return "Invoice"
        elif re.search(r'rfq|request for quote', text, re.IGNORECASE):
            return "RFQ"
        elif re.search(r'complaint|issue', text, re.IGNORECASE):
            return "Complaint"
        elif re.search(r'regulation', text, re.IGNORECASE):
            return "Regulation"
        else:
            return "Unknown"