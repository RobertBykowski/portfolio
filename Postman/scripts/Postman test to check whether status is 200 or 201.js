pm.test("the endpoint returns the expected status code", () => {
    // comma separate the valid response codes below
    const expectedStatusCodes = [200, 201];
  
    pm.expect(pm.response.code).to.be.oneOf(
      expectedStatusCodes,
      `expected response status to be one of ${expectedStatusCodes} but got ${pm.response.code}.`
    );
  });