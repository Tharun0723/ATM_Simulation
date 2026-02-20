import json

FILE_NAME = "account_data.json"
DEFAULT_PIN = "1234"

# Load account data
def load_account():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"balance": 1000}  # Default balance
    
# Save account data 
def save_account(data):
    with open(FILE_NAME, "w") as file:
              json.dump(data, file, indent=4)  

# ATM Functions
def check_balance(account):
     print(f"💰 Your current balance is: ₹{account['balance']}") 

def deposite(account):
     amount = float(input("Enter amount to deposite: ₹")) 
     if amount <= account["balance"] and amount >0:
        account["balance"] -= amount
        save_account(account)
        print("✅ Deposite successful!")
     else:
          print("❌ Invalid amount")

def withdraw(account):
     amount = float(input("Enter amount to withdraw: ₹"))
     if amount <= account["balance"] and amount > 0:
          account["balance"] -= amount
          save_account(account)
          print("✅ Withdrawal successful!")
     else:
          print("❌ Insufficient balance or invalid amount")

def main():
     account = load_account()

     print("🏧Welcome to Python ATM")

     # PIN verification
     pin = input("Enter your 4-digit PIN")

     if pin != DEFAULT_PIN:
          print("❌ Incorrect PIN. Access Denied.")
          return
     
     while True:
          print("\nSelect option:")
          print("1. Check Balance")
          print("2. Deposite")
          print("3. Withdraw")
          print("4. Exit")

          choice = input("Enter choice: ")

          if choice == "1":
               check_balance(account)
          elif choice == "2":
               deposite(account)
          elif choice == "3":
               withdraw(account)
          elif choice == "4":
               print("Thank you for using ATM!") 
               break
          else:
               print("❌ Invalid choice")
if __name__ == "__main__":
     main()              


      


