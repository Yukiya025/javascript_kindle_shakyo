import Animal from "./animal.js";

class Dog extends Animal {
  // constructorを追加してください
  constructor(name, age, breed){
    super(name, age);
    this.breed = breed;
  }
  
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    // 「犬種は〇〇です」と出力してください
    console.log(`犬種は${this.breed}です`);
    
    console.log(`${this.age}歳です`);
    const humanAge = this.getHumanAge();
    console.log(`人間年齢で${humanAge}歳です`);
  }
  
  getHumanAge() {
    return this.age * 7;
  }
}

export default Dog;
