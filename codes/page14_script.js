import Dog from "./dog.js";

const dog = new Dog("レオ", 4);
dog.info();

// dogに対してgetHumanAgeを呼び出してください
const humanAge = dog.getHumanAge();

// 「人間年齢で〇〇歳です」と出力してください
console.log(`人間年齢で${humanAge}歳です`);