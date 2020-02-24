import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import Timetable from 'timetablecomponents/Timetable.js';
//import Search from './Search.js';

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
    <CsvToHtmlTable data={data} csvDelimiter="," />
    );
}*/

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            course: '',
            year: null,
            semester: null,
            data: `
            a,b,c
            d,e,f
            `
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
            let data = await fetch(
                //"api link goes here/" + {this.state.course} + "/" + {this.state.year} + "/" + {this.state.semester}
            );
    
            const items = await data.json();
            console.log(items);
            this.setState({[data]:items})
        };
    
        /*return (
            something to handle the timetable here
        );*/
    }

    render() {
        return (
            <div>
                <h1 title="Search by Course code">Programme Search</h1>
                <form method="get">
                    <label>
                        Programme:
                        <input type="text" name="course" placeholder="Programme Code" onChange={this.changeHandler} />
                    </label>
                    <label>
                        Year of Study:
                        <input type="text" name="year" placeholder="Year" onChange={this.changeHandler} />
                    </label>
                    <label>
                        Semester:
                        <select name="semester" >
                            <option value="1">1</option>
                            <option value="2">2</option>
                        </select>
                    </label>
                    <label>
                        Search
                        <input type="Submit" value="Submit" name="search for course" onSubmit={this.submitHandler.bind(this, )} />
                    </label>
                </form>
                <CsvToHtmlTable
                 data={this.data}
                 csvDelimiter="," />
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));