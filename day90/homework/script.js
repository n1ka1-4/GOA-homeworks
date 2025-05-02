class Temp{
    #minTemp;
    #maxTemp;
    #currentTemp;
    #mode;
    constructor(minTemp, maxTemp, currentTemp, mode) {
        this.#minTemp = minTemp;
        this.#maxTemp = maxTemp;
        this.#currentTemp = this.#rangeTemp(currentTemp);
        this.#mode = mode;
    }
    #rangeTemp(temp) {
        if (temp < this.#minTemp) return this.#minTemp;
        if (temp > this.#maxTemp) return this.#maxTemp;
        return temp;
    }
    adjustTemp(temp) {
        this.#currentTemp = this.#rangeTemp(temp);
    }
    changeMode(mode) {
        const Modes = ["cool", "heat", "off"];
        if (!Modes.includes(mode)) return;
        else {
            this.#mode = mode;
        }
    }
    getCurrentTemp() {
        return this.#currentTemp;
    }
}

const temp = new Temp(16, 30, 20, "cool");
temp.adjustTemp(15);
temp.changeMode("off");
console.log(temp.getCurrentTemp());

class SecureNote {
    #content;
    #pin;
    constructor(content, pin) {
        this.#content = content;
        this.#pin = pin;
    }
    #validatePin(pin) {
        if (pin !== this.#pin) {
            alert("invalid PIN");
        } else {
            return true;
        }
    }
    updateContent(newContent, pin) {
        if (this.#validatePin(pin)) {
            this.#content = newContent;
        }
    }
    getContent(pin) {
        if (pin !== this.#pin) {
            alert("invalid PIN");
            return;
        } else {
            return this.#content;
        }
    }
}

const note = new SecureNote("this is a secret note", "1234");
note.updateContent("this is an updated secret note", "1234");
console.log(note.getContent("1234"));

class InventoryItem {
    #name;
    #quantity;
    #cost;
    constructor(name, quantity, cost) {
        this.#name = name;
        this.#quantity = quantity;
        this.#cost = cost;
    }
    restock(money) {
        if (money <= 0) {
            alert("restock money must be positive");
            return;
        }
        this.#quantity += money;
    }
    sell(money) {
        if (money <= 0) {
            alert("sell money must be positive");
            return;
        }
        if (money > this.#quantity) {
            alert("not enough stock to sell");
            return;
        }
        this.#quantity -= money;
    }
    getInfo() {
        return this.#quantity;
    }
}

const item = new InventoryItem("pizza", 10, 5);
item.restock(5);
item.sell(6);
console.log(item.getInfo());

class EmailClient {
    #password;
    #inbox;
    constructor(email, password) {
        this.email = email;
        this.#password = password;
        this.#inbox = [];
    }
    login(password) {
        if (password !== this.#password) {
            alert("invalid password");
            return;
        } else {
            return true;
        }
    }
    sendEmail(to, message) {
        if (this.login(this.#password)) {
            to.#inbox.push({ from: this.email, message });
            this.#inbox.push({ to: to.email, message });
        }

    }
    readInbox() {
        return this.#inbox;
    }
}

const client1 = new EmailClient("1234@example.com", "1234");
const client2 = new EmailClient("2345@example.com", "1234");
client1.sendEmail(client2, "hello");
client2.sendEmail(client1, "hi");
console.log(client1.readInbox());
console.log(client2.readInbox());

class Subscription {
    #userID;
    #plan;
    #paymentMethod;
    constructor(userID, plan, paymentMethod) {
        this.#userID = userID;
        this.#plan = plan;
        this.#paymentMethod = paymentMethod;
    }
    #validatePayment(paymentMethod) {
        if (paymentMethod !== this.#paymentMethod) {
            alert("invalid payment method");
        } else {
            return true;
        }
    }
    upgradePlan(newPlan) {
        if (this.#validatePayment(this.#paymentMethod)) {
            this.#plan = newPlan;
        }
    }
}

const subscription = new Subscription("1234", "basic", "credit card");
subscription.upgradePlan("premium");
console.log(subscription);