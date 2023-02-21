pm.test("the endpoint does not return unexpected status code", () => {
    // change 404 to the response code you do not expect
    const expectedStatusCode = 404;
  
    pm.response.to.not.have.status(expectedStatusCode);
  });