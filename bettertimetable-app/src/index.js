import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './index.css';
import Timetable from './Timetable.js';
import Search from './search.js';

class App extends React.Component {
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/" exact component={Search} />
                </Switch>
            </Router>
        );
    }   
}

ReactDOM.render(<App />, document.getElementById('root'));