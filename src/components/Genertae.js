import React, { Component } from 'react';
import axios from 'axios';





class Generate extends Component {
    constructor() {
        
        super();
        this.state = {
            items: []
          };
   
        
    }

   
      handleClick(event){
        const bas_url = "http://127.0.0.1:5000";
        axios.post(bas_url + '/api/v1/resources/generate')
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
        
      }
      getData(event){
        const bas_url = "http://127.0.0.1:5000";
        axios.post(bas_url + '/api/v1/resources/getReport')
        .then((response) => {
          console.log(response);
          document.getElementById("int").innerHTML = "Integer: "+response['data'];
          document.getElementById("numeric").innerHTML = "Alphanumeric: "+response['data'];
          document.getElementById("batic").innerHTML = "Alphabatic: "+response['data'];
          document.getElementById("real").innerHTML = "Real number: "+response['data'];
        })
        .catch((error) => {
          console.log(error);
        });
        
      }
      
    render() {
        const {items } = this.state;
        return (
            
        <div>
           
            <button className="btn btn-success" onClick={this.handleClick}>Generate Link</button>
            <br/>
        <a href='http://127.0.0.1:5000/api/v1/resources/download' download>Click to download</a>
        <br/>
        <button className="btn btn-success" onClick={this.getData}>Report</button>
        <ul>
            <li   id="int"></li>
            <li   id="numeric"></li>
            <li   id="batic"></li>
            <li   id="real"></li>
        </ul>
        </div>)
    }
}
export default Generate;