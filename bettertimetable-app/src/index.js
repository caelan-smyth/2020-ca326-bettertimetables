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
            <form method="get">
                <label>
                    Programme:
                    <input type="text" name="course" onChange={this.changeHandler} />
                </label><br />
                <label>
                    Year of Study:
                    <input type="text" name="year" onChange={this.changeHandler} />
                </label><br />
                <input type="submit" value="Search" />
            </form>
        );
    }
}

ReactDOM.render(<Search />, document.getElementById('root'));