"use strict;"

const Application = class {
  constructor(str_1, str_2) {
    this.str_1 = str_1;
    this.str_2 = str_2;
  }

  exactly_equal_size_and_included() {
    return this.__sort_string__(this.str_1) === this.__sort_string__(this.str_2);
  }

  // private

  __sort_string__(str) {
    return str.split("").sort().join("");
  }
}

export default Application
