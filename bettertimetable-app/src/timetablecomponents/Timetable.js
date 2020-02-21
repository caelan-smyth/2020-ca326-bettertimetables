import React, { useState, useEffect } from 'react';
import { CsvToHtmlTable } from 'react-csv-to-table';
import './Timetable.css';

function Timetable() {
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
}

export default Timetable;