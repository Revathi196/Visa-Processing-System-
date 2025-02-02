# visa_processing_system.py
import uuid
from datetime import datetime

class VisaApplication:
    def __init__(self, applicant_name, nationality, visa_type, status="Pending"):
        self.application_id = str(uuid.uuid4())  # Unique application ID
        self.applicant_name = applicant_name
        self.nationality = nationality
        self.visa_type = visa_type
        self.status = status
        self.application_date = datetime.now()

    def __repr__(self):
        return f"Application ID: {self.application_id}, Name: {self.applicant_name}, Status: {self.status}, Visa Type: {self.visa_type}, Application Date: {self.application_date.strftime('%Y-%m-%d %H:%M:%S')}"

class VisaProcessingSystem:
    def __init__(self):
        self.applications = {}

    def apply_visa(self, applicant_name, nationality, visa_type):
        """Create a new visa application."""
        application = VisaApplication(applicant_name, nationality, visa_type)
        self.applications[application.application_id] = application
        print(f"Visa application submitted successfully. Application ID: {application.application_id}")
        return application.application_id

    def check_application_status(self, application_id):
        """Check the status of an existing application."""
        application = self.applications.get(application_id)
        if application:
            print(f"Application Status: {application.status}")
        else:
            print(f"Application ID {application_id} not found.")

    def update_application_status(self, application_id, status):
        """Update the status of an application."""
        application = self.applications.get(application_id)
        if application:
            application.status = status
            print(f"Application ID {application_id} status updated to: {status}")
        else:
            print(f"Application ID {application_id} not found.")

    def view_all_applications(self):
        """View all applications."""
        if self.applications:
            for application in self.applications.values():
                print(application)
        else:
            print("No applications found.")

