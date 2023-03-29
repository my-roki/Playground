import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Login from "./routes/Login";
import Home from "./routes/Home";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
