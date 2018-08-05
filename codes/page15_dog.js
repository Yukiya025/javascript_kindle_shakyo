import Animal from "./animal.js";

class Dog extends Animal {
  // infoメソッドを追加してください
  info(){
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
    
    const humanAge = this.getHumanAge();
    console.log(`人間年齢で${humanAge}歳です`);
  }
  
  
  getHumanAge() {
    return this.age * 7;
  }
}

export default Dog;
