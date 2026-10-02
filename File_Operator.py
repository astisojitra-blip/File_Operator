from datetime import datetime

class JournalManager:
    def __init__(self,filename="journal.txt"):
        self.filename=filename
        
    def create_file(self):
        try:
            with open(self.filename,"x"):
                pass
        
        except FileExistsError:
            pass
         
        except PermissionError:
            print("You do not have permission to create the journal file.")

#Add a new journal entry
    
    def add_entry(self):
        try:
            title = input("Enter your journal entry: ")

            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.create_file()

            with open(self.filename, "a") as file:
                file.write(f"[{date}]\n")
                file.write(f"{title}\n")

            print("Journal entry added successfully!")

        except PermissionError:
            print("Error: You do not have permission to write.")

        
            
#View all journal entries    
    def view_entry(self):
        try:
            with open(self.filename,"r")as file:
                data=file.read()
                
                if data:
                    print("your Journal Entries:")
                    print("-------------------------------")
                    print(data)
                else:
                    print("No journal entries found.")
                    
        except FileNotFoundError:
            print("The journal file does not exist. Please add a new entry first.")
            
        except PermissionError:
            print("Error: You do not have permission to read")
            
       

#search for an entry
    
    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                data = file.readlines()

            found = False
            date = ""
            title = ""

            for line in data:
                if date == "":
                    date = line
                else:
                    title = line

                    if keyword in date or keyword in title:
                        print("\nMatching Entries:")
                        print("-------------------------------")
                        print(date)
                        print(title)
                        found = True

                    date = ""
                    title = ""

            if not found:
                print("No entries were found for the keyword:",keyword)

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
                    print("Error: You do not have permission to read the journal file.")

#Delete all journal entries

    def delete_entry(self):
        try:
            confirm=input("Are you sureyou want to delete all entries? (yes/no):")
            if confirm=="yes":
                with open(self.filename,"w")as file:
                    pass
                
                print("All journal entries have been deleted.")
            
            elif confirm=="no":
                print("No journal entries to delete.")
                
        except FileNotFoundError:
            print("Journal file does not exist.")
        except PermissionError:
            print("You do not have permission to delete entries.")
            
                
journal=JournalManager()              

#main menu
print("Welcome to Personal Journal Manager...")
while True:
    print("Please select an option")  
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    
    
    
    
    choice=(input("User Input:\n"))
    
    if choice=="1":
        journal.add_entry()
        
    elif choice=="2":
        journal.view_entry()
    
    elif choice=="3":
        journal.search_entry()
        
    elif choice=="4":
        journal.delete_entry()
        
    elif choice=="5":
        print("Thank you for using Journal Manager. Goodbye!")
        break
        
    else:
        print("Invalid option.Please select a valid option from the menu.")