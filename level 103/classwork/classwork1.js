class BankAccount {
  constructor(owner, balance) {
    this.owner = owner;   
    this.balance = balance; 
  }

  deposit(amount) {
    this.balance += amount;
    console.log(`${this.owner}-ეს ახალი ბალანსია: ${this.balance} ლარი`);
  }
}

const myAccount = new BankAccount("ნიკა", 50);

myAccount.deposit(20); 
