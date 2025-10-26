class Patient:
    def __init__(self, name: str, symptoms: list[str]):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name.lower()] = result

    def has_covid(self) -> float:
        if "covid" in self.tests:
            return 0.99 if self.tests["covid"] else 0.01

        probability = 0.05
        covid_symptoms = ['fever', 'cough', 'anosmia']
        for symptom in covid_symptoms:
            if symptom in self.symptoms:
                probability += 0.1

        return min(probability, 1.0)