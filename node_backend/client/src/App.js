import logo from './logo.svg';
import './App.css';
import { Component } from 'react';
import { DataGrid } from '@material-ui/data-grid';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

const URL="http://localhost:5000"

class App extends Component{
  constructor(props)
  {
    super(props)
    const columns = [
      { field: 'id', headerName: 'ID', width: 70 },
      { field: 'que', headerName: 'Question', width: 70 },
      { field: 'choices', headerName: 'Choices', width: 70 }
      // { field: 'answer', headerName: 'answer', width: 70 }
    ]
    this.state= {data: ' ', columns: columns, rows:[]}
  }

  async getData()
  {
    const req = await fetch(URL + '/questions')
    var data = await req.json()
    data['choices'] = " Ch"
    // console.log(data)
    this.setState({data:JSON.stringify(data),  rows: data});
  }

  // componentDidMount(){
  //   this.getData()
  // }
  componentWillMount(){
    this.getData();
  }

  render(){
    var rows = ["h1", "h2"]
    var columns = [{h1:"1",h2:'2'},{h1:"2",h2:"2"}];
    return(
      <div>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />

      <h1>Hello world</h1>
      {/* <button onClick={handleButton} value/> */}
      <p> {this.state.data} </p>
      <br/>
      <DataGrid rows={this.state.rows} columns={this.state.columns} pageSize={5} checkboxSelection />
      
      </div>

    )
  }
}

export default App;
