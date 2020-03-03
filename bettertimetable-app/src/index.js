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
            data: [],
            type: '',
            day: '',
        };

        this.filterDays = this.filterDays.bind(this);
        this.filterType = this.filterType.bind(this);
        this.filter = this.filter.bind(this);
        this.changeHandler = this.changeHandler.bind(this);
    }

    filterType = (timeslots) => {
        if(timeslots.isvalid === 0 || timeslots.type !== this.state.type) return {isvalid: 0}
        return timeslots
    }

    filterDays = (day) => {
        if(day.day != this.state.day) {
            return {day: '', timeslots: []}
        }
        return day;
    }

    filter = (data) => {
        let days = data.days
        console.log(data)
        if(this.state.day !== '')
        days = days.map((day) => this.filterDays(day))
        if(this.state.type !== '') {
        days = days.map((day) => {
            return { day: day.day, timeslots: day.timeslots.map((timeslots) => this.filterType(timeslots))}
        })
    }
        return {...data, days}
    }

    changeHandler(event) { //take form parameters and store them in state
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    submitHandler(event) { //do something when the user submits the form
        event.preventDefault();
            
        const fetchTimetable = async () => { //get data from the API and store it in state
            let url = 'http://localhost:5000/' + this.state.course + '/' + this.state.year + '/' + this.state.semester
            fetch(url)
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
                            <button name="Search for course" onClick={this.submitHandler.bind(this)}>Search</button>
                        </label>
                    </div>
                    <div className="form-filtering">
                        <label>
                            Filter by Day:
                            <select name="day" onChange={this.changeHandler}>
                                <option value='' name="no filter">None</option>
                                <option value="Mon" name="Monday filter">Monday</option>
                                <option value="Tue" name="Tuesday filter">Tuesday</option>
                                <option value="Wed" name="Wednesday filter">Wednesday</option>
                                <option value="Thu" name="Thursday filter">Thursday</option>
                                <option value="Fri" name="Friday filter">Friday</option>
                            </select>
                        </label>
                    </div>
                    <div className="form-filtering">
                        <label>
                            Filter by Type:
                            <select name="type" onChange={this.changeHandler}>
                                <option value=''>None</option>
                                <option value="Lec.">Lecture</option>
                                <option value="Prac.">Practical</option>
                                <option value="Tut.">Tutorial</option>
                            </select>
                        </label>
                    </div>
                </form>
                {this.state.data.length !== 0 ? <Timetable data={this.filter(this.state.data)} /> : ''} {/*display table if data is present otherwise display nothing*/}
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));