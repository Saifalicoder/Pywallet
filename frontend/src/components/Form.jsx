import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN , USER} from "../constants";
import "../styles/Form.css"
import LoadingIndicator from "./LoadingIndicator";


function Form({ route, method }) {
    const [email, setEmail] = useState("saifali1@gmail.com");
    const [password, setPassword] = useState("saif123");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();
        if(method==="register"){
        try {
              
                const res = await api.post(route, { email, password })
                    localStorage.setItem(ACCESS_TOKEN, res.data.access);
                    localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                    
                    navigate("/login")
           
            } catch (error) {
                alert(error)
            } finally {
                setLoading(false)
            }
            }
            
            else {
                try{
                const res = await api.post(route, { email, password })
               
                localStorage.clear()
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                localStorage.setItem(USER, JSON.stringify(res.data.user));

                navigate("/");
            
       
        } catch (error) {
            alert(error)
        } finally {
            setLoading(false)
        }
    };
    }
    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                className="form-input"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="email"
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            {loading && <LoadingIndicator />}
            <button className="form-button" type="submit">
                {name}
            </button>
        </form>
    );
}

export default Form