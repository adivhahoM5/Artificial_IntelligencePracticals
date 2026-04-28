knowledge_base = {
    "flu":          ["fever", "cough", "sore_throat"],
    "common_cold":  ["sneezing", "runny_nose", "mild_fever"],
    "malaria":      ["fever", "chills", "sweating", "headache"],
    "covid19":      ["fever", "cough", "shortness_of_breath", "loss_of_taste"],
    "strep_throat": ["sore_throat", "swollen_lymph_nodes", "fever"],
}

advice_base = {
    "flu":          ["Drink  fluids.", " rest.", " and consult a doctor if symptoms worsen."],
    "common_cold":  ["Rest.", "Drink warm fluids.", "Avoid contact with others."],
    "malaria":      ["See a doctor as soon as possible.", "Drink fluids to stay hydrated.", "Avoid self-medicating."],
    "covid19":      ["Isolate yourself.", "Seek medical advice.", "Monitor your symptoms closely."],
    "strep_throat": ["Rest your voice.", "Drink warm fluids.", "See a doctor if symptoms persist."],
}


def get_user_symptom():
    print("Welcome to HealthBot!")
    print("Enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip().replace(" ", "_") for s in user_input.split(",")]
    return symptoms


def infer_disese(user_symptoms):
    possible_diseases = []
    for disease, required_symptoms in knowledge_base.items():
        if all(symptom in user_symptoms for symptom in required_symptoms):
            possible_diseases.append(disease)
    return possible_diseases


def run_chatbot():
    user_symptms = get_user_symptom()
    diseases = infer_disese(user_symptms)

    if diseases:
        print("\nBased on your symptoms, you might have:")
        for disease in diseases:
            print(f"- {disease.title()}")
            for advice in advice_base.get(disease, ["Please consult a doctor."]):
                print(f"  Advice: {advice}")
    else:
        print("\nNo matching disease found.")
        print("Please consult a healthcare professional.")


run_chatbot()