import Form from "../components/Form";
import Navbar from "../components/Navbarr";

function Login() {

    return (
        <>
          <Navbar></Navbar>
            <Form route="user/token/" method="login" />
            <div className="col" style={{ display: 'flex', flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
               
            </div>
        </>
    );
}

export default Login;
