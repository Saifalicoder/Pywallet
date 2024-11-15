import { useState, useEffect } from "react";
import api from "../api";
import Transaction from "../components/Transaction"
import "../styles/Home.css"
import Navbar from '../components/Navbarr';
import {USER} from '../constants';


function Home() {
    const [alltransactions, setAllTransactions] = useState([]); 
    const [addmoney, setAddmoney] = useState(true);
    const [balance, setBalance] = useState(0);
    const [amount, setAmount] = useState();
    const [status, setStatus] = useState(true);
    const user = JSON.parse(localStorage.getItem(USER));
    console.log(user)
 
    useEffect(() => {
        getStatus();
        getBalance();
        getTransactions();
       
    }, []);

    const getTransactions = () => {
        console.log("hitting api")
        api
            .get("wallet/transactions/")
            .then((res) => res.data)
            .then((data) => {
                setAllTransactions(data); 
                
            })
            .catch();
    };
    const getBalance = () => {
       
        api
            .get("wallet/balance/")
            .then((res) => res.data)
            .then((data) => {console.log(data)
                setBalance(parseFloat(data.balance))
            })
            .catch();
    };
    const getStatus = () => {
       
        api
            .get("wallet/status/")
            .then((res) => res.data)
            .then((data) => {
                setStatus(data.status)
                
            })
            .catch();
    };
    const enable = () => {
       
        api
            .post("wallet/enable/")
            .then((res) => res.data)
            .then((data) => {console.log(data)
                getBalance();
                setStatus(true)
            })
            .catch();
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if(status){
            const payload = {
                amount
             }
             if(addmoney){
                 api
                 .post("wallet/add/", payload)
                 .then((res) => {
                     if (res.status === 201);
                     getTransactions();
                     getBalance()
                     setAmount(0)
                 })
                 .catch((err) => console.log(err));
             }
             else{
                 api
                 .post("wallet/remove/", payload)
                 .then((res) => {
                     if (res.status === 201);
                     getTransactions();
                     getBalance()
                     setAmount(0)
                 })
                 .catch((err) => console.log(err));
             }
          
        }
       
        else{
            alert("Wallet is disabled")
        }  
     
    };

    return (
        <>
        <Navbar></Navbar>
        <div className="main">  
            {console.log(alltransactions)}
            <form className="todoform" onSubmit={handleSubmit} >
                <h3 style={{color:"red" , textAlign:"center"}}>Make Transactions</h3>
                

                <label htmlFor="amount">Amount:</label>
                <br />
                <input
                     type="number"
    step="0.01"
                    id="title"
                    name="amount"
                    required
                    onChange={(e) => setAmount(e.target.value)}
                    value={parseFloat(amount)}
                />
                <div className="row">
                <div className="form-check col">
  <input className="form-check-input col" type="radio" name="transactionType" id="flexRadioDefault1"  checked={addmoney === true}
                onChange={() => setAddmoney(true)}/>
  <label className="form-check-label" for="flexRadioDefault1">
    Deposit
  </label>
</div>
                <div className="form-check col">
  <input className="form-check-input col" type="radio" name="transactionType" id="flexRadioDefault1"  checked={addmoney === false}
                onChange={() => setAddmoney(false)}/>
  <label className="form-check-label" for="flexRadioDefault1">
    Withdraw
  </label>
</div>
</div>

             <div className="btncontainer" style={{textAlign:"center"}}>
           
             <input type="submit" className="btn btn-primary"  value="Submit"
            disabled={!status}
             ></input>
             </div>
            </form>
            <hr />

            <div className="container" style={{backgroundColor:"rgb(223 210 246)", padding:"50px" , minHeight:"87vh" , borderRadius:"30px"}}>
                {
                    
                   status?<h2 className="fw-bold">Welcome {user.email}</h2>:(<div style={{display:"flex", justifyContent:"space-between"}}><h3 className="fw-bold" style={{color:"red" , textAlign:""}}>Welcome {user.email} your Wallet is disabled</h3><label class="btn btn-success">
                   <button
                       name="enable"
                       className="btn-check"
                       onClick={() => enable()}
                   />Enable wallet
                 
                   </label></div>)
                }
            
               <hr />   
                <div className="container notes-container" >
                    {
                        status?<><h3 className="fw-bold" style={{color:"black" , textAlign:"center"}}>Current Balance : {balance?balance:0}</h3>
                        {alltransactions.map((transaction) => (
                            <>
                            <Transaction transaction={transaction} key={transaction.id} />
                            </>
                        ))}</>:""
                    }
                
                </div>
            </div>
           
        </div>
        </>
    );
}

export default Home;
