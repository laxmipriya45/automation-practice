let password = "Test123";

let upper = false;
let number = false;

for (let i = 0; i < password.length; i++) {
  let ch = password[i];

  if (ch >= 'A' && ch <= 'Z') upper = true;
  if (ch >= '0' && ch <= '9') number = true;
}

if (upper && number && password.length >= 6) {
  console.log("Valid");
} else {
  console.log("Invalid");
}