let ui = ["A", "B", "C"];
let exp = ["A", "X", "C"];

for (let i = 0; i < ui.length; i++) {
  if (ui[i] !== exp[i]) {
    console.log("Mismatch");
  }
}