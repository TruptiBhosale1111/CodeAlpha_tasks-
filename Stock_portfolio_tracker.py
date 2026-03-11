#stock portfolio tracker
import datetime

hour = datetime.datetime.now().hour

if hour < 12:
    print("\nGood Morning!")
elif hour < 18:
    print("\nGood Afternoon!")
else:
    print("\nGood Evening!")

def run_portfolio_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 370, "AMZN": 140}
    
    print("\n=====WELCOME TO THE SIMPLE PORTFOLIO TRACKER =====")
    print(f"\nAvailable stocks: {', '.join(stock_prices.keys())}")

    stock_name = input("Enter stock name:\n").upper()

    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock_name} you own: \n"))
            price = stock_prices[stock_name]
            total_value = price * quantity

            result_msg = f"Your total investment in {stock_name} is: ${total_value:,}"
            print(f"\n{result_msg}")

            save_choice = input("Would you like to save this result to a file? (yes/no): ").lower()

            if save_choice == 'yes':
                with open("portfolio_summary.txt", "w") as file:
                    file.write("------- Portfolio Summary -------\n")
                    file.write(f"Stock: {stock_name}\n")
                    file.write(f"Quantity: {quantity}\n")
                    file.write(f"Price per share: ${price}\n")
                    file.write(f"{result_msg}\n")

                print("Result successfully saved to 'portfolio_summary.txt'.")
                print("\n<<thankyou!!>>")

        except ValueError:
            print("Error! Please enter a valid number for quantity.")
    else:
        print("Error: Stock not found.")


if __name__ == "__main__":
    run_portfolio_tracker()