import React from 'react';
import ReactDOM from 'react-dom';
import Timetable from './Timetable.js';
import './index.css';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            course: '',
            year: null,
            semester: null,
            data: [] 
        };

        this.changeHandler = this.changeHandler.bind(this);
    }

    changeHandler(event) { //take form parameters and store them in state
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    submitHandler(event) { //do something when the user submits the form
        event.preventDefault();
            
        const fetchTimetable = async () => { //get data from the API and store it in state
            fetch('http://localhost:5000/test')
            .then(res => res.json())
            .then((items => {
                this.setState({ data: items })
            }))
            .catch((e) =>(console.log(e.message)))
            console.log(this.state.data)
        };

        fetchTimetable();
    }

    render() { //main function for displaying React components
        return (
            <div role="main">
                <h1 title="Search by Course code">Programme Search</h1>
                <form method="get" name="search form">
                    <div className="form-field">
                        <label>
                            Programme:
                            <input type="text" name="course" placeholder="Programme Code" onChange={this.changeHandler} />
                        </label>
                    </div>
                    <div className="form-field">
                        <label>
                            Year of Study:
                            <input type="text" name="year" placeholder="Year" onChange={this.changeHandler} />
                        </label>
                    </div>
                    <div className="form-select">
                        <label>
                            Semester:
                            <select name="semester" onChange={this.changeHandler} >
                                <option value="1">1</option>
                                <option value="2">2</option>
                            </select>
                        </label>
                    </div>
                    <div className="form-submit">
                        <label>
                            Search
                            <input type="Submit" value="Search" name="search for course button" onClick={this.submitHandler.bind(this)} />
                        </label>
                    </div>
                </form>
                {this.state.data.length !== 0 ? <Timetable data={this.state.data} /> : ''}
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));