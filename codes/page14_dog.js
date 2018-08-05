import Animal from "./animal.js";

class Dog extends Animal {
  // getHumanAgeメソッドを追加してください
  getHumanAge(){
  return this.age * 7;
}
  
}

export default Dog;
