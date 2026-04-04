let expected = [1, 2, 3];
let actual = [1, 5, 3];

for (let i = 0; i < expected.length; i++) {
  if (expected[i] === actual[i]) {
    console.log("Pass");
  } else {
    console.log("Fail");
  }
}