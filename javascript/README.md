## 1. Environment

- Node v25.6.0
- PNPM 10.25.0

## 2. JEST install for Unit Test

### 2-1. Build a Node.js project

```bash
$ pnpm init
```

You will be asked some questions, but just keep tapping "Enter" key.

### 2-2. Install required packages

```bash
$ pnpm install --save-dev jest babel-jest babel-core @babel/core @babel/preset-env
```

### 2-3. Install a plugin with babel to convert JEST to CommonJS

```bash
$ pnpm install --save-dev jest babel-jest
```

### 2-4. Run a unittest

To execute all unit tests, run `npx jest`.

```bash
$ pnpm jest
 PASS  __tests__/hello.test.js (24.047 s)
  ✓ Hello (3 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        48.781 s
Ran all test suites.
```
