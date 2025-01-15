# Frontend
A react and typescript single page application bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

This service displays tax information and can display total prices it gets from the [backend](../backend/).

It uses [yarn](https://yarnpkg.com/getting-started/install) for building, testing and nearly everything else.

## Prerequisites
* [yarn](https://yarnpkg.com/getting-started/install)
* [nodejs](https://nodejs.org/en/download/)

## Installing dependencies
```bash
yarn install
```

## Tests and checks
To run all tests:
```bash
yarn test
```

### Auto-formatting
```bash
yarn format
```

### Linting
```bash
yarn lint
```

## Run locally
```bash
yarn start
```
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

## Build production version
```bash
yarn build
```
Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed! You can use this for example to build a docker container.


