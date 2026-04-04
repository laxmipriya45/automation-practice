const emails = ["test@gmail.com", "wrong"];

emails.forEach(email => {
  if (email.includes("@") && email.includes(".")) {
    console.log("Valid:", email);
  } else {
    console.log("Invalid:", email);
  }
});