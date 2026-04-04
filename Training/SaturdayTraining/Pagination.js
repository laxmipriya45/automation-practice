let p1 = [1, 2];
let p2 = [2, 3];

let all = p1.concat(p2);

for (let i = 0; i < all.length; i++) {
  for (let j = i + 1; j < all.length; j++) {
    if (all[i] === all[j]) {
      console.log("Duplicate:", all[i]);
    }
  }
}