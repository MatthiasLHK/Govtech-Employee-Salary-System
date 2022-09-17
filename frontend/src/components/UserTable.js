import Table from 'react-bootstrap/Table';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './UserTable.css'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const UserTable = (props) => {
    const [users, setUsers] = useState({blogs: []});
    const [filter, setFilters] = useState({min: 0, max: 100000000, sort: "+id"});

    useEffect(() => {
        const getData = async() => {
            const {data} = await axios.get("/users", {params: {minSalary: filter.min, maxSalary: filter.max, sort: filter.sort}})
            setUsers({blogs: data['results']});
        };
        getData();
    }, [setUsers])

    function onChange1(event) {
        setFilters({min: event.target.value})
    }

    function onChange2(event) {
        setFilters({max: event.target.value})
    }

    function onChange3(event) {
        setFilters({sort: "+id"})
    }

    function onChange4(event) {
        setFilters({sort: "-id"})
    }

    function onChange5(event) {
        setFilters({sort: "+name"})
    }

    function onChange6(event) {
        setFilters({sort: "-name"})
    }

    function onChange7(event) {
        setFilters({sort: "+login"})
    }

    function onChange8(event) {
        setFilters({sort: "-login"})
    }

    function onChange9(event) {
        setFilters({sort: "+salary"})
    }

    function onChange10(event) {
        setFilters({sort: "-salary"})
    }

    function onSubmit(event) {
        event.preventDefault();
        axios.get("/user", {params: {minSalary: filter.min, maxSalary: filter.max, sort: filter.sort}})
    }


    return (
        <div>
            <Form onSubmit={e=>{onSubmit(e)}}>
                <Form.Group>
                    <Form.Label>Min Salary</Form.Label>
                    <Form.Control
                    onChange={e=>{onChange1(e)}}
                    type='number'
                    />
                    <Form.Label>Max Salary</Form.Label>
                    <Form.Control
                    onChange={e=>{onChange2(e)}}
                    type='number'
                    />
                    <Form.Label>Sort By</Form.Label>
                    <Form.Select>
                        <option onChange={e=>{onChange3(e)}}>Id Asc</option>
                        <option onChange={e=>{onChange4(e)}}>Id Desc</option>
                        <option onChange={e=>{onChange5(e)}}>Name Asc</option>
                        <option onChange={e=>{onChange6(e)}}>Name Desc</option>
                        <option onChange={e=>{onChange7(e)}}>Login Asc</option>
                        <option onChange={e=>{onChange8(e)}}>Login Desc</option>
                        <option onChange={e=>{onChange9(e)}}>Salary Asc</option>
                        <option onChange={e=>{onChange10(e)}}>Salary Desc</option>
                    </Form.Select>
                    <Button type="submit">
                        Submit
                    </Button>
                </Form.Group>
            </Form>
            {/* <h className="header">Users</h>
        <Table striped bordered hover>
            
            <thead>
                <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Login</th>
                <th>Salary</th>
                </tr>
            </thead>
            <tbody>
                
                {
                    users.blogs.map((item) => {
                        return (
                            <tr>
                                <td className="entry1">{item['id']}</td>
                                <td className="entry2">{item['name']}</td>
                                <td className="entry3">{item['login']}</td>
                                <td className="entry4">{item['salary']}</td>
                            </tr>
                        )                     
                    })
                }
            </tbody>
        </Table> */}
        </div>
    )
}

export default UserTable;