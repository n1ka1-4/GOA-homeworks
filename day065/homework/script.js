// 1

function Person(name, age, job, height, weight) {
  this.name = name;
  this.age = age;
  this.job = job;
  this.height = height;
  this.weight = weight;
}

person = new Person("John", 25, "Software Developer", 180, 80);

// 2

function motorbike(brand, model, boost, engine, color) {
  this.brand = brand;
  this.model = model;
  this.boost = function() {
    return this.engine * this.boost / 100;
  };
  this.engine = engine;
  this.color = color;
}

motorbike = new motorbike("Yamaha", "MT-07", 74, 689, "black");
