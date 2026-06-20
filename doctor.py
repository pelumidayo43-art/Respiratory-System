class RespiratoryDoctor:
    def __init__(self, name):
        self.name = name

    def diagnose(self, symptoms):
        print(f"Doctor {self.name} checking symptoms: {symptoms}")
        
        symptoms = symptoms.lower()
        
        if "cough" in symptoms and "fever" in symptoms:
            return "Possible flu or chest infection. Rest, fluids, and see a doctor if it lasts >3 days."
        elif "shortness of breath" in symptoms or "wheezing" in symptoms:
            return "Possible asthma/bronchitis. Please consult a doctor immediately."
        elif "cough" in symptoms:
            return "Common cold or mild cough. Stay hydrated and rest."
        else:
            return "Symptoms unclear. Please see a medical professional for proper diagnosis."
          
doc = RespiratoryDoctor("Dr. Pelumi")
user_input = input("Describe your respiratory symptoms: ")
result = doc.diagnose(user_input)
print("Diagnosis:", result)
