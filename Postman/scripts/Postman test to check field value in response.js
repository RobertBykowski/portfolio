pm.test("API response contains the expected fields", () => {
    const response = pm.response.json();
  
    // the line below checks value of the id field is 2 (number).
    pm.expect(response).to.have.property("id", 2);
  
    // the line below checks value of the name field is Morty Smith (string).
    pm.expect(response).to.have.property("name", "Morty Smith");
  });