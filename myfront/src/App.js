import logo from './logo.svg';
import './App.css';

function App() {
	function data(){
		fetch("http://127.0.0.1:8000/boards")
			.then(res => res.text())
			.catch(error => console(error))
			.finally(console.log('finish'))
	}

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
					{data()}
        </a>
      </header>
    </div>
  );
}

export default App;
