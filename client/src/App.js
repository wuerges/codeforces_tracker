import logo from './logo.svg';
import selo from './selo.png';
import assinatura from './assinatura.png';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [horas, setHoras] = useState(0);
  const [nome, setNome] = useState("????");
  const [matricula, setMatricula] = useState("00000-0000-00");

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
        setHoras(myJson.result.count * 2);
      });
  }

  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const today = new Date(Date.now()).toLocaleDateString('pt-BR', options);
  const year = new Date(Date.now()).getFullYear();

  function changeUser(e) {
    setUser(e.target.value);
  }

  return <>
    <div className="App">
      <p id="userForm">
        <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
        <input type="text" value={matricula} onChange={(e) => setMatricula(e.target.value)} />
        <input type="text" value={user} onChange={changeUser} />
        <button onClick={(e) => { e.target.parentElement.style.display = 'none'; getData() }}>Fetch </button>
      </p>
    </div>
    <div style={{ "margin": "3cm" }}>
      <center>
        <img src={selo} style={{ 'max-width': '100px' }} />
        <h2>
          SERVIÇO PÚBLICO FEDERAL
        </h2>
        <h3>
          Universidade Federal da Fronteira Sul
        </h3>
        <h1>
          Declaração
        </h1>
      </center>

      <p>
        Eu, Emílio Wuerges - SIAPE 2052314, coordenador do Clube de Programação do
        Curso de Ciência da Computação do campus de Chapecó da UFFS, declaro que o
        estudante {nome} - Matrícula {matricula}, participou dos
        treinamentos para a Maratona de programação da SBC de {year}, totalizando a carga
        horária de {horas} horas.
      </p>

      <p>
        Chapecó, {today}
      </p>


      <center>
        <img src={assinatura} style={{ 'max-width': '300px' }} />
        <p>
          Emílio Wuerges <br /> Coordenador do Clube de Programação
        </p>
      </center>



    </div>
  </>;
}

export default App;
