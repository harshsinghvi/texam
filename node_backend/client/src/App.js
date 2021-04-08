import logo from './logo.svg';
import './App.css';
import { Component } from 'react';
import { DataGrid } from '@material-ui/data-grid';
import Navbar from './navbar'

// const URL="http://localhost:5000"
const URL="https://texam.projects.harshsinghvi.com/"


class App extends Component{
  constructor(props)
  {
    super(props)
    this.state = {data: {}, queCol: [], queRow:[], resCol:[], resRow: [], ansCol:[], ansRow:[]}
    this.getData = this.getData.bind(this)
  }

  async getData()
  {
    const req = await fetch(URL + '/admin-data')
    var data = await req.json()
    const qc = [
      { field: 'id', headerName: 'ID', width: 70 },
      { field: 'que', headerName: 'Question', width: 800 },
      { field: 'choices', headerName: 'Choices', width: 500 }
      // { field: 'answer', headerName: 'answer', width: 70 }
    ]

    const rc =[

      { field: 'timestamp', headerName: 'Timestamp', width: 300 },
      { field: 'name', headerName: 'Name', width: 130 },
      { field: 'email', headerName: 'Email', width: 250 },
      { field: 'responses', headerName: 'Responses', width: 600 },
      { field: 'penalties', headerName: 'Penalties', width: 150 },
      { field: 'id', headerName: 'ID', width: 250 }
    ]

    const ac = [
      { field: 'id', headerName: 'ID', width: 130 },
      { field: 'answer', headerName: 'Answer', width: 250 }
    ]
    for(var i=0 ; i < data['responses'].length;i++)
    {
      data['responses'][i]['responses'] = JSON.stringify(data['responses'][i]['responses'])
    }

    this.setState({data: data, 
      queCol:qc, queRow: data['questions'],
      resCol:rc, resRow: data['responses'],
      ansCol:ac, ansRow: data['answers']
    });
    return 0
  }

  // componentDidMount(){
  //   this.getData()
  // }
  componentWillMount(){
    this.getData();
  }

  render(){
    return(
      
      <div>
      <Navbar Update={this.getData} New={this.handleNewQuestion} />
      {/* <Navbar New={this.handleNewQuestion} /> */}

      {/* <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" /> */}
      <h1>TEXAM Portal</h1>
      {/* <button onClick={handleButton} value/> */}
      {/* <p> {this.state.columns} </p> */}
      {/* <br/> */}
      <h2>Questions</h2>
      <div style={{ height: 450, width: '100%' }}>
        <DataGrid rows={this.state.queRow} columns={this.state.queCol} />
      </div>
      <h2>Answers</h2>
      <div style={{ height: 450, width: '100%' }}>
        <DataGrid rows={this.state.ansRow} columns={this.state.ansCol} />
      </div>
      <h2>Responses</h2>
      <div style={{ height: 600, width: '100%' }}>
        <DataGrid rows={this.state.resRow} columns={this.state.resCol} />
      </div>
      </div>
    )
  }
}

export default App;
