const allowed = ["Admin", "User"];
const selected = ["Admin", "SuperUser"];

selected.forEach(value => {
  if (allowed.includes(value)) {
    console.log("Valid:", value);
  } else {
    console.log("Invalid:", value);
  }
});