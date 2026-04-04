let users = ["john", "mary", "john"];

for (let i = 0; i < users.length; i++) {
  for (let j = i + 1; j < users.length; j++) {
    if (users[i] === users[j]) {
      console.log("Duplicate:", users[i]);
    }
  }
}