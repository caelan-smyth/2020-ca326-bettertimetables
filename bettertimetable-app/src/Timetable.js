import React from 'react';
import './Timetable.css';

export default class Timetable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: this.props.data || []
        };

        this.formatRows = this.formatRows.bind(this);
    }

    formatData(timeslots) {
        let result = [];
        timeslots.map((entry) => {
            if (entry.isvalid) {
                result.push(
                    <td>{entry.title}</td>
                )
            }
            else {
                result.push(
                    <td>&nbsp;</td>
                );
            }
        });
        return result;
    }

    formatRows() {
        let result = []
        this.state.data.map((item) => {
            result.push(
                <tr>
                    <th scope="Row">{item.day}</th>
                    {this.formatData(item.timeslots)}
                </tr>
            );
        });
        return result;
    }

    render() {
        {console.log(this.state.data)}
        return (
            <div role="table">
                <table>
                    <thead>
                        <tr>
                            <th scope="col">&nbsp;</th>
                            <th scope="col">09:00</th>
                            <th scope="col">09:30</th>
                            <th scope="col">10:00</th>
                            <th scope="col">10:30</th>
                            <th scope="col">11:00</th>
                            <th scope="col">11:30</th>
                            <th scope="col">12:00</th>
                            <th scope="col">12:30</th>
                            <th scope="col">13:00</th>
                            <th scope="col">13:30</th>
                            <th scope="col">14:00</th>
                            <th scope="col">14:30</th>
                            <th scope="col">15:00</th>
                            <th scope="col">15:30</th>
                            <th scope="col">16:00</th>
                            <th scope="col">16:30</th>
                            <th scope="col">17:00</th>
                            <th scope="col">17:30</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.formatRows()}
                    </tbody>
                </table>
            </div>
        );
    }
}