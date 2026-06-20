class Doctor(Person):
    def __init__(self, name, age, staff_id, specialty):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.specialty = specialty
        self.patients = []

    def diagnose(self, patient):
        return f"Dr. {self.name} diagnosed {patient.name} with {patient.symptoms}"

    def add_patient(self, patient):
        self.patients.append(patient)
        return f"{patient.name} assigned to Dr. {self.name}"

    def list_patients(self):
        if not self.patients:
            return f"Dr. {self.name} has no patients yet"
        return [p.name for p in self.patients]

    def __str__(self):
        return f"Dr. {self.name}, Specialty: {self.specialty}, Staff ID: {self.staff_id}"
