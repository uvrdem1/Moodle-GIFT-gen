import {

  BrowserRouter,
  Routes,
  Route,
  Navigate

} from 'react-router-dom'

import Home from './pages/home'
import Login from './pages/Login'
import Register from './pages/Register'
import History from './pages/History'


function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/login"
          element={<Login />}
        />

        <Route
          path="/register"
          element={<Register />}
        />

        <Route
          path="/history"
          element={<History />}
        />

        <Route
          path="*"
          element={<Navigate to="/" />}
        />

      </Routes>

    </BrowserRouter>
  )
}

export default App