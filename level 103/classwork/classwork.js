class Car {
  constructor(brand, model) {
    this.brand = brand;
    this.model = model;
  }

  drive() {
    console.log(`The ${this.brand} ${this.model} is driving.`);
  }
}

const myCar = new Car("Toyota", "Corolla");
myCar.drive(); 
