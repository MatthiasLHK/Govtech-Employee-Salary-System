import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import {useState, setState} from 'react';
import axios from 'axios';


function FileUploadBox() {
    const [file, setState] = useState()
    const fileReader = new FileReader();

    function handleChange(event) {
        // console.log(event.target.files[0])
        setState({file: event.target.files[0]})
        console.log(file)
        console.log(file['file']['name'])
    };

    function handleOnSubmit(event) {
        event.preventDefault();
        const data = new FormData();
        data.append('file', file['file']);
        data.append('filename', file['file']['name']);
        axios.post("http://localhost:5000/upload", data).then(res=>{console.log(res)}).catch(err=>{console.log(err)});
    };

    return (
        <div>
            <Form.Group controlId="formFile" className="mb-3">
                <Form.Label>Upload CSV File Here</Form.Label>
                <Form.Control 
                type="file"
                onChange={e => {handleChange(e)}}
                />
            </Form.Group>
            <Button onClick={e => {handleOnSubmit(e)}}>
                Submit File
            </Button>
        </div>
    )
}

export default FileUploadBox;