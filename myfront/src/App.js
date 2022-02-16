import React, { Component  } from 'react';

const API_HOST = 'http://localhost:8000/boards';

let _csrfToken = null;

async function getCsrfToken() {
  if (_csrfToken === null) {
    const response = await fetch(`${API_HOST}/csrf`, {
            credentials: 'include',
    });
        const data = await response.json();
        _csrfToken = data.csrfToken;
  }
    return _csrfToken;
}

async function testRequest() {
  const data = {
    'title':'react_test',
    'content':'content',
    'author':'lee',
    'password':'1234'
  }
  const response = await fetch (`${API_HOST}`, {
    method: 'POST',
    headers:(
             {'X-CSRFToken': await getCsrfToken()}
    ),
    credentials: 'include',
    body: JSON.stringify(data),
  })
}

class App extends Component {

  constructor(props) {
        super(props);
    this.state = {
            testPost: 'KO',
    };
  }

  async componentDidMount() {
    this.setState({
                        testPost: await testRequest(),
    });
  }

  render() {
    return (
                  <div>
                    <p>Test POST request: {this.state.testPost}</p>
                  </div>
    );
  }
}

export default App;

