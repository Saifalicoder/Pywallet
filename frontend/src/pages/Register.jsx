import Form from "../components/Form"
import Navbar from "../components/Navbarr"
function Register() {
    return (
    <>
      <Navbar></Navbar>
      <Form route="user/signup/" method="register" />
      </>
    )
    
}

export default Register