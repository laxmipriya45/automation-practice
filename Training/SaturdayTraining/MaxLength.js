const inputs = ["hello", "veryverylongtext"];

inputs.forEach(input => {
  if (input.length > 10) {
    console.log("Invalid:", input);
  } else {
    console.log("Valid:", input);
  }
});