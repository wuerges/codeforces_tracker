import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [contests, setContests] = useState(0);
  const [user, setUser] = useState("");

  const getData = () => {
    fetch(`/accs/${user}`
      , {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      }
    )
      .then(function (response) {
        console.log(response)
        return response.json();
      })
      .then(function (myJson) {
        setContests(myJson.result.count);
      });
  }

  function changeUser(e) {
    setUser(e.target.value);
  }

  return (
    <div className="App">
      <p id="userForm">
        <input type="text" value={user} onChange={changeUser} />
        <button onClick={(e) => { e.target.parentElement.style.display = 'none'; getData() }}>Fetch </button> </p>
      <p> {contests} </p>
    </div>
  );
}

export default App;
