let inputs = ["text", "", "   ", null];

for (let i = 0; i < inputs.length; i++) {
  if (!inputs[i] || inputs[i].trim() === "") {
    console.log("Invalid");
  } else {
    console.log("Valid");
  }
}