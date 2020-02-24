import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
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
            <div class="timetable">
                <table class="timetable" >
                    <tr>
                        <th>Day</th>
                        <th>08:00</th>
                        <th>08:30</th>
                        <th>09:00</th>
                        <th>09:30</th>
                        <th>10:00</th>
                        <th>10:30</th>
                        <th>11:00</th>
                        <th>11:30</th>
                        <th>12:00</th>
                        <th>12:30</th>
                        <th>13:00</th>
                        <th>13:30</th>
                        <th>14:00</th>
                        <th>14:30</th>
                        <th>15:00</th>
                        <th>15:30</th>
                        <th>16:00</th>
                        <th>16:30</th>
                        <th>17:00</th>
                        <th>17:30</th>
                    </tr>
                    <tr>
                        <td>{Day}</td>
                        <td>{"08:00"}</td>
                        <td>{"08:30"}</td>
                        <td>{"09:00"}</td>
                        <td>{"09:30"}</td>
                        <td>{"10:00"}</td>
                        <td>{"10:30"}</td>
                        <td>{"11:00"}</td>
                        <td>{"11:30"}</td>
                        <td>{"12:00"}</td>
                        <td>{"12:30"}</td>
                        <td>{"13:00"}</td>
                        <td>{"13:30"}</td>
                        <td>{"14:00"}</td>
                        <td>{"14:30"}</td>
                        <td>{"15:00"}</td>
                        <td>{"15:30"}</td>
                        <td>{"16:00"}</td>
                        <td>{"16:30"}</td>
                        <td>{"17:00"}</td>
                        <td>{"17:30"}</td>
                    </tr>
                </table>
            </div>
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
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));