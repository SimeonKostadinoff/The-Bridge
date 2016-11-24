import React from 'react';
import { render } from 'react-dom';
import Root from './containers/Root';
//import configureStore from './redux/configureStore';
import rootReducer from './redux/reducers/index'
import routes from './routes';
import { syncHistoryWithStore, routerMiddleware } from 'react-router-redux';
import { hashHistory  } from 'react-router';
import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers,
} from "redux"

import thunk from "redux-thunk"

let finalCreateStore = compose(
  applyMiddleware(thunk),
  window.devToolsExtension ? window.devToolsExtension() : f => f
)(createStore)

console.log("Reducers",rootReducer)
let reducer = combineReducers(rootReducer)
let store = finalCreateStore(rootReducer)

// Apply the middleware to the store
// const middleware = routerMiddleware(hashHistory);

// const store = configureStore(middleware);
const history = syncHistoryWithStore(hashHistory, store)

// console.log("Store: ", store)

render(
    <Root history={history} store={store} routes={routes} debug={false} />,
    document.getElementById('organisation_view') 
);