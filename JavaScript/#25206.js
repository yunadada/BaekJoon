const input = require("fs")
  .readFileSync("./JavaScript/example.txt")
  .toString()
  .trim()
  .split("\n");

var GPA = 0;
var totalCredits = 0;
for (let i = 0; i < input.length; i++) {
  let [subject, credit, grade] = input[i].split(" ");

  if (grade.trim() === "P") {
    continue;
  }

  let score = 0;
  credit = parseFloat(credit);

  totalCredits += credit;
  switch (grade.trim()) {
    case "A+":
      score = credit * 4.5;
      GPA += score;
      break;
    case "A0":
      score = credit * 4.0;
      GPA += score;
      break;
    case "B+":
      score = credit * 3.5;
      GPA += score;
      break;
    case "B0":
      score = credit * 3.0;
      GPA += score;
      break;
    case "C+":
      score = credit * 2.5;
      GPA += score;
      break;
    case "C0":
      score = credit * 2.0;
      GPA += score;
      break;
    case "D+":
      score = credit * 1.5;
      GPA += score;
      break;
    case "D0":
      score = credit * 1.0;
      GPA += score;
      break;
    case "F":
      GPA += 0;
      break;
  }
}

console.log(GPA / totalCredits);
