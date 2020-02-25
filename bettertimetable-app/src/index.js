import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import Timetable from './Timetable.js';
import './index.css';

/*function Timetable() {
    useEffect(() => {
        fetchTimetable();
    }, []);

    const [items, setItems] = useState([]);

    const fetchTimetable = async () => {
        const data = await fetch(
            //api link goes here
        );

        const items = await data.json();
        console.log(items);
        setItems(items);
    };

    return (
    );
}*/

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
        this.submitHandler = this.submitHandler.bind(this);
    }

    changeHandler(event) {
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    submitHandler(event) {
        event.preventDefault();
        useEffect(() => {
            fetchTimetable();
        }, []);
    
        const fetchTimetable = async () => {
            let url = ""//api link goes here/ + {this.state.course} + "/" + {this.state.year} + "/" + {this.state.semester};
            const response = await fetch(url);        
            const items = await response.json();
            console.log(items);
            this.setState({data: items.results})
        };

        if (!this.state.data.length) {
            return <div>Timetable not found</div>
        }

        return(
            <Timetable data={this.data} />
        );
    }

    render() {
        return (
            <div role="main">
                <h1 title="Search by Course code">Programme Search</h1>
                <form method="get" role="form">
                    <div class="form-field">
                        <label>
                            Programme:
                            <input type="text" name="course" placeholder="Programme Code" onChange={this.changeHandler} />
                        </label>
                    </div>
                    <div class="form-field">
                        <label>
                            Year of Study:
                            <input type="text" name="year" placeholder="Year" onChange={this.changeHandler} />
                        </label>
                    </div>
                    <div class="form-select">
                        <label>
                            Semester:
                            <select name="semester" aria-valuenow="1" aria-valuemin="1" aria-valuemax="2" >
                                <option value="1">1</option>
                                <option value="2">2</option>
                            </select>
                        </label>
                    </div>
                    <div class="form-submit">
                        <label>
                            Search
                            <input type="Submit" value="Submit" name="search for course" onSubmit={this.submitHandler.bind(this, )} />
                        </label>
                    </div>
                </form>
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));