const emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"];

for (let i = 0; i < emails.length; i++) {
  for (let j = i + 1; j < emails.length; j++) {
    if (emails[i] === emails[j]) {
      console.log("Duplicate:", emails[i]);
    }
  }
}