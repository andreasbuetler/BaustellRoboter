fetch(
  "https://baustellrobots-default-rtdb.europe-west1.firebasedatabase.app/helmetStates.json",
  requestOptions
)
  .then((response) => response.json())
  .then((result) => {
      this.helmetStates = Object.values(result);
  })
  .catch((error) => console.log("error", error));


