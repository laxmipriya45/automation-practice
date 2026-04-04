const users = [
  { name: "John", email: "john@gmail.com", phone: "123" },
  { name: "", email: "test@gmail.com", phone: "456" }
];

users.forEach(user => {
  if (user.name === "" || user.email === "" || user.phone === "") {
    console.log("Invalid:", user);
  } else {
    console.log("Valid:", user);
  }
});