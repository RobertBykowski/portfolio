pm.test("API response contians the expected header", () => {
    pm.response.to.have.header("Content-Type", "application/json; charset=utf-8");
  });