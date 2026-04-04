let arr = [1, 2, 5, 4];

let sorted = true;

for (let i = 0; i < arr.length - 1; i++) {
  if (arr[i] > arr[i + 1]) {
    sorted = false;
  }
}

if (sorted) console.log("Sorted");
else console.log("Not Sorted");