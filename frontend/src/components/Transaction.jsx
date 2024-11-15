import React from "react";
import "../styles/transaction.css"
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button'

function Transaction({ transaction }) {
 
    const formattedDate = new Date(transaction.date).toLocaleDateString("en-US")

    return (
      <>
      <div className="card">
      <div  style={{display:"flex",justifyContent:"space-between" , padding:"20px"}}>
         {transaction.transaction_type=="remove" ? <h2 className="card-title" style={{color:"red"}}>-{transaction.amount}</h2>:<h2 className="card-title " style={{color:"green"}}>{transaction.amount}</h2>}
         <div className="card-meta">
              <p><strong>Created by : </strong> {transaction.user.email}</p>
              <p><strong>Created at : </strong>{formattedDate}</p>
          </div>
      </div>
     
  
  </div>

      </>
    );
}

export default Transaction
