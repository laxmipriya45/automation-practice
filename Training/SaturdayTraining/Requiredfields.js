let data = [{ id: 1, name: "A" }, { id: 2 }];

for (let i = 0; i < data.length; i++) {
  if (!data[i].id || !data[i].name) {
    console.log("Missing Fields");
  }
}