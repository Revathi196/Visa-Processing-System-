# main.py

from visa_processing_system import VisaProcessingSystem

def main():
    visa_system = VisaProcessingSystem()

    while True:
        print("\nVisa Processing System")
        print("1. Apply for Visa")
        print("2. Check Application Status")
        print("3. Update Application Status")
        print("4. View All Applications")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            applicant_name = input("Enter applicant name: ").strip()
            nationality = input("Enter applicant nationality: ").strip()
            visa_type = input("Enter visa type (Tourist/Work/Student): ").strip()
            application_id = visa_system.apply_visa(applicant_name, nationality, visa_type)

        elif choice == '2':
            application_id = input("Enter application ID: ").strip()
            visa_system.check_application_status(application_id)

        elif choice == '3':
            application_id = input("Enter application ID: ").strip()
            status = input("Enter new status (Approved/Denied/Pending): ").strip()
            visa_system.update_application_status(application_id, status)

        elif choice == '4':
            visa_system.view_all_applications()

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
