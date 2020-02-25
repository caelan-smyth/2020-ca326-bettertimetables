import React from 'react';

export default class Timetable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };

        this.formatRows = this.formatRows.bind(this);
    }

    formatData(timetable) {
            let response = [];
        timetable.map((entry) => {
            if (entry.isValid) {
                response.push(
                    <td>{entry.title}</td>
                )
            }
            else {
                response.push(
                    <td>&nbsp;</td>
                )
            }
        });
        return response
    }

    formatRows() {
            let response = []
        this.state.data.map((item) => {
            response.push(
                <tr>
                    <th scope="Row">{item.day}</th>
                    {this.formatData(item.timetable)}
                </tr>
            )
        });
        return response
    }

    render() {
        return (
            <div role="table">
                <table>
                    <thead>
                        <th>&nbsp;</th>
                        <th>09:00</th>
                    </thead>
                </table>
            </div>
        )
    }
}