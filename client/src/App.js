import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';



function App() {
  
  const [contests, setContests] = useState(0);
  const [official, setOfficial] = useState(0);
  const [user, setUser] = useState(0);
  
  const countOfficial=()=> {
    fetch(`https://codeforces.com/api/user.rating?handle=${user}`
    ,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {
      setOfficial(myJson.result.length);
    });

  }
  const getData=()=>{
    fetch('fake.json'
    ,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    )
      .then(function(response){
        // console.log(response)
        return response.json();
      })
      .then(function(myJson) {
        setContests(myJson.result.count);
        setUser(myJson.result.user);
        // console.log(myJson);
      });
  }
  useEffect(()=>{
    countOfficial();
    getData();
  },[]);

  return (
    <div className="App">
      <p> {user} </p>
      <p> {contests} </p>      
      <p> {official} </p>      
    </div>
  );
}

export default App;
