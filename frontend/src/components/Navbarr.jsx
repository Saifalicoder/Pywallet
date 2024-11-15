import React from 'react'
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/esm/Container';
import { Link } from "react-router-dom";
import { ACCESS_TOKEN } from '../constants';
import { useLocation } from 'react-router-dom';

const Navbarr = () => {
  const location = useLocation()
  const is_authorized = localStorage.getItem(ACCESS_TOKEN,null)
  console.log(location.pathname)
  return (
    <Navbar bg="dark" variant="dark"> {/* Updated variant for dark theme */}
    <Container style={{padding:"0px 20px"}}>
        <Navbar.Brand href="#home" style={{fontWeight:"800", color:"yellow"}}>PyWallet</Navbar.Brand>
        {is_authorized?<Nav className=" nav-link mx-end">
            <Link to="/logout" style={{textDecoration:"none"}}><Nav.Link href="#features" style={{color:"white"}}>logout</Nav.Link></Link>

        </Nav>:null}
        {!is_authorized && (location.pathname ==="/login")?<Nav className=" nav-link mx-end">
            <Link to="/register" style={{textDecoration:"none"}}><Nav.Link href="#features" style={{color:"white"}}>Sign up</Nav.Link></Link>

        </Nav>:null
}
        {!is_authorized && location.pathname ==="/signup"?<Nav className=" nav-link mx-end">
            <Link to="/login" style={{textDecoration:"none"}}><Nav.Link href="#features" style={{color:"white"}}>Login</Nav.Link></Link>

        </Nav>:null
}
    </Container>
</Navbar>
  )
}

export default Navbarr