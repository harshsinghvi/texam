import React, {useState, Component} from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

// const URL="http://localhost:5000"
const URL="https://texam.projects.harshsinghvi.com/"


// export default function Newdialog() {
//   const [open, setOpen] = React.useState(false);
//   var id = 0;

//   const handleClickOpen = () => {
//     setOpen(true);
//   };

//   const handleClose = () => {
//     setOpen(false);
//   };

//   const  handleNew = async () =>{
//     // data
//     // r = fetch(URL+'/new-question', {
//     //     body:""
//     // })
//     await handleClose()
//     console.log(open)
//     console.log(id)
//   } 
//   handleChange(event){
//     id = event.target.value
//   }


//   return (
//     <div>
//       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />

//       <Button variant="outlined" color="primary" onClick={handleClickOpen}>
//       <i className="fa fa-plus-circle" aria-hidden="true"></i>
//       </Button>
//       <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
//         <DialogTitle id="form-dialog-title">New Question</DialogTitle>
//         <DialogContent>
//           <DialogContentText>
//             Enter The Details.
//           </DialogContentText>
//           <TextField
//             value={id}
//             onChange={handleChange}
//             autoFocus
//             margin="dense"
//             id="que"
//             label="Question Text"
//             type="text"
//             fullWidth
//           />
//           <TextField
//             autoFocus
//             margin="dense"
//             id="choice1"
//             label="Choice 1"
//             type="text"
//             fullWidth
//           />
//         <TextField
//             autoFocus
//             margin="dense"
//             id="choice2"
//             label="Choice 2"
//             type="text"
//             fullWidth
//           />
//          <TextField
//             autoFocus
//             margin="dense"
//             id="choice3"
//             label="Choice 3"
//             type="text"
//             fullWidth
//           />

//         <TextField
//             autoFocus
//             margin="dense"
//             id="choice4"
//             label="Choice 4"
//             type="text"
//             fullWidth
//           />
//           <TextField
//             autoFocus
//             margin="dense"
//             id="ans"
//             label="Answer"
//             type="text"
//             fullWidth
//           />
//         </DialogContent>
//         <DialogActions>
//           <Button onClick={handleClose} color="primary">
//             Cancel
//           </Button>
//           <Button onClick={handleNew} color="primary">
//           Create <i className="fa fa-plus-circle" aria-hidden="true"></i>
//           </Button>
//         </DialogActions>
//       </Dialog>
//     </div>
//   );
// }


class Newdialog extends Component {

    constructor(props){
        super(props)
        this.state = {open:false, id:'', que:'', choice1:'', choice2:'', choice3:'',choice4:'', ans:''}
        this.handleClickOpen = this.handleClickOpen.bind(this)
        this.handleClose = this.handleClose.bind(this)
        this.setOpen = this.setOpen.bind(this)
        this.handleChangeID = this.handleChangeID.bind(this)
        this.handleChangeC1 = this.handleChangeC1.bind(this)
        this.handleChangeC2 = this.handleChangeC2.bind(this)
        this.handleChangeC3 = this.handleChangeC3.bind(this)
        this.handleChangeC4 = this.handleChangeC4.bind(this)
        this.handleChangeQue = this.handleChangeQue.bind(this)
        this.handleChangeAns = this.handleChangeAns.bind(this)
    }
    setOpen = (st) => {
        this.setState({open:st})
    }

    handleClickOpen = () => {
      this.setOpen(true);
    };
  
    handleClose = () => {
      this.setOpen(false);
    };
  
