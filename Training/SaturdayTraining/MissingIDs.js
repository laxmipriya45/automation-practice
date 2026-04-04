let expected = [1, 2, 3];
let actual = [1, 3];

for (let i = 0; i < expected.length; i++) {
  if (!actual.includes(expected[i])) {
    console.log("Missing:", expected[i]);
  }
}