import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from "react-router-dom";
import './index.css';


class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            course: '',
            year: null,
            semester: null
        }

        this.changeHandler = this.changeHandler.bind(this);
        this.submitHandler = this.submitHandler.bind(this);
    }

    changeHandler(event) {
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    submitHandler(event) {
        event.preventDefault();
        
    }

    render() {
        return (
            <>
                <div>
                    <form method="get">
                        <label>
                            Programme:
                            <input type="text" name="course" onChange={this.changeHandler} />
                        </label>
                        <label>
                            Year of Study:
                            <input type="text" name="year" onChange={this.changeHandler} />
                        </label>
                        <label>
                            Semester:
                            <select name="semester" >
                                <option value="one">1</option>
                                <option value="two">2</option>
                            </select>
                        </label>
                        <label>
                            Search
                            <input type="Submit" value="Submit" name="search for course" />
                        </label>
                    </form>
                </div>
                <BrowserRouter>
                    <Route path ="/" exact component={Search} />
                </BrowserRouter>
            </>
        );
    }
}

ReactDOM.render(<Search />, document.getElementById('root'));