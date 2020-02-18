import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import { CsvToHtmlTable } from 'react-csv-to-table';

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            course: '',
            year: null,
            semester: null,
        }

        this.changeHandler = this.changeHandler.bind(this);
        this.submitHandler = this.submitHandler.bind(this);
    }

    state = {
        timetable: []
    }

    componentDidMount() {
        fetch('http://jsonplaceholder.typicode.com/users')
        .then(res => res.json())
        .then((data) => {
            this.setState({ timetable: data })
        })
        .catch(console.log)
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
        );
    }
}

ReactDOM.render(<Search />, document.getElementById('root'));