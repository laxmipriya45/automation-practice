const attempts = ["fail", "fail", "fail", "success"];
let count = 0;

for (let i = 0; i < attempts.length; i++) {
  if (attempts[i] === "fail") {
    count++;
    console.log("Failed");

    if (count === 3) {
      console.log("Stop after 3 failures");
      break;
    }
  } else {
    console.log("Login Success");
    break;
  }
}