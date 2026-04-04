let data = [1, 2, 2, 3];

for (let i = 0; i < data.length; i++) {
  for (let j = i + 1; j < data.length; j++) {
    if (data[i] === data[j]) {
      console.log("Duplicate:", data[i]);
    }
  }
}