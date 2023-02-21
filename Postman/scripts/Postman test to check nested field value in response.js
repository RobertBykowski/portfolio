pm.test("API response contains the expected fields", () => {
    const response = pm.response.json();
  
    // the line below checks value of the id field is 2 (number).
    pm.expect(response).to.have.nested.property("id", 2);
  
    // the line below checks value of the name field is Morty Smith (string).
    pm.expect(response).to.have.nested.property("name", "Morty Smith");
  
    // the line below checks value of the origin.name field is Earth (C-137) (string).
    pm.expect(response).to.have.nested.property("origin.name", "Earth (C-137)");
  });