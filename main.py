from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
import json

if __name__ == "__main__":
    classifier = ClassifierAgent()
    json_agent = JSONAgent()
    email_agent = EmailAgent()

    inputs = [
        ("inputs/sample_email.txt", "email1"),
        ("inputs/sample_invoice.json", "json1")
    ]

    for input_path, source_id in inputs:
        if input_path.endswith(".json"):
            with open(input_path) as f:
                json_data = json.load(f)
            format, intent = classifier.classify(json_data, source_id)
            print(f"Detected format: {format}")
            print(f"Detected intent: {intent}")
            if format == "JSON":
                result=json_agent.process(json_data, source_id)
                print("JSONAgent Output:")
                print(result)
            else:
                print("Unsupported format for JSONAgent.")
        else:
            format, intent = classifier.classify(input_path, source_id)
            print(f"Detected format: {format}")
            print(f"Detected intent: {intent}")
            if format == "Email":
                with open(input_path) as f:
                    email_text = f.read()
                result=email_agent.process(email_text, source_id)
                print("EmailAgent Output:")
                print(result)
            else:
                print("Unsupported format for EmailAgent.")
    print("\nAll inputs processed successfully.")