"""
 This is executed after a model is successfully generated.
 With random data inputs, the model is tested.
 
 The expected intents are classified as expected with sample data
"""

from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/intentClassifier")

# Test with sample data
print(json.dumps(interpreter.parse("Where are you from?")["intent"], indent=2))
print(json.dumps(interpreter.parse("Gd mrng babie")["intent"], indent=2))
print(json.dumps(interpreter.parse("Tq very much for ur hlp")["intent"], indent=2))
print(json.dumps(interpreter.parse("sry, I can't help")["intent"], indent=2))
print(json.dumps(interpreter.parse("hallo")["intent"], indent=2))