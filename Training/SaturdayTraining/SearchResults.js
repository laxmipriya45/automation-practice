let results = ["apple phone", "tv"];
let key = "apple";

for (let i = 0; i < results.length; i++) {
  if (results[i].includes(key)) {
    console.log("Valid");
  } else {
    console.log("Invalid");
  }
}