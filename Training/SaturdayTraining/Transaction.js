let t = ["Success", "Fail", "Success"];

let s = 0, f = 0;

for (let i = 0; i < t.length; i++) {
  if (t[i] === "Success") s++;
  else f++;
}

console.log("Success:", s);
console.log("Fail:", f);