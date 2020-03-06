/* eslint react/prop-types: 0 */
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
                console.log(entry.type)
                if (entry.type === "Lec.") {
                    result.push(
                        <td style={{backgroundColor:"#F92672"}} name={entry.title}>{entry.code}<br />{entry.title}<br />{entry.loc}<br />{entry.weeks}</td>
                    )
                }
                else if (entry.type === "Prac.") {
                    result.push(
                        <td style={{backgroundColor:"#7289da"}} name={entry.title}>{entry.code}<br />{entry.title}<br />{entry.loc}<br />{entry.weeks}</td>
                    )
                }
                else {
                    result.push(
                        <td style={{backgroundColor:"#FD971F"}} name={entry.title}>{entry.code}<br />{entry.title}<br />{entry.loc}<br />{entry.weeks}</td>
                    )
                }
            }
            else {
                result.push(
                    <td name="blank cell">&nbsp;</td>
                );
            }
        });
        return result;
    }

    formatRows() {
        let result = []
        console.log(this.state.data)
        this.props.data.days.map((item) => {
            result.push(
                <tr>
                    <th name={item.day} scope="Row">{item.day}</th>
                    {this.formatData(item.timeslots)}
                </tr>
            );
        });
        return result;
    }

    render() {
        return (
            <div role="table">
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <table name="timetable">
                    <thead>
                        <tr>
                            <th name="day heading" scope="col">Day</th>
                            <th name="nine o'clock heading" scope="col">09:00</th>
                            <th name="half nine heading" scope="col">09:30</th>
                            <th name="ten o'clock heading" scope="col">10:00</th>
                            <th name="half ten heading" scope="col">10:30</th>
                            <th name="eleven o'clock heading" scope="col">11:00</th>
                            <th name="half eleven heading" scope="col">11:30</th>
                            <th name="twelve o'clock heading" scope="col">12:00</th>
                            <th name="half twelve heading" scope="col">12:30</th>
                            <th name="one o'clock heading" scope="col">13:00</th>
                            <th name="half one heading" scope="col">13:30</th>
                            <th name="two o'clock heading" scope="col">14:00</th>
                            <th name="half two heading" scope="col">14:30</th>
                            <th name="three o'clock heading" scope="col">15:00</th>
                            <th name="half three heading" scope="col">15:30</th>
                            <th name="four o'clock heading" scope="col">16:00</th>
                            <th name="half four heading" scope="col">16:30</th>
                            <th name="five o'clock heading" scope="col">17:00</th>
                            <th name="half five heading" scope="col">17:30</th>
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