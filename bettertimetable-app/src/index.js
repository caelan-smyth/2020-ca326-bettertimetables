import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''}

        this.changeHandler = this.changeHandler.bind(this);
        //this.submitHandler = this.submitHandler.bind(this);
    }

    changeHandler(event) {
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    //submitHandler(event) {}

    render() {
        return (
            <div>
                <form method="get">
                    <label>
                        Programme:
                        <input type="text" name="course" onChange={this.changeHandler} />
                    </label><br />
                    <label>
                        Year of Study:
                        <input type="text" name="year" onChange={this.changeHandler} />
                    </label><br />
                    <label>
                        Semester:
                        <select name="semester" >
                            <option value="one">1</option>
                            <option value="two">2</option>
                        </select>
                    </label><br />
                    <input type="submit" value="Search" name="search for course" />
                </form>
            </div>
        );
    }
}

ReactDOM.render(<Search />, document.getElementById('root'));