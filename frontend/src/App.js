import React, { Component } from 'react';
import './App.css';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = { value: '' };
    this.submit = this.submit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.setState({ value: e.target.value });
  }

  submit(e) {
    e.preventDefault();
    let value = this.state.value;
    fetch('http://localhost:8000/get/', {
      method: 'POST',
      body: JSON.stringify({ value: value }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        let element = '<table>';
        for (let i in data) {
          element += '<tr>';
          for (let j in data[i][0]) {
            if (
              (j !== 'id' && j !== 'usn_id') ||
              (j !== 'id' && j !== 'usn_id')
            ) {
              element += '<td>' + data[i][0][j] + '</td>';
            }
          }
          element += '</td>';
        }
        element += '</table>';
        document.getElementById('put').innerHTML = element;
      });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.submit}>
          <h1>Hello</h1>
          <p>Enter your usn:</p>
          <input
            type='text'
            value={this.state.value}
            onChange={this.handleChange}
          />
          <input type='submit' value='submit' />
        </form>
        <div id='put'></div>
      </div>
    );
  }
}

export default App;
