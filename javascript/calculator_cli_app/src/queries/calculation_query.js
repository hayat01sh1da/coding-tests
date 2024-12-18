const http = require("http")

const CalculationQuery = class {
  constructor(seed) {
    this.seed = seed
    this.uri  = null
  }

  f(n) {
    if (n == 0) {
      return 1;
    } else if (n == 2) {
      return 2;
    } else if (n % 2 == 0) {
      return this.f(n - 1) + this.f(n - 2) + this.f(n - 3) + this.f(n - 4)
    } else {
      return this.__ask_server__(n);
    }
  }

  // private

  __uri__() {
    if (this.uri === null) {
      this.uri = process.env.CALCULATION_API;
      return this.uri;
    } else {
      return this.uri;
    }
  }

  __ask_server__(n) {
    let result;
    http.get(`${this.__uri__()}?seed=${this.seed}&n=${n}`, (res) => {
      let body = "";
      res.setEncoding("utf8");

      res.on("data", (chunk) => {
        body += chunk;
      });

      res.on("end", (res) => {
        result = JSON.parse(body).result;
      });

    }).on("error", (error) => {
      result = error.message;
    });
    return result;
  }
}

export default CalculationQuery
