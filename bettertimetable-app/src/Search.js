import React from 'react';
import 'react-router-dom';

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
        
        history.push("/${}")
    }

    render() {
        return (
            <div>
                <h1 title="Search by Course code">Programme Search</h1>
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
                        <input type="Submit" value="Submit" name="search for course" onSubmit={this.submitHandler} />
                    </label>
                </form>
            </div>
        );
    }
}

export default Search;