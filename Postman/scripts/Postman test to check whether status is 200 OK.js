pm.test("the endpoint returns the expected status code", () => {
  // change 200 to the response code you expect
  const expectedStatusCode = 200;

  pm.response.to.have.status(expectedStatusCode);
});