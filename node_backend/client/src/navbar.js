import { Component } from 'react';
import './navbar.css'
import {Newdialog,DeleteDialog} from './dialog'

class Navbar extends Component{
    render(){
        return( 
    <div className="topnav">

    <a className="active" href="/">Exam Admin</a>
    <a className="active" style={{ float: 'right' }} href='https://texam.projects.harshsinghvi.com/'> Results </a>
    <a className="active" style={{ float: 'right' }} > 
    <Newdialog Update={this.props.Update} />
    </a>
    <a className="active" style={{ float: 'right' }} > 
    <DeleteDialog Update={this.props.Update} />
    </a>
    </div>
    )}
}

export default Navbar;