    handleNew =  () =>{
      fetch(URL+'/new-question', {
          method:'POST',
          mode:'no-cors',
          headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
              id: this.state.id,
              que: this.state.que,
              answer: this.state.ans,
              choices:[this.state.choice1,this.state.choice2,this.state.choice3,this.state.choice4]
          })
        // body: JSON.stringify(this.state)
      }).then( r => {this.handleClose();this.props.Update() })
    
      console.log(this.state)
    }

    handleChangeID(event)
    {
        this.setState({id: event.target.value});
    }

    handleChangeQue(event)
    {
        this.setState({que: event.target.value});
    }
  
    handleChangeC1(event)
    {
        this.setState({choice1: event.target.value});
    }
  
    handleChangeC2(event)
    {
        this.setState({choice2: event.target.value});
    }
  
    handleChangeC3(event)
    {
        this.setState({choice3: event.target.value});
    }

    handleChangeC4(event)
    {
        this.setState({choice4: event.target.value});
    }

    handleChangeAns(event)
    {
        this.setState({ans: event.target.value});
    }

  render(){
    return (
      <div>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  
        <Button variant="outlined" color="primary" onClick={this.handleClickOpen}>
        <i className="fa fa-plus-circle" aria-hidden="true"></i>
        </Button>
        <Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">New Question</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Enter The Details.
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="id"
              label="ID"
              type="text"
              fullWidth
              value={this.state.id}
              onChange={this.handleChangeID}
            />
            <TextField
              autoFocus
              margin="dense"
              id="que"
              label="Question Text"
              type="text"
              fullWidth
              value={this.state.que}
              onChange={this.handleChangeQue}
            />
            <TextField
              autoFocus
              margin="dense"
              id="choice1"
              label="Choice 1"
              type="text"
              fullWidth
              value={this.state.choice1}
              onChange={this.handleChangeC1}
            />
          <TextField
              autoFocus
              margin="dense"
              id="choice2"
              label="Choice 2"
              type="text"
              fullWidth
              value={this.state.choice2}
              onChange={this.handleChangeC2}
            />
           <TextField
              autoFocus
              margin="dense"
              id="choice3"
              label="Choice 3"
              type="text"
              fullWidth
              value={this.state.choice3}
              onChange={this.handleChangeC3}
            />
  
          <TextField
              autoFocus
              margin="dense"
              id="choice4"
              label="Choice 4"
              type="text"
              fullWidth
              value={this.state.choice4}
              onChange={this.handleChangeC4}
            />
            <TextField
              autoFocus
              margin="dense"
              id="ans"
              label="Answer"
              type="text"
              fullWidth
              value={this.state.ans}
              onChange={this.handleChangeAns}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={this.handleNew} color="primary">
            Create <i className="fa fa-plus-circle" aria-hidden="true"></i>
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );}
  }

  class DeleteDialog extends Component {

    constructor(props){
        super(props)
        this.state = {open:false, id:'', que:'', choice1:'', choice2:'', choice3:'',choice4:'', ans:''}
        this.handleClickOpen = this.handleClickOpen.bind(this)
        this.handleClose = this.handleClose.bind(this)
        this.setOpen = this.setOpen.bind(this)
        this.handleDelete = this.handleDelete.bind(this)
        this.handleChangeID = this.handleChangeID.bind(this)

    }
    setOpen = (st) => {
        this.setState({open:st})
    }

    handleClickOpen = () => {
      this.setOpen(true);
    };
  
    handleClose = () => {
      this.setOpen(false);
    };
  

    handleDelete = () => {
        fetch(URL+'/delete-question', {
            method:'POST',
            mode:'no-cors',
            headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
                id: this.state.id,
            })
          // body: JSON.stringify(this.state)
        }).then( r => {this.handleClose();this.props.Update() })

    }

    handleChangeID(event)
    {
        this.setState({id: event.target.value});
    }

  render(){
    return (
      <div>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  
        <Button variant="outlined" color="primary" onClick={this.handleClickOpen}>
        <i className="fa fa-trash" aria-hidden="true"></i>
        </Button>
        <Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">New Question</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Enter Question ID
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="id"
              label="ID"
              type="text"
              fullWidth
              value={this.state.id}
              onChange={this.handleChangeID}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={this.handleDelete} color="primary">
            Delete <i className="fa fa-trash" aria-hidden="true"></i>
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );}
  }

export {Newdialog}
export {DeleteDialog}