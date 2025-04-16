class BankAccount {
    #accountNumber
    #balance
    #pin
    #validatePin(pin) {
        if (pin !== this.#pin) {
            alert("Invalid PIN");
        } else {
            return true;
        }
    }
    #setBalance(amount){
        if (amount < 0) {
            alert("Balance cannot be negative");
        }
        this.#balance = amount;
    }

    constructor(accountNumber, initialBalance, pin) {
        this.#accountNumber = accountNumber;
        this.#balance = initialBalance;
        this.#pin = pin;
    }
    deposit(amount) {
            if (amount <= 0) {
                alert("Deposit money must not be negative");
                return;
            }
            this.#setBalance(this.#balance + amount);
        }
    withdraw(amount, pin) {
        this.#validatePin(pin);
        if (amount <= 0) {
            alert("Withdrawal money must not be negative");
            return;
        }
        if (amount > this.#balance) {
            alert("you dont have enough money");
            return;
        }
        this.#setBalance(this.#balance - amount);
    }
    checkBalance(pin) {
        if (pin !== this.#pin) {
            alert("Invalid PIN");
            return;
        } else {
            return this.#balance;
        };
    }


    get accountNumber () {
        return this.#accountNumber;
    }
    set set_pin (pin) {
        this.#pin = pin;
    }
}